# Module Extraction AI Agent (Streamlit Application)

## Overview

This project is an AI-powered Streamlit application that extracts structured product modules and submodules from documentation-based help websites.

The system converts unstructured documentation content into a clean, machine-readable JSON format that can be used by product teams, AI assistants, and analytics systems.

---

## Features

- Accepts documentation URLs as input
- Crawls documentation pages within the same domain
- Extracts and cleans meaningful content
- Identifies modules and submodules
- Generates accurate descriptions from extracted content only
- Displays output as structured JSON
- Simple Streamlit-based user interface
- One-click setup for users

---

## Tech Stack

- Python 3.9+
- Streamlit
- Requests
- BeautifulSoup

---

## Design Decisions

- Agent-based architecture was used to ensure modularity, explainability, and ease of debugging.
- The system prioritizes robustness over strict HTML assumptions, as real-world documentation varies widely.
- A safe fallback strategy is implemented to prevent empty outputs when documentation structure is inconsistent.
- Streamlit is used purely as a presentation layer; all intelligence resides in the backend pipeline.
- Feature-level documentation pages are recommended for best results.

---

## Project Structure

module-extraction-ai-agent/
├── app.py
├── module_extractor.py
├── run_app.bat
├── requirements.txt
├── README.md
├── assumptions_and_limitations.md
├── src/
│ ├── input_handler.py
│ ├── crawler.py
│ ├── content_extractor.py
│ ├── structure_detector.py
│ ├── inference_engine.py
│ ├── description_generator.py
│ └── output_formatter.py
├── output/
└── logs/

---

## How to Run (No Command Line Required)

### Windows

1. Install Python 3.9+ from https://www.python.org
2. Double-click `run_app.bat`
3. The application will open automatically in your browser

---

## How to Use

1. Open the Streamlit application in your browser
2. Enter one or more documentation URLs (one per line)

Example:
https://wordpress.org/documentation/article/

3. Click **Run Module Extraction**
4. View extracted modules and submodules as JSON output

---

## Output Format

[
{
"module": "Module Name",
"Description": "Description derived from documentation content.",
"Submodules": {
"Submodule Name": "Submodule description."
}
}
]

---

## Assumptions

- Input URLs are documentation/help websites
- Content is publicly accessible and written in English
- Documentation uses structured HTML headings

---

## Limitations

- The system performs best on feature-level documentation pages rather than high-level index pages.
- Documentation sites with heavy JavaScript rendering may produce limited results.
- Some documentation index pages may contain navigational headings that are not true feature modules.
- Crawl depth is intentionally limited to ensure fast execution for demonstration purposes.
- The application does not handle authentication-gated documentation.

---

## Conclusion

This project demonstrates an agent-based AI approach to extracting structured knowledge from documentation websites using a simple and user-friendly Streamlit interface.
