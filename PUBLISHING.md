# Publishing PyUtilKit to PyPI

This document outlines the steps needed to build and publish the PyUtilKit package to PyPI (Python Package Index).

## Prerequisites

1. Make sure you have the latest versions of packaging tools:
   ```bash
   pip install --upgrade pip setuptools wheel twine build
   ```

2. Create accounts on both [PyPI](https://pypi.org/account/register/) and [TestPyPI](https://test.pypi.org/account/register/) (for testing).

## Building the Package

1. Make sure you're in the root directory of the project (where `setup.py` is located).

2. Update the version number in `pyutilkit/__init__.py`:
   ```python
   __version__ = "x.y.z"  # Increment according to semantic versioning
   ```

3. Build the package:
   ```bash
   python -m build
   ```
   
   This will create both a source distribution and a wheel in the `dist/` directory.

## Testing on TestPyPI (Recommended)

1. Upload to TestPyPI first:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```
   
   You'll be prompted for your TestPyPI username and password.

2. Test the installation:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pyutilkit
   ```
   
   The extra index URL is needed because TestPyPI might not have all the dependencies.

3. Verify that the package works correctly:
   ```bash
   python -c "import pyutilkit; print(pyutilkit.__version__)"
   ```

## Publishing to PyPI

Once you've confirmed everything works with TestPyPI:

1. Upload to the real PyPI:
   ```bash
   python -m twine upload dist/*
   ```
   
   You'll be prompted for your PyPI username and password.

2. Test the installation from the real PyPI:
   ```bash
   pip install pyutilkit
   ```

## Troubleshooting

- If you need to make changes after testing, don't forget to update the version number before rebuilding.
- Clean the `dist/` directory before rebuilding: `rm -rf dist/` or `del dist\*` on Windows.
- Make sure your README.md renders correctly on PyPI by checking it on TestPyPI first.

## Post-Publication

1. Tag the release in Git:
   ```bash
   git tag -a vX.Y.Z -m "Version X.Y.Z"
   git push origin vX.Y.Z
   ```

2. Create a GitHub release with release notes.

3. Update the documentation as needed. 