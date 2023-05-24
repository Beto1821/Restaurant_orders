from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    # Teste de instanciação e atributos do prato
    lasanha = Dish("Lasanha", 15.99)
    assert lasanha.name == "Lasanha"
    assert lasanha.__repr__() == "Dish('Lasanha', R$15.99)"

    # Teste de igualdade e hash de pratos iguais
    lasanha2 = Dish("Lasanha", 15.99)
    assert lasanha == lasanha2
    assert lasanha.__hash__() == lasanha2.__hash__()

    # Teste de desigualdade e hash de pratos diferentes
    sushi = Dish("Sushi", 12.99)
    assert lasanha != sushi
    assert lasanha.__hash__() != sushi.__hash__()

    # Teste de exceções ao criar prato com valores inválidos
    with pytest.raises(TypeError):
        Dish("name", "price")
    with pytest.raises(ValueError):
        Dish("name", 0)

    # Teste de adição de ingredientes à receita do prato
    lasanha.add_ingredient_dependency(Ingredient("Massa de Lasanha"), 8)
    assert lasanha.recipe.get(Ingredient("Massa de Lasanha")) == 8
    assert lasanha.get_restrictions() == set()

    # Teste de obtenção dos ingredientes da receita e restrições do prato
    lasanha.add_ingredient_dependency(Ingredient("Queijo"), 2)
    assert lasanha.get_ingredients() == {
        Ingredient("Massa de Lasanha"),
        Ingredient("Queijo"),
    }
    assert lasanha.get_restrictions() == set()
