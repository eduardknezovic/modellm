from modellm import BaseModelAI

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# TODO: load variables from .env

openai_model="gpt-4o-mini"
anthropic_model="claude-haiku-4-5-20251001"

llm = ChatOpenAI(model=openai_model)
claude_llm = ChatAnthropic(model=anthropic_model)

# New approach with BaseModelAI factory - generate_from WILL GLOW in IDE! ✨
class Recipe(BaseModelAI(llm)):
    """
    A cooking recipe.
    """
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

class HealthyRecipe(BaseModelAI(claude_llm)):
    """
    Recipe with minimal calories and maximal nutrients.
    """
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

class DeliciousRecipe(BaseModelAI(claude_llm)):
    """
    The recipe with the most flavor.

    This one is made for the taste buds.
    """
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

class SimplifiedRecipe(BaseModelAI(llm)):
    """
    A simplified version of the recipe with 5 ingredients or less.

    Easy to follow and easy to prepare.
    """
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str
    difficulty_level: str


def test_recipe():
    text = "Fish and chips"
    # generate_from should glow in your IDE! ✨
    recipe: Recipe = Recipe.generate_from(text)
    healthy_simple_recipe: HealthyRecipe = HealthyRecipe.generate_from(recipe)
    print(healthy_simple_recipe)
    delicious_simple_recipe: DeliciousRecipe = DeliciousRecipe.generate_from(healthy_simple_recipe)
    print(delicious_simple_recipe)


if __name__ == "__main__":
    test_recipe()

