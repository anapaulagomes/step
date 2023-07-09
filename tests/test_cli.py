import pytest

from step.cli import convert_to_python_method_name, InvalidMethodName


@pytest.mark.parametrize(
    "phrase,expected_method",
    [
        ("Setup new customer (environment)", "setup_new_customer_environment"),
        ("The rationale behind this", "the_rationale_behind_this"),
        ("Development", "development"),
    ],
)
def test_create_valid_python_method_name_from_str(phrase, expected_method):
    method_name = convert_to_python_method_name(phrase)
    assert method_name == expected_method


@pytest.mark.parametrize("phrase", ["", None, "#%&^!@%55253"])
def test_raise_exception_when_impossible_to_create_method_name(phrase):
    with pytest.raises(InvalidMethodName):
        convert_to_python_method_name(phrase)
