from alchemy.grimoire import light_spellbook


def main() -> None:
    header = "=== Kaboom 0 ==="
    print(header)
    print("Using grimoire module directly")
    ingredients = "Earth, wind and fire"
    spell = "Fantasy"
    record_light_spell = light_spellbook.light_spell_record(spell, ingredients)
    print(f"Testing record light spell: {record_light_spell}")


if __name__ == "__main__":
    main()
