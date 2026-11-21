---
name: browser-use
description: Direct browser control via Chrome DevTools Protocol (CDP) and Playwright for AI driven web interaction, automation, deep scraping, form autofill, job portal navigation, and visual verification.
---

# Browser Use: Autonomous Web Automation Engine

Direct browser control via Chrome DevTools Protocol (CDP) and Playwright. Enables autonomous agents to navigate complex web pages, interact with dynamic elements, handle user authentication sessions, fill multi step application forms, and extract structured data.

## When to Use

• **Complex Web Interaction**: Clicking, form typing, selecting dropdowns, and handling reactive web single page applications (React, Angular, Vue, Workday).  
• **Dynamic & Authenticated Pages**: Interacting with logged in user sessions, cookies, and local storage state.  
• **Visual Testing & Audits**: Capturing full page screenshots, verifying rendered UI layout, and inspecting DOM accessibility.  
• **Automated Application & Portal Navigation**: Filling multi stage internship portals, Greenhouse, Lever, and Workday application flows with validation.  
• **Bot Protected & JavaScript Rendered Extraction**: When basic HTTP curl requests fail or return empty client rendered shells.

## When Not to Use

• **Static Public Documentation**: If a plain HTTP request or markdown fetcher can read the page cleanly, avoid launching browser processes.  
• **Standard REST APIs**: Use direct HTTP endpoints rather than driving a visual browser.

## Core Architecture & Automation Patterns

### 1. Headless Browser Initialization
```python
import asyncio
from playwright.async_api import async_playwright

async def run_browser_task(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = await context.new_page()
        await page.goto(url, wait_until='networkidle')
        await browser.close()
```

### 2. Multi Step Form Autofill Pattern
• Identify selectors using stable attributes (`name`, `id`, `aria-label`, `data-testid`).  
• Wait for elements to be visible and actionable before dispatching click or fill events.  
• Trigger native change events to ensure reactive frontend frameworks register field input.  
• Capture screenshot proof after completion to confirm successful submission.

### 3. Session Reuse & Tab Management
• Maintain one primary tab per domain to prevent resource exhaustion.  
• Reuse established browser contexts to preserve authentication cookies and session state.  
• Always close child pages and browser instances cleanly inside execution handlers.
