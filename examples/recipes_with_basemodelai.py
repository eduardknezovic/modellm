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
    
    # Simple usage - generate_from should glow in your IDE! ✨
    recipe: Recipe = Recipe.generate_from(text)
    print("=== Basic Recipe ===")
    print(recipe)
    print()
    
    recipe_with_system: Recipe = Recipe.generate_from(
        "Chocolate cake",
    )
    print("=== Recipe with string input only ===")
    print(recipe_with_system)
    print()
    
    # With extra guidance - add additional instructions to the input
    recipe_with_guidance: Recipe = Recipe.generate_from(
        "Pasta carbonara",
        extra_guidance="Make it authentic Italian style. Use only 5 ingredients."
    )
    print("=== Recipe with Extra Guidance ===")
    print(recipe_with_guidance)
    print()
    
    # With both prompts - full control
    recipe_full_control: Recipe = Recipe.generate_from(
        "Vegetable stir fry",
        system_prompt="You are a health-conscious chef specializing in quick meals.",
        extra_guidance="Keep cooking time under 15 minutes. Use common pantry items."
    )
    print("=== Recipe with Both Prompts ===")
    print(recipe_full_control)
    print()
    
    # Chaining models with extra guidance
    healthy_simple_recipe: HealthyRecipe = HealthyRecipe.generate_from(
        recipe,
        extra_guidance="Reduce calories by at least 30%. Maintain great taste."
    )
    print("=== Healthy Recipe (from basic recipe) ===")
    print(healthy_simple_recipe)
    print()
    
    delicious_simple_recipe: DeliciousRecipe = DeliciousRecipe.generate_from(
        healthy_simple_recipe,
        system_prompt="You are a Michelin-star chef focused on maximum flavor.",
        extra_guidance="Enhance the taste while keeping it healthy."
    )
    print("=== Delicious Recipe (from healthy recipe) ===")
    print(delicious_simple_recipe)


if __name__ == "__main__":
    test_recipe()

