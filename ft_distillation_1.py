import alchemy


def main() -> None:
    header = "=== Distillation 1 ==="
    print(header)
    structure = "'import alchemy'"
    print(f"Using: {structure} structure to access potions")
    strength_pot = alchemy.strength_potion()
    print(f"Testing strength_potion: {strength_pot}")
    heal_alias = alchemy.heal()
    print(f"Testing heal alias: {heal_alias}")


if __name__ == "__main__":
    main()
