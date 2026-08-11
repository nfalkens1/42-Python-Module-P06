from alchemy import create_air


def main() -> None:
    header = "=== Alembic 5 ==="
    print(header)
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
