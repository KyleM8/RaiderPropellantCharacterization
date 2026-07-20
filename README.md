# RaiderPropellantCharacterization
Program for interpretation of subscale static fire data to characterize propellants.
Developed for Raider Aerospace Society (Space Raiders) at Texas Tech University.

NOTE: CURRENTLY ONLY BATES GRAINS ARE SUPPORTED!
<br>

## Reference
Nakka characterization resources:
[Nakka PTBurn](https://www.nakka-rocketry.net/ptburn.html)
[Nakka Burnrate](https://www.nakka-rocketry.net/burnrate.html)
[Nakka Burnrate Simple](https://www.nakka-rocketry.net/burnrate-simple.htm)

This program uses the method listed at the PTBurn link to calculate the regression and burn rate, but uses the average burn rate and pressure over several different static test fires to obtain a more representative solution.
<br>

## Dependencies
If you are not using the .exe release (still to come), the libraries imported in the Characterization.py file are required: you must have these libraries installed for this software to run correctly. If you believe there is an error caused by a library version issue, please contact me; there have been issues with this in the past. Mandatory libraries include: `os`, `pandas`, `scipy`, `numpy`, `math`, `matplotlib`, `openpyxl`, `pyyaml`, `FreeSimpleGUI`.
<br>

## Configuration File Formatting
Sample .yaml file:
```
pressUnits: "psig" #"psig" or kPa
thrustUnits: "lbf" #"lbf" or "N"

psmoothing: [-1, -1, -1] #array for pressure smoothing values: set to -1 for no smoothing, and set to a value between 0 and 1 for smoothing (higher number -> more smoothing)
tsmoothing: [-1, -1, -1] #array for thrust smoothing values

geometryUnits: "in" #"in" or "mm"
geometry: [[3.139,0.75,1.8], [3.139,0.75,1.8], [3.139,0.75,1.8], [3.139,1,1.8]] #geometry information: starting with the forwardmost grain and ending with the aftmost grain, one array for each grain with the grain length, core diameter, and outer diameter in that order

throatUnits: "in" #"in" or "mm"
throatDiameter: [0.546, 0.531, 0.515] #array of throat diameters for each fire

massUnits: "lb" #"lb" or "kg"
mass: [1.525, 1.525, 1.525] #array of mass values for each fire

densityUnits: "lb/in3" #"lb/in3" or "kg/m3"
density: [0.0589986, 0.0589986, 0.0589986] #array of density values for each fire
```
Configuration file formatting details:
* `pressUnits`: Units for pressure data. Only `psig` and `kPa` (psi gauge and kilopascals) are accepted entries.
* `thrustUnits`: Units for thrust data. Only `lbf` and `N` (pounds-force and Newtons) are accepted entries.
* `psmoothing` & `tsmoothing`: Array containing data denoting whether smoothing is turned on or off for pressure (`psmoothing`) and thrust (`tsmoothing`) data for each fire. Entries of -1 denote smoothing turned off, and values between 0 and 1 directly correspond to the window spacing for smoothing (i.e. how much smoothing there should be; a higher value corresponds to more smoothing).
* `geometryUnits`: Units used for the motor geometry. Only `in` and `mm` (inches and millimeters) are accepted entries.
* `geometry`: A 2D array containing geometry information for the motor being tested. Starting from the forwardmost grain and ending with the aftmost grain, each array contains the grain length, core diameter, and outer diameter. (In this example, there are four grains with a length of 3.139". The forwardmost three grains have a core diameter of 0.75" and the aftmost grain has a core diameter of 1". And the outer diameter for all four grains is 1.8".)
* `throatUnits`: Units used for the throat diameter. Only `in` and `mm` (inches and millimeters) are accepted entries.
* `throatDiameter`: Array of throat diameters for each fire. Again, these numbers must be entered in the order in which the fires appear as worksheets in the Excel workbook given at the beginning of the configuration. If there are multiple fires with the same throat diameter, it must be entered multiple times.
* `massUnits`: Units for propellant mass. Accepted units are `lb` or `kg` (pounds or kilograms).
* `mass`: Array of propellant mass values for each fire with data in the entered Excel workbook in the order in which the fires appear in the workbook.
* `densityUnits`: Units for propellant density. Accepted units are `lb/in3` or `kg/m3` (pounds per cubic inch or kilograms per cubic meters).
* `density`: Propellant density for each fire with data in the entered Excel workbook in the order in which the fires appear in the workbook.

The file should be a .yaml file and the full path to the file must be included as the first argument in the command line call to run the Characterization.py script.

Currently, running two different propellants (i.e. two sets of static fires) at the same time is not supported due to the current structure of the .yaml file and GUI.
<br>

## Running the Program
The main method for this program is contained in `Characterization.py`. It can be called from the command line: `python Characterization.py` (assuming the terminal is open to the directory where `Characterization.py` is contained) or run from your preferred IDE. Just ensure you have all the requisite libraries installed and updated. Currently there is no single-file .exe distribution, however, this would be one of the next steps towards making this more user-friendly.

When the code is run, a GUI window will open:

<img width="512" height="382" alt="image" src="https://github.com/user-attachments/assets/81bfaeae-d05a-4677-9750-76d00842930f" />

Click the "Browse" button near the entries for each file and select the input files (the .yaml for the YAML input, the .xlsx for the input static fire data, and the directory where the folder for the output files should be created).

Once all the files have been selected, click the "Perform Characterization Calculations" button. This will begin the characterization calculations, which usually take only a few seconds. Writing to the output Excel file can take longer depending on how much data there is (i.e. how many lines are in the input Excel). Status messages will be printed to the terminal; the final two lines should read:
<img width="555" height="42" alt="image" src="https://github.com/user-attachments/assets/24e1e4a5-de11-430c-97df-15b7e0030760" />

These two lines printed to the terminal means that the program has concluded and the output files can be viewed in the new folder (named "out1", "out2", or similar) created in the directory that was selected as the output folder.

The code outputs a variety of simple plots for quick sanity checks (in the future these plots should be refined), as well as an Excel sheet with all the calculated data from all static fires in both Imperial and SI units and, of course, the burn rate laws. Please note: after the output directory is selected, the program checks for previous folders (`out1`, `out2`, etc.) in the chosen directory and names the new output folder with this in mind so that any new output will not overwrite any previous output. Some screenshots of sample output data are below, and more detailed examples can be found in the `examples` folder in this repository.
<img width="1300" height="800" alt="0,1__burnrate-burnarea_imperial" src="https://github.com/user-attachments/assets/75c38ca1-1c54-4e1c-8c34-39230958fb31" />
<img width="1300" height="800" alt="0,1__thrust-pressure_imperial" src="https://github.com/user-attachments/assets/9ac15d00-8ae0-4e7a-85c8-5f0f1c2e2e23" />
<img width="1300" height="800" alt="characterization_imperial_0" src="https://github.com/user-attachments/assets/004f8393-e9e7-4089-bed4-7140ab8d5baf" />
<img width="1867" height="777" alt="image" src="https://github.com/user-attachments/assets/0343fc22-4816-4bb1-89ab-a3a0f54fe849" />
<img width="353" height="267" alt="image" src="https://github.com/user-attachments/assets/eb0dd6d7-1436-4789-9da0-5d8e41ea25f7" />
<br>

## Input Data Excel Formatting
Each workbook used with this script must be composed of worksheets that include data for each fire. The first column of each sheet should be time, the second column should be pressure, and the third column should be thrust. It doesn't matter if the data has a header or not (but if it does, this header must not be more than one row). Example inputs and outputs are included in this repository. Ensure your entries follow the established data input format, or the code will not work.
<br>

## CHECK YOUR INPUTS!
The most common cause of inacurrate output is inaccurate input!
<br>

## Version/Update Notes
Please note that this should be considered a v0.5 release. It has full functionality in terms of being able to characterize propellants, however, it does not have a single-file .exe distribution, the plots could be improved, and some additional features and statistics could be added. This repository is licensed under GNU GPLv3, so changes and improvements to the functionality of this program are welcomed.
