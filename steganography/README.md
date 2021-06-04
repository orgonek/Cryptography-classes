# Steganography CLI
## Description

An assignment for a cryptography class. Allows user to encode and decode message inside image.

## Installation

1. Clone this repository
```console
$ git clone https://github.com/orgonek/Cryptography-classes.git
```
2. Change directory 
```console
$ cd steganography/
```
3. Install required packages
```console
$ pip install -r requirements.txt 
```

## Usage
To run tests
```console
$ pytest *(inside steganography folder)*
```
To run scripts
```console
$ cd src
$ python main.py [option]
```
### Options 
*encode-message*- allows user to encrypt message inside image (vigenere/caesar ciphers available)

*decode-message* - allows user to decode hidden message

### Source
[Based on medium.com](https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2)



