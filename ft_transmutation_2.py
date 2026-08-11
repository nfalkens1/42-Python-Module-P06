import alchemy


def main() -> None:
    header = "=== Transmutation 2 ==="
    print(header)
    print("Import alchemy module only")
    crafting_gold = alchemy.lead_to_gold()
    print(f"Testing lead to gold: {crafting_gold}")


if __name__ == "__main__":
    main()
