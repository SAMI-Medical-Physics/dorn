[![DOI](https://zenodo.org/badge/549013816.svg)](https://zenodo.org/badge/latestdoi/549013816)

# Dorn

Dorn is a Python GUI program for generating individual close contact restrictions for radionuclide therapy patients.
Example use cases are I-131 for thyroid cancer and Lu-177-dotatate for neuroendocrine tumours.

## Requires

Python >= 3.9

## Dependencies

Python packages:
- `numpy`
- `scipy`
- `matplotlib`
- `pandas`
- `glowgreen`
- `xmltodict`
- `python-docx`

E.g., works with:
- `numpy` == 1.23.3
- `scipy` == 1.9.2 (but <=1.9.1 for `cx_Freeze` .exe to work)
- `matplotlib` == 3.6.1
- `pandas` == 1.5.0
- `glowgreen` == 0.0.4
- `xmltodict` == 0.13.0
- `python-docx` == 0.8.11

## glowgreen package

Dorn uses the Python package `glowgreen` for calculating radiation dose from contact patterns and restriction periods. 

https://github.com/SAMI-Medical-Physics/glowgreen

## Tests

A limited number of tests can be ran using `pytest`. Install `pytest`:

    pip install pytest


Add the **dorn-master\src** directory to the PYTHONPATH environment variable. For example, for Windows:

    set PYTHONPATH=%PYTHONPATH%;\path\to\dorn-master\src\

Then in the **dorn-master** directory run:

    python -m pytest

## Build an executable

Build an executable to run on computers that don't have Python installed. 

*Note the *.exe* file will only work on computers running the same platform as the computer on which it was built.* 

Install `cx_Freeze`:

    python -m pip install cx_Freeze

Currently does not work with `scipy` 1.9.2

    python -m pip install scipy==1.9.1

Then in the **dorn-master\src** directory run:
    
    python make_exe.py build

This generates a directory called something like **exe.win-amd64-3.9** inside **dorn-master\src\build**. 
You can copy this directory to another computer and run the program from the *Dorn.exe* file.

Note that we have to use

    base = None 

in *make_exe.py* for the command line interface to work in the *.exe*, but it means we're stuck with a black window popping up along with the GUI.

## Make icon file

The icon file *icofile.ico* was generated from *shovel.png* in Python.
Something like:

    python -m pip install Pillow

Then 

    from PIL import Image
    filename = 'shovel.png'
    img = Image.open(filename)
    icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
    img.save('new_icofile.ico', sizes=icon_sizes)


## Source 
https://github.com/SAMI-Medical-Physics/dorn

## Bug tracker
https://github.com/SAMI-Medical-Physics/dorn/issues

## Author
Jake Forster (Jake.Forster@sa.gov.au)

## Copyright
Dorn is Copyright (C) 2022 South Australia Medical Imaging.

## License
MIT license. See LICENSE file.

## Publications

Dorn reference paper:
- Close contact restriction periods for patients who received radioactive iodine-131 therapy for differentiated thyroid cancer, J. C. Forster et al., In preparation.

---------------------------------------

## Development

### Program overview

- Patient data is stored in an ordered dictionary. Program reads/writes patient data to XML files.

- Program settings are stored in another ordered dictionary, which has read/write with *settings.xml*.
If *settings.xml* does not exist at runtime, hard-coded settings are used in the program and a new *settings.xml* file is written. 
The hard-coded settings are applicable to South Australia Medical Imaging.

- Some settings cannot be edited via the GUI, such as the therapy options and the radionuclide data. 
The user may add at most 1 additional therapy options with measured clearance data and 1 additional therapy option with generic clearance via the command line interface (see below).

- A command-line interface is provided that offers additional flexibility. To see the command line options, enter:

        python dorn_cli.py -h

    or with the executable:

        Dorn.exe -h


### To do

Additional features considered:

- For therapy options that use generic clearance, allow the user to provide a single dose rate measurement to use for the clearance function parameter: initial dose rate at 1 m.
- Allow different distances for dose rate measurements.
- Allow the user to edit/add contact patterns.
- More dose rate measurement time points and a scroll bar.
- Add curve fit model representing no excretion at night. The difficulty will be adding the support in `glowgreen`.
- Add a familiar name field for the detector.
- Review contact patterns. 
- Low-, medium- and high-grade versions of patterns?
