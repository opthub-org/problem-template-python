"""Tests for the evaluator."""

from example_problem.evaluator.main import evaluate

EPS = 1e-6  # Epsilon for comparing floating point numbers


def test_evaluate_scalar() -> None:
    """Example test for the evaluate function using a scalar as a variable."""
    variable = 1.0
    env = "example_env"
    result = evaluate(variable, env)

    expected_objective = 1.0

    if abs(result["objective"] - expected_objective) > EPS:
        msg = f"Expected objective: {expected_objective}, Got: {result['objective']}"
        raise ValueError(msg)


def test_evaluate_vector() -> None:
    """Example test for the evaluate function using a vector as a variable."""
    variable = [1.0, 2.0]
    env = "example_env"
    result = evaluate(variable, env)

    expected_objective = 3.0

    if abs(result["objective"] - expected_objective) > EPS:
        msg = f"Expected objective: {expected_objective}, Got: {result['objective']}"
        raise ValueError(msg)


#
# Write more tests here.
#
