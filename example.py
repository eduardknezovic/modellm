from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from modellm import add_llm

# TODO: load variables from .env


llm = ChatOpenAI(model="gpt-4o-mini")
claude_llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

@add_llm(llm)
class Story(BaseModel):
    """
    A story. 
    """

    title: str
    content: str

@add_llm(claude_llm)
class StoryForChildren(Story):
    """
    A short 3 sentence story for children.
    """
    pass

@add_llm(llm)
class ThreeSentenceStory(Story):
    """
    A story with 3 sentences.
    """
    pass


def execute_workflow(text: str):
    story = text | Story | StoryForChildren | ThreeSentenceStory
    return story

def test_story():
    text = "The story of the boy who wanted to be a hero"
    story = execute_workflow(text)
    print(story)

if __name__ == "__main__":
    test_story()
