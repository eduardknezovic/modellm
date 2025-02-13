
from setuptools import setup, find_packages

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read README.md for long description
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="modellm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Eduard Knezovic",
    author_email="knezovic.eduard@gmail.com",
    description="A minimalist LLM modeling library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eduardknezovic/modellm",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
