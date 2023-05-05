# fpyo2ipa
A package tool that allow you to built a python iOS apps with flet UI.

⚠️Note: this is a macOS only package.

## How does it work ?
It take the flet-pyodide `dist` folder then create an xcode project with briefcase iOS-python-version then load the pyodide as a localhost.

## requirements
- xcode (12>)
- briefcase (it will be installed if you install this package)

## usage
I am try to make it simple as possible.

This is a video tutorial: [Tutorial](https://youtu.be/PC9sXtuKqPQ)

1- Create a flet `dist` folder.

```
flet publish main.py
```

2- create a python virtual environment.

```
python3 -m venv venv
```

3- install this package.

```
pip install fpyo2ipa --upgrade
```

4- use this build tool.

```
python3 -m fpyo2ipa.build
```
Follow the instructions then you are there!!
