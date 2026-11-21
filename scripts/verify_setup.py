import sys
from pathlib import Path

def run_verification():
    root = Path(__file__).resolve().parent.parent
    prompts_dir = root / "prompts"
    rules_dir = root / "rules"
    skills_dir = root / "skills"
    
    checks = [
        ("Master Onboarding Prompt", prompts_dir / "MASTER_AGENT_ONBOARDING_PROMPT.md"),
        ("Quickstart Prompt", prompts_dir / "QUICKSTART_PROMPT.txt"),
        ("Universal Agent Rules", rules_dir / "AGENTS.md"),
        ("Claude Configuration", rules_dir / "CLAUDE.md"),
        ("Major Skills Directory", skills_dir)
    ]
    
    major_skills = [
        "test-driven-development",
        "ponytail",
        "graphify",
        "floorplan",
        "spec-driven-development",
        "planning-and-task-breakdown",
        "incremental-implementation",
        "unslop",
        "code-review-and-quality",
        "security-and-hardening",
        "skillspector",
        "browser-use",
        "karpathy-guidelines",
        "brag",
        "obscura"
    ]
    
    print("\nVerifying AI Agent OS Configuration...\n")
    passed = 0
    for name, path in checks:
        if path.exists():
            print(f" [PASS] {name} is active ({path.name})")
            passed += 1
        else:
            print(f" [FAIL] {name} missing")
            
    print("\nVerifying Major Skills Catalog...\n")
    skills_passed = 0
    for skill in major_skills:
        skill_file = skills_dir / skill / "SKILL.md"
        if skill_file.exists():
            print(f" [PASS] Skill: {skill}")
            skills_passed += 1
        else:
            print(f" [FAIL] Skill missing: {skill}")
            
    total_checks = len(checks) + len(major_skills)
    total_passed = passed + skills_passed
    print(f"\nResult: {total_passed}/{total_checks} verification checks passed.\n")
    return 0 if total_passed == total_checks else 1

if __name__ == "__main__":
    sys.exit(run_verification())
