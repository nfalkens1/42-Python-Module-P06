import alchemy.elements


def main() -> None:
    header = "=== Alembic 2 ==="
    print(header)
    structure = "'import ...'"
    print(f"Accessing alchemy/elements.py using {structure} structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
