# ModeLLM

[![PyPI version](https://badge.fury.io/py/modellm.svg)](https://badge.fury.io/py/modellm)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

ModeLLM allows you to create AI workflows simply 
by defining and chaining Pydantic models. 

This allows you to build quickly and evolve gracefully, 
since your data model is the single source of truth of the workflow.

```python
# AI workflows get created by chaining the Pydantic models!
output: PydanticModel2 = input_str | PydanticModel1 | PydanticModel2
print(output)
```

## Features

- **Pydantic-First**: Use Python's type system to define your LLM outputs
- **Chain Transformations**: Pipe output through multiple models seamlessly
- **Multiple LLM Support**: Works with OpenAI, Anthropic, and other LangChain providers
- **Prompt Engineering in Docstrings**: Define your prompts naturally in Python docstrings

## Installation

```bash
pip install modellm
```

You will need to add your OPENAI_API_KEY or ANTHROPIC_API_KEY to your environment variables.

## Quick Start

Here's a minimal example to get you started:

```python
from pydantic import BaseModel
from modellm import add_llm
from langchain_openai import ChatOpenAI

# Set up your LLM
llm = ChatOpenAI(model="gpt-4o-mini")

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

class HealthyRecipe(Recipe): # LLM is inherited from the Recipe
    """Recipe with minimal calories and maximal nutrients.""" 
    pass

@add_llm(claude_llm) # We're using a different LLM here
class SimplifiedRecipe(HealthyRecipe):
    """Simplified recipe with more basic, everyday ingredients"""
    pass

# Chain transformations
healthy_simple_recipe: Recipe = recipe | HealthyRecipe | SimplifiedRecipe
print(healthy_simple_recipe)
```
## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use ModeLLM in your research, please cite:

```bibtex
@software{modellm_2025,
  author = {[Eduard Knezovic]},
  title = {ModeLLM: A Minimalist LLM Modeling Library},
  year = {2025},
  publisher = {eduardknezovic},
  url = {https://github.com/eduardknezovic/modellm}
}
```

## Acknowledgments

- Built on top of Pydantic and LangChain
- Inspired by the functional programming paradigm
- Thanks to the open source AI community

---

*"Make it as simple as possible, but not simpler." - Albert Einstein*
