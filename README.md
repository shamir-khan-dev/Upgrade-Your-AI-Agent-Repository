# Upgrade Your AI Agent

A production grade operating protocol and prompt architecture designed to transform default conversational AI assistants into rigorous, test driven Staff Software Engineers.

### The Problem With Default AI Coding Assistants

Out of the box, most conversational coding models exhibit predictable failure modes:
• Speculative Bloat: adding unnecessary libraries, wrappers, and layers when ten lines of native standard library code would solve the problem.
• Lack of Verification: assuming generated code works without writing failing automated tests first.
• AI Slop UI: defaulting to generic neon purple gradients, floating glow cards, and repetitive marketing blocks.
• Monolithic Dumps: attempting to write hundreds of lines in a single pass without atomic milestones.

This repository provides the exact operating rules, onboarding prompts, and verification harnesses required to eliminate these bad habits.

***

### The Three Core Operating Rules

1. Minimalism First
Prioritize native language features and standard libraries over third party dependencies. Enforce YAGNI (You Aren't Gonna Need It).

2. Proof First (Test Driven Development)
Write failing automated unit tests before writing application logic. Code is only considered complete when passing verified tests.

3. Craftsmanship and Anti Slop Frontend Engineering
Design clean, bespoke user interfaces using thoughtful typography, intentional spacing systems, and persistent theme states.

***

### One Click Master Onboarding Prompt

Copy and paste the following prompt into your AI agent (Antigravity, Cursor, Claude Code, or ChatGPT) at the start of your project:

```text
Act as an elite Staff Software Engineer and mentor. Follow three non negotiable rules:
1. Minimalism First: write the simplest clean code using native standard libraries, no bloat or unnecessary dependencies.
2. Proof First: follow test driven development, writing automated tests before logic.
3. Zero Slop: produce bespoke production quality design without generic AI aesthetics. Plan before coding and explain your engineering decisions clearly.
```

***

### Repository Structure

• prompts/MASTER_AGENT_ONBOARDING_PROMPT.md: comprehensive staff engineer mentor instructions.
• prompts/QUICKSTART_PROMPT.txt: single sentence injection for rapid coding sessions.
• rules/AGENTS.md: universal drop in workspace protocol for autonomous agents.
• rules/CLAUDE.md: tailored rules for Claude Code environments.
• scripts/install_agent_os.py: one click workspace setup script.
• scripts/verify_setup.py: automated verification test suite.

***

### Quickstart

1. Clone this repository into your workspace:
```bash
git clone <REPOSITORY_URL>
cd Upgrade_Your_AI_Agent
```

2. Run the automated verification suite:
```bash
python scripts/verify_setup.py
```

3. Install the rules into any project:
```bash
python scripts/install_agent_os.py
```
