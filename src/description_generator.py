def generate_description(content_blocks, fallback_title="", max_sentences=2):
    """
    Generates a concise description from content blocks.
    Falls back to title if content is empty.
    """

    if not content_blocks:
        if fallback_title:
            return f"This section covers {fallback_title.lower()}."
        return ""

    joined_text = " ".join(content_blocks)
    sentences = joined_text.split(".")
    selected = sentences[:max_sentences]

    description = ". ".join(s.strip() for s in selected if s.strip())

    if description and not description.endswith("."):
        description += "."

    return description


def attach_descriptions(modules):
    """
    Attaches descriptions to modules and submodules.
    """

    final_output = []

    for module in modules:
        module_name = module["module"]
        module_description = generate_description(
            module.get("content", []),
            fallback_title=module_name
        )

        submodule_map = {}

        for sub in module.get("submodules", []):
            sub_name = sub["submodule"]
            sub_desc = generate_description(
                sub.get("content", []),
                fallback_title=sub_name
            )
            submodule_map[sub_name] = sub_desc

        final_output.append({
            "module": module_name,
            "Description": module_description,
            "Submodules": submodule_map
        })

    return final_output
