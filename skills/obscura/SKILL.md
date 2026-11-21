---
name: obscura
description: High performance, low memory headless browser engine in Rust for AI agents and web scraping with Chrome DevTools Protocol and anti detect capabilities.
---

# Obscura: Rust Headless Browser Engine for AI Agents

Obscura is a lightweight headless browser engine written in Rust designed as a drop in alternative to headless Chrome for AI agent automation, deep web scraping, and browser testing.

### Key Architectural Advantages
• Memory Efficiency: Consumes roughly 30 MB of memory per instance compared to 200+ MB on standard headless Chrome.
• Speed: Instant startup with 85 ms average page load times.
• Built in Anti Detect: Automatically masks headless browser footprints, spoofing canvas, audio, and navigator properties without external plugins.
• Chrome DevTools Protocol: Exposes a standard CDP endpoint compatible with Playwright, Puppeteer, and custom WebSocket clients.

### When to Use Obscura
• High volume web scraping where Chrome memory overhead exhausts system resources.
• AI agent browser navigation requiring lightweight background execution.
• Sites with aggressive anti automation fingerprinting where standard headless Chrome gets blocked.
• Exporting clean screenshots, PDF page captures, and DOM trees.

### Integration Patterns

#### 1. Python Playwright CDP Connection
```python
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://example.com")
        print(await page.title())
        await browser.close()

asyncio.run(run())
```

#### 2. Node.js Puppeteer CDP Connection
```javascript
import puppeteer from 'puppeteer';

const browser = await puppeteer.connect({
  browserURL: 'http://localhost:9222'
});
const page = await browser.newPage();
await page.goto('https://example.com');
console.log(await page.title());
await browser.disconnect();
```

### Best Practices
• Connection Reuse: Maintain a single Obscura daemon process and spawn isolated browser contexts for each agent task.
• Resource Hygiene: Close inactive pages to maintain the 30 MB baseline memory footprint.
• Fallback Strategy: If an obscure proprietary browser feature is required, fall back cleanly to standard Playwright browser binaries.
