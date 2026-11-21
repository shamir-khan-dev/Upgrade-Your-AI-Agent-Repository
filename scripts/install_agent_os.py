import os
import shutil
from pathlib import Path

def install_agent_os():
    root = Path(__file__).resolve().parent.parent
    rules_src = root / "rules" / "AGENTS.md"
    skills_src = root / "skills"
    target_cwd = Path.cwd()
    
    print("\nInstalling Universal Agent Rules and Skills into active workspace...\n")
    if not rules_src.exists():
        print(f"Error: Source rules not found at {rules_src}")
        return 1
        
    target_agents_file = target_cwd / "AGENTS.md"
    shutil.copy2(rules_src, target_agents_file)
    print(f" [DONE] Installed workspace rules: {target_agents_file}")
    
    target_cursor_file = target_cwd / ".cursorrules"
    shutil.copy2(rules_src, target_cursor_file)
    print(f" [DONE] Installed Cursor configuration: {target_cursor_file}")
    
    # Optional IDE skills directory discovery
    home = Path.home()
    ide_dirs = [
        home / ".gemini" / "config" / "skills",
        home / ".agents" / "skills",
        home / ".cursor" / "skills"
    ]
    
    for ide_dir in ide_dirs:
        if ide_dir.parent.exists():
            ide_dir.mkdir(parents=True, exist_ok=True)
            print(f" [SYNC] Updating IDE skills at: {ide_dir}")
            for skill_path in skills_src.iterdir():
                if skill_path.is_dir():
                    dst_skill = ide_dir / skill_path.name
                    if dst_skill.exists():
                        shutil.rmtree(dst_skill)
                    shutil.copytree(skill_path, dst_skill)
                    print(f"   + Synced skill: {skill_path.name}")
                    
    print("\nUniversal Agent OS and Major Skills successfully installed.\n")
    return 0

if __name__ == "__main__":
    install_agent_os()
