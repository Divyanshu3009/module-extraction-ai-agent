def detect_structure(content_blocks):
    """
    Robust structure detection with fallback.
    Builds modules directly from headings if needed.
    """

    structure = []
    current_module = None

    for block in content_blocks:
        tag = block["tag"]
        text = block["text"]

        if tag == "h1":
            current_module = {
                "module": text,
                "content": [],
                "submodules": []
            }
            structure.append(current_module)

        elif tag == "h2" and current_module:
            current_module["submodules"].append({
                "submodule": text,
                "content": []
            })

        elif current_module:
            current_module["content"].append(text)

    # 🚨 FALLBACK: if nothing structured was created
    if not structure:
        for block in content_blocks:
            if block["tag"] in ("h1", "h2"):
                structure.append({
                    "module": block["text"],
                    "content": [],
                    "submodules": []
                })

    return structure
