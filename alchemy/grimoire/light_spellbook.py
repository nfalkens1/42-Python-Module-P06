def light_spell_allowed_ingredients() -> list[str]:
    allowed = ["earth", "air", "fire", "water"]
    return allowed


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    recorded_check: list = ["Spell recorded", "Spell discarded"]
    if validation.split(" - ")[-1] == "VALID":
        recorded = recorded_check[0]
    else:
        recorded = recorded_check[1]
    format_out = f"{recorded}: {spell_name} ({validation})"
    return (format_out)
