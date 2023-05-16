from src.models.ingredient import Ingredient, Restriction


def test_ingredient():

    ingredient = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo gorgonzola")

    assert ingredient.name == "queijo mussarela"

    assert ingredient.__repr__() == "Ingredient('queijo mussarela')"

    assert ingredient == ingredient

    assert ingredient != ingredient2

    assert hash(ingredient) == hash("queijo mussarela")

    assert hash(ingredient) != hash(ingredient2)

    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
