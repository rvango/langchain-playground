from langchain.tools import StructuredTool


def substractor(a: float, b: float) -> float:
    """Subtract the provided floats."""
    return a - b


substractor = StructuredTool.from_function(substractor)
