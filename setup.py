import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intelup_python",
    version="0.0.1",
    author="Intelup",
    author_email="contato@intelup.com.br",
    description="A package that sends data to Intelup platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Intelup/intelup-python",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ),
)
