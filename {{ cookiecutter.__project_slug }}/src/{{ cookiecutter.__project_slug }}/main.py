"""{{ cookiecutter.__project_slug }} package"""

from {{ cookiecutter.__project_slug }}.cfg import settings


# assert settings.name == "developer"

def run() -> str:
    """
    This function returns the string "Hello, World!".

    Returns:
        str: The string "Hello, World!".
    """
    return "Hello, World!"
