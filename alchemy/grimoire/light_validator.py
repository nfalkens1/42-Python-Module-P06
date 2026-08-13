from alchemy.grimoire import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()
    if any(word in ingredients.lower() for word in allowed):
        validity = "VALID"
    else:
        validity = "INVALID"
    format_out = f"{ingredients} - {validity}"
    return format_out
