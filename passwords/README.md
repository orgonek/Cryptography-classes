# SQLite password storage	
## Description

An assignment for a cryptography class. It contains an implementation of a simple login system, using SQLite database. 
The user enters a name and password, which is hashed using the SHA256 algorithm and a random salt.

## Installation

1. Clone this repository
```console
$ git clone https://github.com/orgonek/Cryptography-classes.git
```
2. Change directory 
```console
$ cd passwords
```
3. Install required packages
```console
$ pip install -r requirements.txt 
```

## Usage
To run tests
```console
$ pytest 
```
To run scripts
```console
$ cd src
$ python main_cli.py [option]
```
### Options 
*register*- allows the user to register

*login* - user can login using account created earlier



