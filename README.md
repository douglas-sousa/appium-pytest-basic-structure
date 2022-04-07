# Eribank Appium Test
Example project showing a basic structure to run tests on Android with Appium
## Requirements
You need python 3.6+ for this project to be run on your machine.
All requirements are listed on the *requirements.txt* file. You can install all the requirements of this project using pip as decribed below :

Linux:
```
> $ python3 -m venv venv # Optional (but recommended) creation of virtual environment for the project
> $ source venv/bin/activate # Activation of the created virtual environment
> $ pip install -r requirements.txt # Recursively install all requirements listed on file
```

## Configurations
It's necessary to update config.py to match your android specs.
You can find those infos with the following commands
```
adb shell getprop ro.kernel.qemu.avd_name # name of your android
adb shell getprop ro.build.version.release # android version
adb devices # returns the ID for the device that's connected to the computer
```

## Based on
https://github.com/jonathassilva/appium-practices

## Running the test
Turn on the appium server either by its CLI or desktop app and type pytest on your terminal and you're good to go