# Nexstar Python API

This code follows the NexStar Communication Protocol as described in NexStarCommunicationProtocolV1.2.pdf

This latest version of this code is located at https://github.com/matt404/nexstar

This code is forked from 
https://github.com/circuitqed/nexstar
https://github.com/sidneycadot/nexstar

The main class is NexstarHandController and supports the following methods:

* getAlignmentComplete - Check to see if the telescope alignment has been completed.
* getDeviceVersion - Get the version of the telescope device.
* getGotoInProgress - Check if the telescope is slewing to a GoTo target.
* getLocation - Get the location coordinates of the telescope.
* getModel - Get the telescope model.
* getPosition - Get the position currently targeted by the telescope.
* getTime - Get the current time setting from the telescope.
* getTrackingMode - Gets the current tracking mode, ie alt-az or eq north/south
* getVersion
* gotoPosition - Command the telescope to GoTo a new target position
* passthrough - For sending un-modeled commands as a pass-through
* setLocation - Set the lat/lng coordinates of the telescope
* setTime - Set the time on the telescope.
* setTrackingMode - Sets the tracking mode on the telescope
* slew_fixed
* slew_variable
* sync - To sync the telescope to re-center the current GoTo target.

#### Install Package Locally

```shell
sudo python3 setup.py install
```
