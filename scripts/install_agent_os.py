import os
import shutil
import sys
from pathlib import Path

def install_agent_os():
    root = Path(__file__).resolve().parent.parent
    rules_src = root / "rules" / "AGENTS.md"
    claude_src = root / "rules" / "CLAUDE.md"
    skills_src = root / "skills"
    target_cwd = Path.cwd()
    home = Path.home()
    
    print("\n=======================================================")
    print("   AI AGENT OS: GLOBAL AUTOMATIC CONFIGURATION")
    print("=======================================================\n")
    
    if not rules_src.exists():
        print(f"Error: Source rules not found at {rules_src}")
        return 1

    # 1. Local Workspace Installation
    print("[1/3] Configuring Active Workspace...")
    target_agents = target_cwd / "AGENTS.md"
    target_cursor = target_cwd / ".cursorrules"
    shutil.copy2(rules_src, target_agents)
    shutil.copy2(rules_src, target_cursor)
    print(f" [OK] Local workspace rules: {target_agents}")
    print(f" [OK] Local cursor rules: {target_cursor}")

    # 2. Global IDE Rules (Applies to ALL new projects automatically)
    print("\n[2/3] Installing Global Rules for All New Projects...")
    global_rules_destinations = [
        home / ".cursorrules",                               # Cursor global
        home / ".gemini" / "GEMINI.md",                       # Antigravity global instructions
        home / ".gemini" / "config" / "AGENTS.md",            # Antigravity config rules
        home / ".claude" / "CLAUDE.md",                       # Claude Code global memory
        home / ".agents" / "AGENTS.md"                        # Universal agent standard
    ]

    for dest in global_rules_destinations:
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            src_file = claude_src if "claude" in str(dest).lower() else rules_src
            shutil.copy2(src_file, dest)
            print(f" [OK] Global Rule Active: {dest}")
        except Exception as e:
            print(f" [SKIP] Could not write {dest}: {e}")

    # 3. Global Skills Sync (Makes all 14 skills available globally)
    print("\n[3/3] Installing Skills Globally Across All AI Environments...")
    global_skill_dirs = [
        home / ".gemini" / "config" / "skills",
        home / ".agents" / "skills",
        home / ".cursor" / "skills"
    ]

    synced_count = 0
    for target_skill_dir in global_skill_dirs:
        try:
            target_skill_dir.mkdir(parents=True, exist_ok=True)
            print(f"\n Target Directory: {target_skill_dir}")
            for skill_folder in skills_src.iterdir():
                if skill_folder.is_dir():
                    dest_skill = target_skill_dir / skill_folder.name
                    if dest_skill.exists():
                        shutil.rmtree(dest_skill)
                    shutil.copytree(skill_folder, dest_skill)
                    print(f"   + Synced: {skill_folder.name}")
                    synced_count += 1
        except Exception as e:
            print(f" [SKIP] Could not write to {target_skill_dir}: {e}")

    print("\n=======================================================")
    print(" [COMPLETE] Your AI Agent is now upgraded globally!")
    print(" Every new project, folder, or chat will automatically")
    print(" use these 14 skills and follow the staff engineer rules.")
    print("=======================================================\n")
    return 0

if __name__ == "__main__":
    sys.exit(install_agent_os())
