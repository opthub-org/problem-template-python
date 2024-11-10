"""Example validator for example_env."""

import json
from typing import cast

from jsonschema import validate

# Schema to validate whether the environment variable is a string (e.g., "example").
# Please modify this schema as needed.
EXAMPLE_ENV_SCHEMA = """{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Example environment variable as a string.",
    "type": "string"
}"""


def validate_example_env(example_env: object) -> str:
    """Validate the environment variable (example_env).

    *Please change example_env to the necessary environment variable.

    Args:
        example_env (str): The value of the example environment variable.

    Returns:
    str: The value of the validated example environment variable.
    """
    # Validate the environment variable here.
    # This is an example that validates the environment variable as a string.
    validate(example_env, json.loads(EXAMPLE_ENV_SCHEMA))

    return cast(str, example_env)
