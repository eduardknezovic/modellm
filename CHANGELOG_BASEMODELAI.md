# BaseModelAI Factory Pattern - Changelog

## What Changed

Refactored `BaseModelAI` from a class with `__init_subclass__` to a **factory function** that returns configured base classes.

## New Syntax

### Before (class with kwargs):
```python
class Recipe(BaseModelAI, llm=llm):
    name: str
```

### After (factory function):
```python
class Recipe(BaseModelAI(llm)):
    name: str
```

## Why This is Better

Following Eric S. Raymond's principles from *Art of Unix Programming*:

### ✅ Rule of Least Surprise
- Factory pattern is established in Python (`Generic[T]`, SQLAlchemy's `declarative_base()`)
- Developers recognize this pattern immediately
- No surprise kwargs in class inheritance

### ✅ Rule of Transparency  
- Clear that `BaseModelAI(llm)` returns a configured base class
- Easy to understand: "I'm getting a base class configured with this LLM"
- No hidden magic in `__init_subclass__`

### ✅ Explicit is Better Than Implicit
- You can SEE the LLM being passed to create the base class
- The dependency is obvious in the class definition
- Follows Zen of Python

### ✅ Greppability
- Easy to find: `grep "BaseModelAI(llm)" *.py`
- Clear what's happening when reading code
- No hidden configuration in kwargs

## Features

Both syntaxes still work:

```python
# Method call (IDE autocomplete! ✨)
recipe = Recipe.generate_from("chocolate cake")

# Pipe operator
recipe = "chocolate cake" | Recipe
```

## Benefits

1. **Full IDE Support** - `generate_from()` method glows in your IDE
2. **Type Safety** - Proper type hints for all methods
3. **Conventional** - Follows established Python patterns
4. **Explicit** - Clear configuration and dependencies
5. **Flexible** - Each model can easily use a different LLM

## Files Changed

- `modellm/modellm.py` - Refactored to factory function
- `modellm/__init__.py` - Exports `BaseModelAI`
- `modellm/__init__.pyi` - Type stubs for IDE support
- `examples/recipes_with_basemodelai.py` - Updated examples
- `README.md` - Added BaseModelAI documentation

## Backward Compatibility

The `@add_llm` decorator still works for existing code. `BaseModelAI` is a new alternative approach.

