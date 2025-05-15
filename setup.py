from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyutilkitsarvs",
    version="0.1.1",
    author="Your Name",
    author_email="sarveshkannan30@gmail.com",
    description="A multi-purpose Python utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pyutilkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
) 