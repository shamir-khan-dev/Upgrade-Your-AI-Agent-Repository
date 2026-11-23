---
name: playwright-mcp
description: Direct Microsoft Playwright MCP integration for automated browser execution, accessibility tree snapshots, end to end web testing, form automation, and visual verification.
---

# Microsoft Playwright MCP Automation Engine

Official Microsoft Playwright Model Context Protocol (MCP) server integration for intelligent browser automation, accessibility tree inspection, and automated end to end verification.

Repository: `https://github.com/microsoft/playwright-mcp`

## Core Architectural Advantages

• **Accessibility Tree Snapshots**: Rather than streaming heavy visual frames or raw pixels that consume thousands of LLM tokens, Playwright MCP captures structured accessibility trees, exposing buttons, inputs, links, and text elements with zero token bloat.
• **Determinism**: Native Playwright waits ensure elements are actionable, attached, and settled before executing clicks or text input, eliminating test flakiness.
• **Full Emulation**: Supports mobile viewports, custom user agents, geolocation overrides, and device profiles (Pixel, iPhone).
• **Diagnostic Interception**: Captures browser console errors, failed network requests, and visual full page screenshots on demand.

## When To Automatically Trigger This Skill

Automatically invoke this skill whenever:
• Verifying newly created or modified web pages, dashboards, or components
• Running end to end user journey tests (sign in, checkout, booking, form submission)
• Auditing web applications for accessibility compliance and broken DOM hierarchies
• Testing responsive layouts across mobile and desktop viewport dimensions
• Performing automated data extraction or scraping from client rendered web applications

## MCP Server Invocation

Configured in `mcp_config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest"],
      "type": "stdio"
    }
  }
}
```

## Available Browser Operations

• **browser_navigate**: Opens target URL and returns accessibility tree snapshot.
• **browser_click**: Selects and clicks DOM target by selector or role label.
• **browser_type**: Fills input fields with text and triggers change events.
• **browser_snapshot**: Returns compact accessibility tree of current viewport.
• **browser_screenshot**: Captures visual proof of render state or layout bugs.
• **browser_console_logs**: Retrieves browser runtime logs, warnings, and errors.
• **browser_network_requests**: Inspects outbound API calls and HTTP status codes.

## Integration With Skill Autopilot

In Phase 4 of `skill-autopilot`, after editing or building any web application:
1. Launch local or preview web server.
2. Trigger Playwright MCP to navigate to the live interface.
3. Verify interactive controls, check console for zero runtime errors, and confirm layout stability before marking the task complete.
