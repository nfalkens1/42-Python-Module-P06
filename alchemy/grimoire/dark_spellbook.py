from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    return allowed


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    recorded_check: list = ["Spell recorded", "Spell discarded"]
    if validation.split(" - ")[-1] == "VALID":
        recorded = recorded_check[0]
    else:
        recorded = recorded_check[1]
    format_out = f"{recorded}: {spell_name} ({validation})"
    return (format_out)
