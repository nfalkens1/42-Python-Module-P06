import alchemy


def main() -> None:
    header = "=== Alembic 4 ==="
    print(header)
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will create an exception!")
    print("Testing the hidden create_earth: ")
    try:
        print(alchemy.create_earth())
    except AttributeError as e:
        print(str(e))


if __name__ == "__main__":
    main()
