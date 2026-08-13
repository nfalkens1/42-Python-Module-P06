if __name__ == "__main__":
    header = "=== Kaboom 1 ==="
    print(header)
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire import dark_spellbook
    ingredients = "bats, Eyes and glue"
    spell = "doom"
    record_dark_spell = dark_spellbook.dark_spell_record(spell, ingredients)
    print(f"{record_dark_spell}, this wont get printed anyways")
