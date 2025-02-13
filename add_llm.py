
"""
Modellm 
------------------
A framework for declarative creation of LLM-powered agents with 
structured inputs and outputs using Pydantic data models and the pipe operator.
"""

from pydantic import BaseModel
from typing import List, Union, Callable, ClassVar, TypeVar, Generic, Type
from langchain_core.language_models.chat_models import BaseChatModel

InputT = TypeVar('InputT', bound=Union[str, BaseModel])
OutputT = TypeVar('OutputT', bound=BaseModel)

def _get_agent_function(
    input_model: Union[Type[BaseModel], Type[str]],
    output_model: Type[BaseModel],
    llm: BaseChatModel,
) -> Callable[[InputT], OutputT]:
    """
    Creates an agent function that processes input through an LLM and returns structured output.

    Args:
        input_model: The expected input type (either str or a Pydantic model)
        output_model: The Pydantic model class for structured output
        llm: The language model to use for processing

    Returns:
        A callable that takes input_model and returns output_model
    """
    llm = llm.with_structured_output(output_model)
    
    def run_llm(input_data: InputT) -> OutputT:
        """
        Process the input through the LLM and return structured output.

        Args:
            input_data: Input matching input_model type

        Returns:
            Structured output matching output_model

        Raises:
            ValueError: If input_data doesn't match the expected input_model type
        """
        if input_model == str:
            if not isinstance(input_data, str):
                raise ValueError("Input must be a string")
        elif not isinstance(input_data, input_model):
            raise ValueError(f"Input must be an instance of {input_model}")
            
        if isinstance(input_data, BaseModel):
            input_data = input_data.model_dump_json()
            
        return llm.invoke(input_data)
        
    return run_llm

def add_llm(llm: BaseChatModel) -> Callable[[Type[BaseModel]], Type[BaseModel]]:
    """
    Decorator that adds LLM processing capabilities to a Pydantic model using the pipe operator.

    Args:
        llm: The language model to use for processing

    Returns:
        A decorator function that enhances a Pydantic model with LLM processing
    """
    def decorator(cls: Type[BaseModel]) -> Type[BaseModel]:
        class AushaMeta(type(cls)):
            """Metaclass that implements the pipe operator for LLM processing."""
            
            def __ror__(cls, other: InputT) -> OutputT:
                """Implements the right pipe operator (input | Model)."""
                agent_function = _get_agent_function(
                    str if isinstance(other, str) else type(other),
                    cls, 
                    llm
                )
                return agent_function(other)

        # Create new class with our metaclass
        class WrappedClass(cls, metaclass=AushaMeta):
            """A wrapper class that adds LLM processing capabilities to the original model."""
            pass

        # Preserve the original class metadata
        WrappedClass.__name__ = cls.__name__
        WrappedClass.__qualname__ = cls.__qualname__
        WrappedClass.__doc__ = cls.__doc__
        
        return WrappedClass
    return decorator

