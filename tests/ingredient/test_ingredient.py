from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Req 1
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # Req 2
    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    # Req 3
    ingredient1 = Ingredient("queijo mussarela")
    assert ingredient1 == ingredient1

    # Req 4
    ingredient2 = Ingredient("queijo gorgonzola")
    assert ingredient1 != ingredient2

    # Req 5
    assert hash(ingredient1) == hash(ingredient1)

    # Req 6
    assert hash(ingredient1) != hash(ingredient2)

    # Req 7
    assert ingredient.name == "queijo mussarela"

    # Req 8
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
