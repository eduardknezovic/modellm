"""Type stubs for modellm package."""
from typing import Protocol, Union, TypeVar, Type
from pydantic import BaseModel
from langchain_core.language_models.chat_models import BaseChatModel

_T = TypeVar('_T', bound=BaseModel)

class _BaseModelAI(BaseModel):
    """Base class returned by BaseModelAI factory with LLM capabilities."""
    
    @classmethod
    def generate_from(cls: Type[_T], input_data: Union[str, BaseModel]) -> _T:
        """Generate structured output from input using LLM."""
        ...

def BaseModelAI(llm: BaseChatModel) -> Type[_BaseModelAI]:
    """
    Factory function that returns a BaseModel with LLM capabilities.
    
    Args:
        llm: The language model to use
        
    Returns:
        A base class with generate_from() method
    """
    ...

class SupportsGenerate(Protocol[_T]):
    """Protocol for models decorated with @add_llm."""
    
    @classmethod
    def generate_from(cls: Type[_T], input_data: Union[str, BaseModel]) -> _T:
        """Generate structured output from input using LLM."""
        ...

def add_llm(llm: BaseChatModel) -> callable[[Type[_T]], Type[_T]]:
    """Decorator that adds LLM processing capabilities."""
    ...

__all__ = ['add_llm', 'BaseModelAI', 'SupportsGenerate']

