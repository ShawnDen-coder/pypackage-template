import os
import shutil
import subprocess


def excludeFiles():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            if name == "__pycache__":
                shutil.rmtree(os.path.join(root, name))


def init_branchs():
    repo_url = '{{ cookiecutter.__project_remote_repo }}'
    cmd = ["task", "init_repo", repo_url]
    subprocess.check_call(cmd)


excludeFiles()
init_branchs()
