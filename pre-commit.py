import subprocess
import sys
import os


def pip_install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pre-commit"])


def install_hooks():
    os.system("pre-commit install")


if __name__ == "__main__":
    pip_install()
    install_hooks()
