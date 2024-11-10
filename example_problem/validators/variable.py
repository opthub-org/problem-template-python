"""Example validator for the variable."""

import json
from typing import cast

from jsonschema import validate

# Schema to validate whether the variable is a scalar(e.g., 1)
VARIABLE_SCALAR_SCHEMA = """{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Variable as a scalar.",
    "type": "number"
}"""

# Schema to validate whether the variable is a vector(e.g., [1, 2, 3])
VARIABLE_VECTOR_SCHEMA = """{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Variable as a vector.",
    "type": "array",
    "items": {"type": "number"}
}"""


def validate_variable(variable: str) -> float | list[float]:
    """Validate the variable.

    Args:
        variable (str): The variable.

    Returns:
    float | list[float]: The validated variable.
    """
    # Validate the variable here.
    # This is an example that validates whether the variable is a scalar or a vector.
    combined = {
        "anyOf": [
            json.loads(VARIABLE_SCALAR_SCHEMA),  # Validate the variable as a scalar
            json.loads(VARIABLE_VECTOR_SCHEMA),  # Validate the variable as a vector
        ],
    }  # Combine the schemas
    json_variable = json.loads(variable)  # Convert the variable to JSON
    validate(json_variable, combined)  # Validate the variable

    return cast(float | list[float], json_variable)
