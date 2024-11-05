"""Example evaluator for the example problem."""

from typing import TypedDict


class Evaluation(TypedDict):
    """The type of the solution."""

    objective: float


def evaluate(variable: float | list[float], example_env: str) -> Evaluation:
    """Evaluate the solution variable.

    Args:
        variable (float): Solution variable.
        example_env (str): Example environment variable.

    Returns:
    Evaluation: The evaluation result.
    """
    # Evaluate the solution variable here.
    # This is an example function that returns the sum of the variable.
    if isinstance(variable, list) and isinstance(example_env, str):
        objective = sum(variable)
    elif isinstance(variable, float) and isinstance(example_env, str):
        objective = variable
    else:
        msg = "The variable must be a float or a list of floats and the environment variable must be a string."
        raise TypeError(msg)

    return {"objective": objective}
