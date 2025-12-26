from bs4 import BeautifulSoup


def extract_clean_content(soup: BeautifulSoup):
    """
    Extracts meaningful documentation content from HTML soup.
    Removes scripts, styles, navigation, and footer elements.
    Returns a list of ordered content blocks.
    """

    # Remove unwanted tags
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    content_blocks = []

    for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        text = element.get_text(strip=True)

        if not text:
            continue

        content_blocks.append({
            "tag": element.name,
            "text": text
        })

    return content_blocks
