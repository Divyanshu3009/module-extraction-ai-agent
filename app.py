import streamlit as st

from src.input_handler import validate_urls
from src.crawler import DocumentationCrawler
from src.content_extractor import extract_clean_content
from src.structure_detector import detect_structure
from src.inference_engine import infer_modules
from src.description_generator import attach_descriptions
from src.output_formatter import save_output


# -------------------- Streamlit Page Setup --------------------
st.set_page_config(
    page_title="Module Extraction AI Agent",
    layout="wide"
)

st.title("Module Extraction AI Agent")
st.write(
    "This AI-powered application extracts structured product modules and "
    "submodules from documentation websites."
)

# -------------------- Input Section --------------------
st.subheader("Enter Documentation URLs")

urls_input = st.text_area(
    "Provide one or more documentation URLs (one per line):",
    height=120,
    placeholder="https://www.chargebee.com/docs/2.0/"
)

run_button = st.button("Run Module Extraction")

# -------------------- Processing Logic --------------------
if run_button:
    if not urls_input.strip():
        st.error("Please enter at least one documentation URL.")
    else:
        urls = [u.strip() for u in urls_input.splitlines() if u.strip()]

        with st.spinner("Running AI agents on documentation..."):
            try:
                # 1. Validate URLs
                validated_urls = validate_urls(urls)

                all_structures = []

                # 2. Crawl and extract content
                for url in validated_urls:
                    crawler = DocumentationCrawler(url)
                    pages = crawler.crawl()

                    for _, soup in pages.items():
                        content_blocks = extract_clean_content(soup)
                        structure = detect_structure(content_blocks)
                        all_structures.extend(structure)

                # 3. Infer modules
                inferred_modules = infer_modules(all_structures)

                # 4. Final output (with fallback)
                if inferred_modules:
                    final_output = attach_descriptions(inferred_modules)
                else:
                    # Safe fallback: show detected headings as modules
                    final_output = []
                    seen = set()

                    for item in all_structures:
                        title = item.get("module")
                        if title and title not in seen:
                            final_output.append({
                                "module": title,
                                "Description": f"This section covers {title.lower()}.",
                                "Submodules": {}
                            })
                            seen.add(title)

                # 5. Save and display
                save_output(final_output)

                st.success("Module extraction completed successfully!")
                st.subheader("Extracted Modules (JSON Output)")
                st.json(final_output)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
