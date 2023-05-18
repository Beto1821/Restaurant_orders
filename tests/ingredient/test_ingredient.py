from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Criação de instâncias de Ingredient
    ingredient = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo gorgonzola")

    # Verificações do atributo name
    assert ingredient.name == "queijo mussarela"

    # Verificação da representação em string
    assert ingredient.__repr__() == "Ingredient('queijo mussarela')"

    # Verificação de igualdade do próprio objeto
    assert ingredient == ingredient

    # Verificação de desigualdade entre objetos diferentes
    assert ingredient != ingredient2

    # Verificação do valor de hash do objeto ingredient
    assert hash(ingredient) == hash("queijo mussarela")

    # Verificação de valores de hash diferentes para objetos diferentes
    assert hash(ingredient) != hash(ingredient2)

    # Verificação das restrições do objeto ingredient
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
