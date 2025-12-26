import re


def normalize_title(title: str) -> str:
    """
    Cleans and normalizes module/submodule titles.
    """
    title = re.sub(r"\s+", " ", title)
    return title.strip().title()


def infer_modules(structure):
    """
    Refines detected structure into final modules and submodules.
    Removes empty sections and normalizes names.
    """

    refined_modules = []

    for module in structure:
        module_name = normalize_title(module.get("module", ""))

        if not module_name:
            continue

        module_content = module.get("content", [])
        submodules = module.get("submodules", [])

        refined_submodules = []

        for sub in submodules:
            sub_name = normalize_title(sub.get("submodule", ""))
            sub_content = sub.get("content", [])

            if sub_name:
                refined_submodules.append({
                    "submodule": sub_name,
                    "content": sub_content
                })

            refined_modules.append({
                "module": module_name,
                "content": module_content,
                "submodules": refined_submodules
            })

    return refined_modules
