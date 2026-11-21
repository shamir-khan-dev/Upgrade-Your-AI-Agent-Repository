import sys
from pathlib import Path

def run_verification():
    root = Path(__file__).resolve().parent.parent
    prompts_dir = root / "prompts"
    rules_dir = root / "rules"
    
    checks = [
        ("Master Onboarding Prompt", prompts_dir / "MASTER_AGENT_ONBOARDING_PROMPT.md"),
        ("Quickstart Prompt", prompts_dir / "QUICKSTART_PROMPT.txt"),
        ("Universal Agent Rules", rules_dir / "AGENTS.md"),
        ("Claude Configuration", rules_dir / "CLAUDE.md")
    ]
    
    print("\nVerifying AI Agent OS Configuration...\n")
    passed = 0
    for name, path in checks:
        if path.exists() and path.stat().st_size > 0:
            print(f" [PASS] {name} is active ({path.name})")
            passed += 1
        else:
            print(f" [FAIL] {name} missing or empty")
            
    print(f"\nResult: {passed}/{len(checks)} verification checks passed.\n")
    return 0 if passed == len(checks) else 1

if __name__ == "__main__":
    sys.exit(run_verification())
