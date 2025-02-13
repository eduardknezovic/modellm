
# ModeLLM

A minimalist LLM modeling library.

## Installation

```bash
pip install modellm
```

## Usage

```python
from modellm import add_llm

@add_llm(llm)
class Story(BaseModel):
    """
    A story.
    """

    title: str
    content: str
```
