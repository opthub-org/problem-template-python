"""Tests for the example_env validator."""

import pytest
from jsonschema import ValidationError

from example_problem.validators.example_env import validate_example_env


def test_valid_type() -> None:
    """Example test for the validate_example_env function with valid input."""
    example_env = "example"  # A string (valid input)
    validate_example_env(example_env)  # No error should be raised


def test_invalid_type() -> None:
    """Example test for the validate_example_env function with invalid input."""
    example_env = 1  # Not a string (invalid input)
    with pytest.raises(ValidationError):
        validate_example_env(example_env)  # A ValidationError should be raised


#
# Write more tests here.
#
