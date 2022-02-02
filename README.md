# Phone Scraper Test

This software runs in Python and is only used as a testing program for web scraping. In this example, it goes to the BT PHONE BOOK and gets all the phone numbers from the directory. To ensure that it does not cause harm to the BT Phone Book website, it delays each request to not overload the website.

## Usage

Make sure Python and pip are installed. (This was developed and the following guide is done on Windows. Please check the steps for MacOS and Linux)

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

Start a virtualenv.

```
$ python -m virtualenv venv
```

Enable virtualenv.

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

Start a virtualenv.

```
$ virtualenv venv
```

Or

```
$ virtualenv -p python3 venv
```

Enable virtualenv.

```
$ source venv\bin\activate
```

Install dependencies.

```
$ pip3 install -r requirements.txt
```

Run app.py

```
$ python3 app.py
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

This project is written in python and should run fine in cross platform environments. However, problems may arise on MacOS and Linux as this was developed on a Windows 10 operating system. For problems that arise contact the developer, Antonio Nardini or add to the issues tab on [https://github.com/NardiniA/phone-scraper-test/issues](this repository).

## Disclaimer

This software is only a test and should only be used in accordance with the laws of your land and the terms of BT Phone Book website. As of 02.02.2022, it is lawful to use this software. However, the data provided by this software requires to be in accordance with any GDPR or any other Personal Data laws.
