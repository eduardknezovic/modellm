
# ModeLLM

[![PyPI version](https://badge.fury.io/py/modellm.svg)](https://badge.fury.io/py/modellm)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

_"Controlling complexity is the essence of computer programming."_ 

## Overview

ModeLLM is here to make your AI workflows dead simple to build and maintain.

Your Pydantic data models become the single source of truth.

Once the data models are well defined, you can create the workflow in a single line of code:

```python
output: YourPydanticModel2 = input_data | YourPydanticModel1 | YourPydanticModel2
```

## More Benefits

- **Prompts as Documentation**: Keep prompts and code together by writing prompts in Pydantic docstrings, making them easy to understand for both humans and LLMs 
- **Self-Documenting Workflows**: Understand the entire pipeline at a glance through clear model definitions and model chains
- **Production-Ready Design**: Built on battle-tested libraries like Pydantic and LangChain
- **Rapid Prototyping and Maintenance**: Iterate quickly by swapping models and transformations with minimal code changes. 

## Installation

```bash
pip install modellm
```

ModeLLM requires Python 3.9+. All required dependencies (pydantic, langchain) will be installed automatically.

Currently, ModeLLM supports the following LangChain LLM providers:
- ChatOpenAI
- ChatAnthropic

To use them, you will need to add your 
OPENAI_API_KEY and/or ANTHROPIC_API_KEY to your environment variables.

## Quick Start

Here's a minimal example to get you started:

```python
from pydantic import BaseModel
from modellm import add_llm
from langchain_openai import ChatOpenAI

# Set up your LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

@add_llm(llm)
class Recipe(BaseModel):
    """
    A cooking recipe.
    """
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

# Generate a recipe
text = "Fish and chips"
recipe = text | Recipe
print(recipe)
```

## Detailed Usage

ModeLLM supports complex transformation chains and multiple LLM providers:

```python
# Continuing from the previous example

claude_llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0.2)

@add_llm(claude_llm) # Add a different LLM to this model
class SimplifiedRecipe(Recipe):
    """Simplified recipe with more basic, everyday ingredients"""
    pass

class HealthyRecipe(Recipe): # OpenAI LLM is inherited from the Recipe
    """Recipe with minimal calories and maximal nutrients.""" 
    pass

# Chain transformations
healthy_simple_recipe: Recipe = recipe | HealthyRecipe | SimplifiedRecipe
print(healthy_simple_recipe)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 

For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Built on top of Pydantic and LangChain
- Inspired by the Eric S. Raymond's [Art of Unix Programming](http://www.catb.org/~esr/writings/taoup/html/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

