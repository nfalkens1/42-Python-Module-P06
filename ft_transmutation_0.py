import alchemy.transmutation.recipes


def main() -> None:
    header = "=== Transmutation 0 ==="
    print(header)
    path = "alchemy/transmutation/recipes.py"
    print(f"Using file {path} directly")
    crafting_gold = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {crafting_gold}")


if __name__ == "__main__":
    main()
