import os
import shutil
from pathlib import Path

def install_agent_os():
    root = Path(__file__).resolve().parent.parent
    rules_src = root / "rules" / "AGENTS.md"
    target_cwd = Path.cwd()
    
    print("\nInstalling Universal Agent Rules into active workspace...\n")
    if not rules_src.exists():
        print(f"Error: Source rules not found at {rules_src}")
        return 1
        
    target_agents_file = target_cwd / "AGENTS.md"
    shutil.copy2(rules_src, target_agents_file)
    print(f" [DONE] Installed workspace rules: {target_agents_file}")
    
    target_cursor_file = target_cwd / ".cursorrules"
    shutil.copy2(rules_src, target_cursor_file)
    print(f" [DONE] Installed Cursor configuration: {target_cursor_file}")
    
    print("\nUniversal Agent OS successfully installed.\n")
    return 0

if __name__ == "__main__":
    install_agent_os()
