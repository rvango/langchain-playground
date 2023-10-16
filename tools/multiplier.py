from langchain.tools import StructuredTool


def multiplier(a: float, b: float) -> float:
    """Multiply the provided floats."""
    return a * b


multiplier = StructuredTool.from_function(multiplier)
