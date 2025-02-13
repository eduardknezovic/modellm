
# ModeLLM

A minimalist LLM modeling library.

## Installation

```bash
pip install modellm
```

## Usage

```python
from modellm import add_llm

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
claude_llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

@add_llm(llm)
class Story(BaseModel):
    """
    A story.
    """

    title: str
    content: str

# LLM model is inherited from the base model (Story)
class ThreeSentenceStory(Story):
    """
    Story written in 3 sentences.
    """
    pass

@add_llm(claude_llm) # We can pick a different llm for a specific model
class StoryForChildren(Story):
    """
    Story for children.
    """
    pass

# story: Story = "A story about a boy who wanted to be a hero" | Story
# story_for_children: StoryForChildren = story | StoryForChildren

text: str = "A story about a boy who wanted to be a hero"
short_children_story: Story = text | StoryForChildren | ThreeSentenceStory

print(short_children_story)
```


