from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    if any(word in ingredients.lower() for word in allowed):
        validity = "VALID"
    else:
        validity = "INVALID"
    format_out = f"{ingredients} - {validity}"
    return format_out
