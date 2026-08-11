from .elements import create_air, create_earth
import elements


def healing_potion() -> str:
    air = create_air()
    earth = create_earth()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire = elements.create_fire()
    water = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"


def avatar_potion() -> str:
    water = elements.create_water()
    earth = create_earth()
    fire = elements.create_fire()
    air = create_air()
    elements_consumed = [water, earth, fire, air]
    for element in elements_consumed:
        print(element)
    return "You are now the Avatar!"
