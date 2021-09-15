# CONTRIBUTING GUIDE

https://www.dataschool.io/how-to-contribute-on-github/

Use Powershell/Command Line for the following commands

*Note:* here terminal and command line mean the same thing, and are used interchangeably.

## Clone this repository on your local machine
First change the current directory to your choice, example *Desktop*

```
$ git clone https://github.com/GuptaAyush19/weather-update.git
```

This command will open vscode

```
$ code weather-update
```

## Create a virtual environment and launch it
To first create a virtual environment, run this command in your terminal. Don't run this segment in Powershell, but on Command Line (cmd)
```
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ python -m venv env
```
Once the virtual environment is created, run this command to launch it
```
$ env\Scripts\activate.bat
```

## Run the unittest
Run this command in command line to test the modules
```
$ python -m unittest discover -s tests
```