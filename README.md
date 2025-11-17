
# ModeLLM

[![PyPI version](https://badge.fury.io/py/modellm.svg)](https://badge.fury.io/py/modellm)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

_"Controlling complexity is the essence of computer programming."_ 

## Overview

ModeLLM makes your AI workflows dead simple to build and maintain.

Your Pydantic data models become AI-powered with one line of code:

```python
class Recipe(BaseModelAI(llm)):
    name: str
    ingredients: list[str]

recipe = Recipe.generate_from("chocolate chip cookies")
```

Chain transformations with clean, explicit syntax:

```python
result = Recipe.generate_from(input_text)
improved = ImprovedRecipe.generate_from(result)

# Or use the pipe operator
result = input_text | Recipe | ImprovedRecipe
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

ModeLLM requires Python 3.10+. All required dependencies (pydantic, langchain) will be installed automatically.

Currently, ModeLLM supports the following LangChain LLM providers:
- ChatOpenAI
- ChatAnthropic

To use them, you will need to add your 
OPENAI_API_KEY and/or ANTHROPIC_API_KEY to your environment variables.

## Quick Start

Here's a minimal example to get you started:

```python
from modellm import BaseModelAI
from langchain_openai import ChatOpenAI

# Set up your LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Define your model with AI capabilities
class Recipe(BaseModelAI(llm)):
    """A cooking recipe."""
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

# Generate structured output - THREE ways:

# 1. Explicit method (recommended - full IDE autocomplete!)
recipe: Recipe = Recipe.generate_from("Fish and chips")

# 2. Pipe operator (functional style)
recipe = "Fish and chips" | Recipe

# 3. Direct call (coming soon!)
# recipe = Recipe("Fish and chips")

print(recipe)
```

**Why BaseModelAI?**
- ✨ **Full IDE support** - `generate_from()` method autocompletes perfectly
- 🎯 **Conventional syntax** - Follows established Python patterns like `Generic[T]`
- 📖 **Explicit** - Clear which LLM is used for each model
- 🔍 **Easy to grep** - Find configurations easily: `grep "BaseModelAI("`
- 🚀 **Type safe** - Full type hints for better code quality

## Alternative: Decorator Style

If you prefer decorators, you can also use the `@add_llm` decorator:

```python
from pydantic import BaseModel
from modellm import add_llm

@add_llm(llm)
class Recipe(BaseModel):
    """A cooking recipe."""
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

# Use with pipe operator
recipe = "Fish and chips" | Recipe
print(recipe)
```

The decorator style works great for the pipe operator pattern!

## Detailed Usage

ModeLLM supports complex transformation chains and multiple LLM providers:

```python
from modellm import BaseModelAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# Use different LLMs for different models
gpt4 = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
claude = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0.2)

class Recipe(BaseModelAI(gpt4)):
    """A cooking recipe."""
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str

class HealthyRecipe(BaseModelAI(claude)):
    """Recipe with minimal calories and maximal nutrients."""
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str
    nutritional_info: str

class SimplifiedRecipe(BaseModelAI(gpt4)):
    """Simplified recipe with basic, everyday ingredients."""
    name: str
    ingredients: list[str]
    instructions: list[str]
    cooking_time: str
    difficulty_level: str

# Chain transformations - three equivalent ways:

# Method chaining (explicit, recommended)
recipe = Recipe.generate_from("Fish and chips")
healthy = HealthyRecipe.generate_from(recipe)
simple = SimplifiedRecipe.generate_from(healthy)

# Pipe operator (functional)
simple = "Fish and chips" | Recipe | HealthyRecipe | SimplifiedRecipe

# Mixed style
recipe = Recipe.generate_from("Fish and chips")
simple = recipe | HealthyRecipe | SimplifiedRecipe

print(simple)
```

## Contributing

Contributions are welcome! Feel free to submit a pull request!

For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Built on top of [Pydantic](https://github.com/pydantic/pydantic) and [LangChain](https://github.com/langchain-ai/langchain)
- Inspired by the Eric S. Raymond's [Art of Unix Programming](http://www.catb.org/~esr/writings/taoup/html/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

