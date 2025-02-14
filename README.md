# ModeLLM

A minimalist LLM modeling library.

## Installation

```bash
pip install modellm
```

## Quick start

You will need to add your OPENAI_API_KEY or ANTHROPIC_API_KEY to your environment variables.


```python
from pydantic import BaseModel
from modellm import add_llm
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# You will need to add your OPENAI_API_KEY or ANTHROPIC_API_KEY to your environment variables, or simply uncomment and set them here.
# import os
# os.environ["OPENAI_API_KEY"] = "sk-..."
# os.environ["ANTHROPIC_API_KEY"] = "sk-ant-api03-..."

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

# OpenAI LLM model is inherited from the base model (Recipe)
@add_llm(claude_llm)
class HealthyRecipe(Recipe):
    """
    Recipe with minimal calories and maximal nutrients.
    """
    pass

@add_llm(claude_llm) # We can pick a different llm for a specific model
class DeliciousRecipe(Recipe):
    """
    The recipe with the most flavor.
    """
    pass

@add_llm(llm)
class SimplifiedRecipe(Recipe):
    """
    A simplified version of the recipe with 5 ingredients or less.
    """
    difficulty_level: str

# Basic recipe transformation
text = "Fish and chips"
recipe = text | Recipe

# Chain multiple transformations
# result = input_str_or_base_model | pydantic_model1 | pydantic_model2
healthy_simple_recipe = recipe | HealthyRecipe | SimplifiedRecipe
delicious_simple_recipe = recipe | DeliciousRecipe | SimplifiedRecipe

print(healthy_simple_recipe)
print(delicious_simple_recipe)
```


