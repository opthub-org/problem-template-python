"""Example tests for the example problem."""

import subprocess

from opthub_runner.evaluator import Evaluator  # type: ignore[import]

EPS = 1e-6  # Epsilon for comparing floating point numbers


def test_example() -> None:
    """Example test for the example problem."""
    # Build the Docker image to test the problem.
    subprocess.run(["make", "build"], check=True)  # Build the image  # noqa: S603, S607
    subprocess.run(["docker", "image", "prune", "-f"], check=True)  # Delete <none> images  # noqa: S603, S607

    # Evaluate the variable using opthub-runner.
    image_name = "opthub/problem-example-problem:latest"  # Docker image name
    environments = {
        "EXAMPLE_ENV": "example_env_test",
    }  # Environment variables for the Docker container
    evaluator = Evaluator(image_name, environments)  # Create an evaluator
    variable = [2.0, 4.0]  # variable to evaluate for testing
    result = evaluator.run(variable)  # Run the evaluator

    # Validate the result.
    expected_result = 6.0
    if abs(result["objective"] - expected_result) > EPS:
        msg = f"Expected: {expected_result}, Got: {result['objective']}"
        raise ValueError(msg)


#
# Write more tests here.
#
