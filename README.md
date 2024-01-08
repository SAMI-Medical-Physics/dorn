[![DOI](https://zenodo.org/badge/549013816.svg)](https://zenodo.org/badge/latestdoi/549013816)

# Dorn

Dorn is a Python GUI program for generating individual close contact restrictions for radionuclide therapy patients.
Some example use cases are shown in the Table below.

| Radionuclide therapy                         | In/outpatient | Dose rate measurements |
|----------------------------------------------|---------------|------------------------|
| I-131 for thyroid cancer                     | Inpatient     | Yes                    |
| I-131 for hyperthyroidism                    | Outpatient    | No                     |
| Lu-177-dotatate for neuroendocrine neoplasms | Outpatient    | Yes                    |
 
## Requires

Python >= 3.9

## Dependencies

Python package dependencies:
- `numpy`
- `scipy`
- `matplotlib`
- `pandas`
- `glowgreen`
- `xmltodict`
- `python-docx`


## Platforms 

The Python files *dorn.py* and *dorn_cli.py* are known to run on:
- Windows 10
- Windows 11
- Ubtuntu 22.04.2 LTS

They probably also run on Windows 7 but I can no longer confirm. I have not tried on macOS.

On Linux, some of the GUI windows are too small and need to be expanded to reveal content. 
Also note that LibreOffice does not render the generated report *.docx* files correctly; the restriction tables are not formatted as intended. 


## glowgreen package

Dorn uses the Python package `glowgreen` for calculating radiation dose from contact patterns and restriction periods. 

https://github.com/SAMI-Medical-Physics/glowgreen

## Tests

A limited number of tests can be ran using `pytest`. Install `pytest`:

    python -m pip install pytest


Add the **dorn-master\src** directory to the PYTHONPATH environment variable. For Windows:

    set PYTHONPATH=%PYTHONPATH%;\path\to\dorn-master\src\
    
For Linux: 

    export PYTHONPATH="${PYTHONPATH}:/path/to/dorn-master/src/"

Then in the **dorn-master** directory run:

    python -m pytest

## Executable provided with release

Each release on Github includes a zip file. The zip file contains an executable file *Dorn.exe* that can be used to run the Dorn program on Windows 10 and 11 systems without needing to install Python and Dorn's other dependencies.

The executable for Windows provided with the current release (version 1.10.x) was built using the following:

- Windows 10
- Python 3.11.2
- `pip` == 23.2.1
- `numpy` == 1.24.2
- `scipy` == 1.11.2
- `matplotlib` == 3.8.0
- `pandas` == 2.1.0
- `glowgreen` == 0.1.0
- `xmltodict` == 0.13.0
- `python-docx` == 0.8.11
- `cx_Freeze` == 6.15.7

## Build your own standalone executable

Follow these instructions to build a standalone executable of Dorn that can run on computers that don't have Python installed.
This requires Python and the Python packages listed above.

Note the executable will only work on computers running the same platform as the computer on which it was built.

Install `cx_Freeze`:

    python -m pip install cx_Freeze

Then in the **dorn-master\src** directory run:
    
    python make_exe.py build

This generates a directory called something like **exe.win-amd64-3.11** inside **dorn-master\src\build**. 
You can copy this directory to another computer and run the program from the *Dorn.exe* file.

Note that we have to use

    base = None 

in *make_exe.py* for the command line interface to work in the *.exe*, but it means we're stuck with a console popping up along with the GUI.

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
Jake Forster (jake.forster@sa.gov.au)

## Copyright
Dorn is copyright (C) 2022, 2023 South Australia Medical Imaging.

## License
MIT License. See LICENSE file.

## Citation
See CITATION.cff file. 

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


### TODO

New features considered:

- For therapy options that use generic clearance, allow the user to provide an initial dose rate measurement to determine the clearance function parameter: initial dose rate at 1 m.
- Add more dose rate measurement time points and a scroll bar.
- Add curve fit model representing no excretion at night. The difficulty will be adding the support in `glowgreen`.
- Add a familiar name field for the detector.
- Review appropriateness of contact patterns. 
- Attempt to propagate uncertainty from the contact pattern onto the calculated restriction period or dose.
- Allow the user to edit/add contact patterns.
