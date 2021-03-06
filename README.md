# Phone Scraper Test

This software runs in Python and is only used as a testing program for web scraping. In this example, it goes to the BT PHONE BOOK and gets all the phone numbers from the directory. To ensure that it does not cause harm to the BT Phone Book website, it delays each request to not overload the website.

## Usage

Make sure Python and pip are installed. (This was developed and the following guide is done on Windows. Please check the steps for [MacOS](#macos) and Linux)

Clone the repository into a folder/directory of your choice.

```
$ git clone https://github.com/NardiniA/phone-scraper-test <new_name> 
```

(new_name is an optional parameter)

### Windows

```
$ python --version
$
$ pip --version
```

Install Virtualenv.

```
$ python -m pip install --user virtualenv
```

Create a virtualenv.

```
$ python -m virtualenv venv
```

Start virtualenv using batch file.

```
$ venv\Scripts\activate
```

Install dependencies.

```
$ pip install -r requirements.txt
```

Run app.py

```
$ python app.py
```

To deactivate virtual environment.

```
$ venv\Scripts\deactivate
```

### MacOS

```
$ python3 --version
$
$ pip3 --version
```

Install Virtualenv.

```
$ pip3 install virtualenv
```

Create a virtualenv.

```
$ virtualenv venv
```

Or

```
$ virtualenv -p python3 venv
```

Start virtualenv using batch file.

```
$ source venv\bin\activate
```

Install dependencies.

```
$ pip3 install -r requirements.txt
```

Run app.py.

```
$ python3 app.py
```

To deactivate virtual environment.

```
$ deactivate
```

## For the cool kids, like Wilfred.

To look cool or nerdy infront of your friends, run:

```
$ color a
```

to turn terminal text green or run:

```
$ color f
```

to turn it back to white.

## Cross Platform

This project is written in python and should run fine in cross platform environments. However, problems may arise on MacOS and Linux as this was developed on a Windows 10 operating system. For problems that arise contact the developer, Antonio Nardini or add to the issues tab on [this repository](https://github.com/NardiniA/phone-scraper-test/issues).

## Bug Fixes

Some may experience where they cannot select an option, when asking which search format youwould like. To move between them, use the arrows or the numpad arrows (ensure numlock is on).

## Disclaimer

This software is only a test and should only be used in accordance with the laws of your land and the terms of BT Phone Book website. As of 02.02.2022, it is lawful to use this software. However, the data provided by this software requires to be in accordance with any GDPR or any other Personal Data laws.
