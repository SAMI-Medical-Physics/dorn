# Releasing

This document describes how to create and publish a new release of Dorn.

## Update the source

```text
* pyproject.toml (project)[version]: Update.
(tool.cxfreeze.executables)[copyright]: Update years if required.
* CHANGELOG.md: Enter release date.
* src/dorn/app.py (__version__): Update.
(__release_date__): Enter.
(__copyright_year__): Update years if required.
```

After committing, create and push a tag like so:

    git tag v<version> -m "Release version <version>"
    git push origin v<version>

## Create a cx_Freeze distribution for the new release

In a new venv:

    python -m pip install --upgrade pip
    python -m pip install . .[windows] .[freeze]
    cxfreeze build

## Create a release on GitHub

Before creating the release on GitHub, check that the Dorn repository is enabled on Zenodo so that the new release will automatically appear on Zenodo and be assigned a DOI.

Create the release based on the Git tag created above.

For the release notes (which also appear on the Zenodo record), start with this:

```text
The release on GitHub includes a zip file Dorn_<MAJOR>-<MINOR>-<PATCH>_Win.zip. This zip file contains an executable file Dorn.exe that can be used to run Dorn on Windows 10 and 11 computers without needing to install Python and Dorn's other dependencies.

Changes since version <PREVIOUS-VERSION> (excerpt from CHANGELOG.md):
```

Remember to attach the zip file of the cx_Freeze distribution.

After release, check that [Zenodo](https://doi.org/10.5281/zenodo.7189660) registered it.  If not, submit a support ticket to Zenodo.

Once the new release has a DOI, add it to CITATION.cff.

## Upload to PyPI

In a new venv:

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build twine
    python3 -m build
    python3 -m twine upload dist/*

## Create cx_Freeze distribution for SAMI

Apply patches to use SAMI's organisation information by default:

    git apply <VERSION>.patch

* src/dorn/organisation_logo.png: Replace with the SAMI logo.

In a new venv:

    python -m pip install --upgrade pip
    python -m pip install . .[windows] .[freeze]
    cxfreeze build

Finally, let the team know there is a new version!