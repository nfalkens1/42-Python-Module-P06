from alchemy.elements import create_air


def main() -> None:
    header = "=== Alembic 3 ==="
    print(header)
    structure = "'from ... import ...'"
    print(f"Accessing alchemy/elements.py using {structure} structure")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
