from setuptools import setup, find_packages

'''DOCS to be added LATER'''

setup(
    name = "code-reviewer",
    version='1.0',
    packages = find_packages(),
    install_requires = ["pylint", ],
    description = "Code analyzer/reviewer",
    entry_points = {
        "console_scripts" : ["analyze = src.main:main"],
    },
)