"""Test {{ cookiecutter.project_slug }}."""
from src import {{ cookiecutter.project_slug }} # noqa: F821


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance({{ cookiecutter.project_slug }}.__name__, str) # noqa: F821
