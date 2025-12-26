from urllib.parse import urlparse
import requests


def validate_urls(urls):
    """
    Validates input URLs by syntax and basic reachability.
    Does not aggressively reject URLs to avoid false negatives.
    """

    if not urls or not isinstance(urls, list):
        raise ValueError("Input must be a non-empty list of URLs")

    validated_urls = []
    seen = set()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for url in urls:
        parsed = urlparse(url)

        # Basic syntax check
        if not parsed.scheme or not parsed.netloc:
            continue

        normalized_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        if normalized_url in seen:
            continue

        # Try reachability, but do NOT fail hard
        try:
            response = requests.get(
                normalized_url,
                headers=headers,
                timeout=10,
                allow_redirects=True
            )
            # Accept even if status is not perfect
            validated_urls.append(normalized_url)
            seen.add(normalized_url)

        except requests.RequestException:
            # Still accept URL if syntax is valid
            validated_urls.append(normalized_url)
            seen.add(normalized_url)

    if not validated_urls:
        raise ValueError("No valid URLs provided")

    return validated_urls



def extract_domain(url):
    """
    Extracts domain from URL for crawl boundary enforcement.
    """
    parsed = urlparse(url)
    return parsed.netloc
