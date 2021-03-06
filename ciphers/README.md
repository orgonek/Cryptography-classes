# Caesar and Vigenère ciphers	
## Description

A console application, written using Python language. The project contains the implementation of Caesar and Vigenere ciphers. 
The user can encrypt and decrypt the text, using predefined values such as text, shift, and key. 
Additionally, in the case of Caesar cipher, it is possible to crack ciphered text without knowing the key using the following methods:

- manual decryption, showing all possibilities 
- user-based shift guessing
- automatic cracking, based on English dictionary

## Installation

1. Clone this repository
```console
$ git clone https://github.com/orgonek/Cryptography-classes.git
```
2. Install required packages
```console
$ pip install -r requirements.txt 
```

## Usage
To run tests
```console
$ pytest ciphers
```
To run scripts
```console
$ cd ciphers/src
$ python caesar_cli.py 
$ python vigenere_cli.py 
$ python caesar_cracker_cli.py 
```



