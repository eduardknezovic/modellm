from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from modellm import add_llm

# TODO: load variables from .env


llm = ChatOpenAI(model="gpt-4o-mini")
claude_llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

@add_llm(llm)
class Recipe(BaseModel):
    """
    A cooking recipe.
    """
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

@add_llm(claude_llm)
class HealthyRecipe(Recipe):
    """
    Recipe with minimal calories and maximal nutrients.
    """
    pass

@add_llm(claude_llm)
class DeliciousRecipe(Recipe):
    """
    The recipe with the most flavor.

    This one is made for the taste buds.
    """
    pass

@add_llm(llm)
class SimplifiedRecipe(Recipe):
    """
    A simplified version of the recipe with 5 ingredients or less.

    Easy to follow and easy to prepare.
    """
    difficulty_level: str


def test_recipe():
    text = "Fish and chips"
    recipe = text | Recipe
    healthy_simple_recipe = recipe | HealthyRecipe | SimplifiedRecipe
    print(healthy_simple_recipe)
    delicious_simple_recipe = recipe | DeliciousRecipe | SimplifiedRecipe
    print(delicious_simple_recipe)


if __name__ == "__main__":
    test_recipe()
