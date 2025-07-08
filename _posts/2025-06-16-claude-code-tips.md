---
date: 2025-06-16
layout: post
title: Claude Code Tips
description: "This is a practical guide for using Claude Code, a command line tool for agentic coding. This post covers tips for effectively using Claude Code."
categories: [Tech]
---

## Tips

### Work with GitHub CLI
Claude knows how to use the GitHub CLI to interact with GitHub for creating issues, opening pull requests, reading comments, and more.

### Handling Large Inputs
- **Don't** paste long, large content in Claude Code
- **Do** use file-based workflow. Store the input in a file and ask Claude Code to read the file

### Turn on macOS Dictation
You can speak to enter the prompts, making it like chatting with a real agent.

### Make a Plan Before Implementing
Ask Claude Code to propose a plan and verify the feasibility. You may use prompts like: "propose a few solutions to the XXX issues."

### Give Claude More Context

#### CLAUDE.md
- CLAUDE.md is a special file that Claude automatically pulls into context when starting a conversation.
- This is the ideal place for documenting how to set up or contribute to the project.

#### Other methods
- You can use pipe to pass context into Claude Code: `cat foo.txt | claude`
- Ask Claude to read files or fetch URLs

## Key Bindings

- **Escape**: Press Esc to interrupt at any time
- **Double-tap Escape**: Jump back to history message
- **Shift+Tab**: Toggle between auto-accept mode, plan mode, and normal mode

## Use Headless Mode

Claude Code has headless mode for non-interactive environments like CI, pre-commit hooks, build scripts, and automation. Use the `-p` flag with a prompt to enable headless mode, and `--output-format stream-json` for streaming JSON output.

### Examples:
- `claude -p "<your prompt>" --output-format stream-json --verbose`
- `claude -p "<your prompt>" --output-format json | your_command`

## Useful Commands

- `/init`: Generate a CLAUDE.md project summary
- `/vim`: Toggle between Vim mode and normal editing mode
- `/clear`: Use this command between tasks to reset the context window and keep context focused
- `/memory`: Open any memory file in your system editor for additional memory
- `claude commit`: Create a Git commit, co-authored by Claude
- `claude -r`: Resume the previous conversation

### Custom Slash Commands
You can create your own slash commands as Markdown files to build reusable prompts:
- **Project commands**: Store in `.claude/commands/` to share with your team
- **Personal commands**: Store in `~/.claude/commands/` for personal use across projects
- Use `$ARGUMENTS` placeholder for dynamic content, and reference files with `@` prefix
- Example: Create `.claude/commands/optimize.md` with "Analyze this code for performance issues: $ARGUMENTS" and use with `/optimize myfile.js`

## Links

- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [YouTube Tutorial](https://www.youtube.com/watch?v=6eBSHbLKuN0)
- [Claude Code Memory Documentation](https://docs.anthropic.com/en/docs/claude-code/memory)