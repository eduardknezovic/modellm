
from .modellm import add_llm, BaseModelAI
from typing import Protocol, Union, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class SupportsGenerate(Protocol[T]):
    """
    Protocol for models decorated with @add_llm.
    Use this for type hints when you need IDE autocomplete.
    
    Example:
        @add_llm(llm)
        class Recipe(BaseModel):
            name: str
        
        # For full IDE support:
        recipe: Recipe = Recipe.generate_from("cookies")  # IDE will autocomplete!
    """
    
    @classmethod
    def generate_from(cls, input_data: Union[str, BaseModel]) -> T:
        """Generate structured output from input using LLM."""
        ...

__all__ = ['add_llm', 'BaseModelAI', 'SupportsGenerate']
