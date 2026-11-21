---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Enforces thinking before coding, simplicity first with minimum code, surgical edits, and goal driven verification.
---

# Karpathy Guidelines

Behavioral guidelines to reduce common AI coding mistakes, derived from Andrej Karpathy's observations on software generation pitfalls.

## 1. Think Before Coding
• State assumptions explicitly. If uncertain, ask clarifying questions instead of guessing.
• If multiple interpretations exist, present them openly rather than choosing silently.
• If a simpler approach exists, say so and push back when warranted.
• If requirements are unclear, pause immediately and name what is ambiguous.

## 2. Simplicity First
• Write the minimum code that solves the problem. Add nothing speculative.
• Zero unrequested features or premature abstractions for single use code.
• Zero unneeded flexibility or configurability.
• Zero defensive error handling for impossible scenarios.
• If a solution can be expressed in 50 lines instead of 200, rewrite and simplify.

## 3. Surgical Changes
• Touch only what must change to satisfy the user request.
• Match existing codebase style, even if you would personally format it differently.
• Never perform drive by refactoring or modify adjacent formatting.
• Clean up only your own orphans by removing unused imports or variables introduced by your edits.

## 4. Goal Driven Execution
• Define concrete success criteria before writing implementation code.
• Turn vague tasks into verifiable goals: write tests reproducing bugs or validating new behavior first, then pass them.
• Execute in small steps: step, verify check, confirm green.

