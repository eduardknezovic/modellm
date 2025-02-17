
from typing import List
from pathlib import Path

from pydantic import BaseModel
from langchain_openai import ChatOpenAI

from modellm import add_llm

# Initialize the LLM (Language Model) we'll use for generating content
llm = ChatOpenAI(model="gpt-4o-mini")

# The @add_llm decorator connects the model to our LLM instance
# This enables automatic content generation for the model's fields
@add_llm(llm) 
class Story(BaseModel):
    title: str
    content: str
    genre: str 

# Please note that the docstrings will be used by LLM to 
# understand how to adapt the content
# This is a powerful feature, 
# keeping the code easy to understand (For both humans and LLMs)

@add_llm(llm) 
class StoryForBabies(Story):
    """
    A story that is specifically tailored to be a baby's story.

    Appropriate for infants and toddlers aged 0-2 years old.
    Features:
    - Simple, repetitive language
    - Basic concepts
    - Short sentences
    - Sensory-rich descriptions
    """
    # The class inherits all fields from Story
    pass

@add_llm(llm)
class StoryForTeenagers(Story):
    """
    A story that is specifically tailored for teenage readers.

    Appropriate for young adults aged 13-19 years old.
    Features:
    - Complex character development
    - Engaging plot with relatable conflicts
    - Contemporary themes and social issues
    - Age-appropriate emotional depth
    - Exploration of identity and personal growth
    - Modern dialogue and realistic relationships
    """
    pass # Same as with StoryForBabies

@add_llm(llm)
class HtmlModel(BaseModel):
    """
    An HTML representation with beautiful CSS styling.
    """
    html: str

def main():
    story_idea = "A story about farmer's struggle and perseverance"
    html_filepath = Path("story.html")

    # That's it. Only one line of code
    html_story = story_idea | Story | StoryForBabies | HtmlModel

    # Alternative pipeline for teenage audience
    # The | operator makes it easy to swap components in the pipeline
    # html_story = story_idea | Story | StoryForTeenagers | HtmlModel

    html_filepath.write_text(html_story.html)
    print(f"Story saved in HTML format to: {html_filepath.resolve()}")


if __name__ == "__main__":
    main()
