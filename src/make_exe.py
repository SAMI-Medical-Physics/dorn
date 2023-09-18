# usage: python make_exe.py build

from cx_Freeze import setup, Executable

# import sys

base = None
# if sys.platform == "win32":
#    base = "Win32GUI"

executables = [
    Executable(
        "dorn_cli.py",
        base=base,
        icon="icofile.ico",
        target_name="Dorn.exe",
        copyright="Copyright (C) 2022, 2023 South Australia Medical Imaging",
    )
]

include_files = ["gui_background.png", "report_logo.png", "icofile.ico"]

packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "docx",
    "xmltodict",
    "glowgreen",
]

options = {
    "build_exe": {
        "packages": packages,
        "include_files": include_files,
        "excludes": [
            "matplotlib.tests",
            "numpy.random._examples",
        ],  # necessary for building on work PC
    },
}

setup(
    name="Dorn",
    options=options,
    version="1.10.0",
    description="Individual close contact restrictions for nuclear medicine patients",
    executables=executables,
)
