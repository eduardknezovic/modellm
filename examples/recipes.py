from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from modellm import add_llm

# TODO: load variables from .env

openai_model="gpt-4o-mini"
anthropic_model="claude-haiku-4-5-20251001"

llm = ChatOpenAI(model=openai_model)
claude_llm = ChatAnthropic(model=anthropic_model)

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
    recipe = Recipe.generate_from(text)
    healthy_simple_recipe = HealthyRecipe.generate_from(recipe)
    print(healthy_simple_recipe)
    delicious_simple_recipe = DeliciousRecipe.generate_from(healthy_simple_recipe)
    print(delicious_simple_recipe)


if __name__ == "__main__":
    test_recipe()
