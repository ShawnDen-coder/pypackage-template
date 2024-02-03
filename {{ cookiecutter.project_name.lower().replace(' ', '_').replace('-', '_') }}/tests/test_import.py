"""Test {{ cookiecutter.project_name.lower().replace(' ', '-') }}."""
from src import {{ cookiecutter.project_name.lower().replace(' ', '-') }}


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(my_python_template.__name__, str)
