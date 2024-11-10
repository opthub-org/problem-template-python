"""Example problem."""

import json
import logging
import sys

import click

from example_problem.evaluator.main import evaluate
from example_problem.validators.example_env import validate_example_env
from example_problem.validators.variable import validate_variable

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)  # Logger


@click.command(help="Example problem.")
@click.option(
    "-e",
    "--example-env",
    type=str,
    default="example_env",
    envvar="EXAMPLE_ENV",
    help="Example environment variable.",
)
def main(example_env: str) -> None:
    """Example main function for evaluating given variable."""
    try:
        validated_example_env = validate_example_env(example_env)  # Validate the environment variable
        msg = f"validated_example_env: {validated_example_env}"
        LOGGER.info(msg)

        variable = input()  # Read the variable from the standard input

        validated_variable = validate_variable(variable)  # Validate the variable
        msg = f"validated_variable: {validated_variable}"
        LOGGER.info(msg)

        result = evaluate(validated_variable, validated_example_env)  # Evaluate the variable
        msg = f"result: {result}"
        LOGGER.info(msg)

        sys.stdout.write(json.dumps(result))  # Write the result to the standard output

    except Exception as e:
        error_result = {"objective": None, "error": str(e)}
        sys.stdout.write(
            json.dumps(error_result),
        )  # Write the error result to the standard output
        msg = f"error result: {error_result}"
        LOGGER.info(msg)


if __name__ == "__main__":
    main()
