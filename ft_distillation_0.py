from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    header = "=== Distillation 0 ==="
    print(header)
    structure = "Direct access to alchemy/potions.py"
    print(structure)
    strength_pot = strength_potion()
    healing_pot = healing_potion()
    print(f"Testing strength_potion: {strength_pot}")
    print(f"Testing healing_potion: {healing_pot}")


if __name__ == "__main__":
    main()
