import json
import os


def save_output(data, output_path="output/sample_output.json"):
    """
    Saves the final structured output to a JSON file.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
