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
Sample entry:
```
!CONFIGSTART
filename test_data_propellant1.xlsx psig lbf
psmoothing off
tsmoothing off
geometry in 3.139,0.75,1.8||3.139,0.75,1.8||3.139,0.75,1.8||3.139,1,1.8
throat in 0.546 0.531 0.515
mass lb 1.525 1.525 1.525
density lb/in3 0.0589986 0.0589986 0.0589986
!CONFIGEND
!CONFIGSTART
filename test_data_propellant2.xlsx psig lbf
psmoothing off
tsmoothing on 0.075 0.075 0.075 0.075 0.075 0.075
geometry in 3.05,0.5,1.8||3.25,0.75,1.8
throat in 0.344 0.327 0.344 0.327 0.3195 0.289
mass lb 0.7782 0.7782 0.7782 0.7782 0.7782 0.7782
density lb/in3 0.0556 0.0556 0.0556 0.0556 0.0556 0.0556
!CONFIGEND
```
Configuration file formatting details:
* Line 1: `!CONFIGSTART` is the start of a characterization entry.
* Line 2: `file test_data.xlsx psig lbf` denotes the filename ("test_data.xlsx" here) and the pressure and thrust units associated with this static fire (here psig and lbf). Only `psig` and `kPa` (psi gauge and kilopascals) are accepted entries for pressure, and only `lbf` and `N` (pounds-force and Newtons) are accepted entries for thrust. This file should have worksheets with data from each static fire.
* Line 3-4. Denotes wherther smoothing is turned on or off for pressure (`psmoothing`) and thrust (`tsmoothing`) data. If turned on, the six following numbers separated by spaces denotes the window spacing (i.e. how much smoothing there should be; a higher value corresponds to more smoothing). If you want smoothing on some tests and not others, set the number to -1 for tests you do not want smoothing for.
* Line 5: `geometry in 3.139,0.75,1.8||3.139,0.75,1.8||3.139,0.75,1.8||3.139,1,1.8` denotes the geometry of the motor being tested. `in` denotes the units being used in this line (here inches). Only `in` and `mm` (inches and millimeters) are accepted entries. Separated by a double bar `||`, the grain length, core diameter, and outer diameter for each grain is entered, starting with the forwardmost grain and ending with the aftmost grain. (In this example, there are four grains with a length of 3.139". The forwardmost three grains have a core diameter of 0.75" and the aftmost grain has a core diameter of 1". And the outer diameter for all four grains is 1.8".)
* Line 6: `throat in 0.546 0.531 0.515` denotes the throat diameter for each fire with data in the entered Excel workbook. `in` denotes the units being used in this line (here inches). Only `in` and `mm` (inches and millimeters) are accepted entries. These numbers must be entered in the order in which the fires appear as worksheets in the Excel workbook given in Line 2 of the configuration. If there are multiple fires with the same throat diameter, it must be entered multiple times.
* Line 7: Propellant mass for each fire with data in the entered Excel workbook in the order in which the fires appear in the workbook. Accepted units are `lb` or `kg` (pounds or kilograms).
* Line 8: Propellant density for each fire with data in the entered Excel workbook in the order in which the fires appear in the workbook. Accepted units are `lb/in3` or `kg/m3` (pounds per cubic inch or kilograms per cubic meters).
* Line 9: `!CONFIGEND` denotes the end of a characterization entry. If another characterization entry is desired within the same configuration file, this series of 7 lines can be repeated for another series of fires.

Ensure there are no unnecessary spaces in the entry (a double-space or a space after a line could mess up the parsing of the config file).

The file should be a regular .txt file and the filename and path must be denoted in the characterization script (details in comments in the script). The configuration file as well as the Excel workbook(s) must be stored in the `dat` folder.

The benefit of using this configuration file is that changing the configuration file name in the script is the only change required to the script for any run.

Note that for one propellant, only one 9-line entry is required.

### Excel Formatting
Each workbook used with this script must include sheets that include data for each fire. The first column of each sheet should be time, the second column should be pressure, and the third column should be thrust. It doesn't matter if the data has a header or not (but if it does, this header must not be more than one row). Example inputs and outputs are included in this repository. Ensure your entries follow the established format, or the code will not work.

### TRIPLE AND QUADRUPLE CHECK YOUR INPUTS! THE MOST COMMON CAUSE OF INACCURATE OUTPUT IS INACCURATE INPUT!
GARBAGE IN = GARBAGE OUT
