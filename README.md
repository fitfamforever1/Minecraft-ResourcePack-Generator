# Custom Item Model Setup

Add custom textures to Minecraft items using a Python script and item model. Only 1.21.5 is supported, you need to edit syntax in the `.py` file to let it work for other versions. Only item display are support and armor display doesn't work.

---

## Folder Structure

Place files as follows before running the script:

```
assets/minecraft/
├── script.py
└── textures/
    └── item/
        ├── example_1.png
        └── example/
            └── example_2_pickaxe.png
```

---

## Steps

1. Download the `.py` file and place it inside `assets/minecraft/`
2. Create a `textures/` folder inside `assets/minecraft/`
3. Create an `item/` folder inside `textures/`
4. Place all `.png` texture files inside `item/` — subfolders are supported
5. Rename the `.png` files to your liking
6. Run the `.py` file using ```python main.py``` in cmd/terminal (Requires python3)
7. Apply the item model in-game (see below)

---

## Item Model Naming

The item model name is the texture's path relative to `item/`, without the `.png` extension.

| File path | Item model |
|---|---|
| `item/example_1.png` | `example_1` |
| `item/example/example_2.png` | `example/example_2` |

---

## Applying In-Game

### ItemEdit plugin

```
/ie itemmodel rune/rune_7
```

> [ItemEdit on Modrinth](https://modrinth.com/plugin/itemedit)

### Command generator

Use the give command generator at [gamergeeks.net](https://www.gamergeeks.net/apps/minecraft/give-command-generator) to build a `/give` command with the `item_model` component set to your texture name. The opstion for item model is present in extras tab.

<img width="472" height="42" alt="image" src="https://github.com/user-attachments/assets/24b50b10-0b4b-4a38-9e85-6e5a394f3119" />
