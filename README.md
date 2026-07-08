# OKF
**Local-First Developer Knowledge Vault & Exhaust Synthesizer**

Chronos is an autonomous, local-first background agent that turns raw developer "exhaust" (terminal commands and daily scratchpad notes) into a structured, version-controlled knowledge graph. 

Instead of losing your daily bug fixes and terminal discoveries, Chronos intercepts your OS history, processes it through a local LLM, and builds a permanent, machine-readable memory bank using the **Open Knowledge Format (OKF)**.

## Key Features

* **Zero-Cloud Architecture:** Runs entirely locally using Python and **Ollama (Llama 3.2)**. No expensive API keys, no data leaving your machine.
* **Native OS Ingestion:** Automatically parses and cleans macOS Zsh history (`~/.zsh_history`) to capture real developer actions without manual data entry.
* **Open Knowledge Format (OKF):** Synthesizes chaotic history into clean Markdown files equipped with structured YAML frontmatter, making your brain completely grep-able and Git-ready.
* **Agentic Categorization:** The AI autonomously tags entries as `BugFix`, `Tooling`, or `Concept` based on context.

## System Architecture

```text
[ ~/.zsh_history ] ──(Trigger)──► [ Python Scraper (history.py) ]
                                            │
                                            ▼
[ Local Llama 3.2 via Ollama ] ◄──(JSON Prompt via controller.py)
                                            │
                                            ▼
[ OKF Generator (main.py) ] ────► [ ~/.vault/*.md ]
