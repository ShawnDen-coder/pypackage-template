import os

# project_name pre action
project_name = '{{cookiecutter.project_name}}'
project_slug = project_name.lower().replace(' ', '_').replace('-', '_')
os.environ['COOKIECUTTER_PROJECT_SLUG'] = project_slug
