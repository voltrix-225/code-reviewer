from setuptools import setup, find_packages

'''Setup file for global module'''

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