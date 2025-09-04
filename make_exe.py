# usage: python make_exe.py build

from cx_Freeze import setup, Executable

base = None
# if sys.platform == "win32":
#    base = "Win32GUI"

executables = [
    Executable(
        "src/dorn/cli.py",
        base=base,
        icon="src/dorn/shovel.ico",
        target_name="Dorn.exe",
        copyright="Copyright (C) 2022-2025 South Australia Medical Imaging",
    )
]

setup(
    name="Dorn",
    version="2.0.0b1",
    description="Individualised close contact restrictions for nuclear medicine patients",
    executables=executables,
)
