"""Tests for the variable validator."""

import pytest
from jsonschema import ValidationError

from example_problem.validators.variable import validate_variable


def test_valid_scalar() -> None:
    """Example test for the validate_variable function using a scalar."""
    variable = "1.0"  # A scalar (valid input)
    validate_variable(variable)  # No error should be raised


def test_valid_vector() -> None:
    """Example test for the validate_variable function using a vector."""
    variable = "[1.0, 2.0]"  # A vector (valid input)
    validate_variable(variable)  # No error should be raised


def test_invalid_type() -> None:
    """Example test for the validate_variable function with invalid input."""
    variable = '"a"'  # Not a scalar or a vector (invalid input)
    with pytest.raises(ValidationError):
        validate_variable(variable)  # A ValidationError should be raised


#
# Write more tests here.
#
