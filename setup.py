import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PRO_API",
    version="0.0.1",
    author="Walross",
    description="An advanced stub file for writing PRO scripts, with some debugging features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Inspirateur/PRO_API",
    packages=['PRO'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)