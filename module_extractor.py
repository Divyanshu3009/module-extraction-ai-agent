import argparse

from src.input_handler import validate_urls
from src.crawler import DocumentationCrawler
from src.content_extractor import extract_clean_content
from src.structure_detector import detect_structure
from src.inference_engine import infer_modules
from src.description_generator import attach_descriptions
from src.output_formatter import save_output


def run_pipeline(urls):
    validated_urls = validate_urls(urls)

    all_structures = []

    for url in validated_urls:
        crawler = DocumentationCrawler(url)
        pages = crawler.crawl()

        for _, soup in pages.items():
            content_blocks = extract_clean_content(soup)
            structure = detect_structure(content_blocks)
            all_structures.extend(structure)

    inferred_modules = infer_modules(all_structures)
    final_output = attach_descriptions(inferred_modules)

    save_output(final_output)

    print("✅ Module extraction completed successfully.")
    print("📄 Output saved to output/sample_output.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Module Extraction AI Agent")
    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="One or more documentation URLs"
    )

    args = parser.parse_args()
    run_pipeline(args.urls)
