# Minecraft Resource Pack Item Generator

#Import necessary libraries
import os
import json

# Define the directory of the script for relative paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define templates for item models and item files
item_held_template = {
  "parent": "minecraft:item/handheld",
  "textures": {
    "layer0": "minecraft:item/{name}"
  }
}

item_generated_template = {
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "minecraft:item/{name}"
  }
}

model_template = {
  "model": {
    "type": "minecraft:model",
    "model": "minecraft:item/{name}"
  }
}

# Function to find missing item models and item files based on textures
def get_missing_items(textures_path="textures/item/", items_path="items/"):
    textures_path = os.path.join(SCRIPT_DIR, textures_path)
    items_path = os.path.join(SCRIPT_DIR, items_path)

    held = []
    generated = []
    handheld_keywords = ("sword", "pickaxe", "axe", "shovel", "hoe")

    for root, dirs, files in os.walk(textures_path):
        for f in files:
            if f.endswith(".png"):
                rel_dir = os.path.relpath(root, textures_path)
                base_name = os.path.splitext(f)[0]
                name = base_name if rel_dir == "." else f"{rel_dir}/{base_name}"
                name = name.replace("\\", "/")

                json_path = os.path.join(items_path, name + ".json")
                if not os.path.isfile(json_path):
                    if any(kw in base_name for kw in handheld_keywords):
                        held.append(name)
                    else:
                        generated.append(name)

    return held, generated

# Function to create item model JSON files and item JSON files for missing items
def create_files(held, generated):
    os.makedirs(os.path.join(SCRIPT_DIR, "models/item"), exist_ok=True)
    os.makedirs(os.path.join(SCRIPT_DIR, "items"), exist_ok=True)

    all_items = [(n, "held") for n in held] + [(n, "generated") for n in generated]

    for name, kind in all_items:
        model_out = os.path.join(SCRIPT_DIR, f"models/item/{name}.json")
        item_out = os.path.join(SCRIPT_DIR, f"items/{name}.json")

        os.makedirs(os.path.dirname(model_out), exist_ok=True)
        os.makedirs(os.path.dirname(item_out), exist_ok=True)

        if kind == "held":
            model_data = json.loads(json.dumps(item_held_template).replace("{name}", name))
        else:
            model_data = json.loads(json.dumps(item_generated_template).replace("{name}", name))

        with open(model_out, "w") as f:
            json.dump(model_data, f, indent=2)

        item_data = json.loads(json.dumps(model_template).replace("{name}", name))
        with open(item_out, "w") as f:
            json.dump(item_data, f, indent=2)

    print(f"Created {len(held)} handheld + {len(generated)} generated model files.")
    print(f"Created {len(all_items)} item files.")

# Main execution
if __name__ == "__main__":
    held, generated = get_missing_items()
    print("Held:", held)
    print("Generated:", generated)
    create_files(held, generated)
