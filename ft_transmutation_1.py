import alchemy.transmutation


def main() -> None:
    header = "=== Transmutation 1 ==="
    print(header)
    print("Import transmutation module directly")
    crafting_gold = alchemy.transmutation.lead_to_gold()
    print(f"Testing lead to gold: {crafting_gold}")


if __name__ == "__main__":
    main()
