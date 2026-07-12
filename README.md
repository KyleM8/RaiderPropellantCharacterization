# RAS-SR-SRM-Characterization
Scripts for characterization for RAS Space Raiders solid rocket motors.

NOTE: CURRENTLY ONLY BATES GRAINS ARE SUPPORTED!

### Reference
Nakka characterization resources:
[Nakka PTBurn](https://www.nakka-rocketry.net/ptburn.html)
[Nakka Burnrate](https://www.nakka-rocketry.net/burnrate.html)
[Nakka Burnrate Simple](https://www.nakka-rocketry.net/burnrate-simple.htm)

This method uses the method listed at the PTBurn link, but uses the average burn rate and pressure over several different static test fires.

### Dependencies
If you are not using the .exe release, the libraries imported in the Characterization.py file are required: you must have these libraries installed for this software to run correctly. If you believe there is an error caused by a library version issue, please contact me; there have been issues with this in the past.
argparse
os
pandas
scipy
numpy
math
matplotlib
openpyxl
pyyaml

### Configuration File Formatting
Sample .yaml file:
```
dataFilepath: '.\example_data_propellant1.xlsx' #full path OR relative path with respect to the .yaml file to the .xlsx data file containing formatted static fire data 

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
* `dataFilepath`: (explanation). This file should have worksheets with data from each static fire.
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

Currently, running two different propellants (i.e. two sets of static fires) at the same time is not supported.

### Running the Code
(This method is in process and not final yet. Some changes may be made to this method)

Open a command line from which you can run python programs. The command line prompt to run the program is:
`python <path to Characterization.py> "<path to input.yaml file>" "<path to folder in which output files should be created>"`

The easiest way to call this command is to use the command line to navigate to the `src` folder (where the Characterization.py script is stored). Then, assuming it is ok that output files will be created in the same directory as the script, the command line prompt would be:
`python Characterization.py "<path to input.yaml file>" "."`

### Excel Formatting
Each workbook used with this script must include sheets that include data for each fire. The first column of each sheet should be time, the second column should be pressure, and the third column should be thrust. It doesn't matter if the data has a header or not (but if it does, this header must not be more than one row). Example inputs and outputs are included in this repository. Ensure your entries follow the established format, or the code will not work.

### TRIPLE AND QUADRUPLE CHECK YOUR INPUTS! THE MOST COMMON CAUSE OF INACCURATE OUTPUT IS INACCURATE INPUT!
GARBAGE IN = GARBAGE OUT
