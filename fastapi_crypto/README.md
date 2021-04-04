# FastAPI crypto API
## Description

A simple web application, written in Python using FastAPI. It is an API that offers the following features:
1. Symmetric algorithm
   * Generate random key
   * Set key
   * Encode message
   * Decode message 
2. Asymmetric algorithm
   * Generate random keys
   * Set keys
   * Sign message
   * Verify message
   * Encrypt message
   * Decrypt message
 
## Installation

1. Clone this repository
```console
$ git clone https://github.com/orgonek/Cryptography-classes.git
```
2. Change directory
```console
$ cd fastapi_crypto/
```
3. Install required packages
```console
$ pip install -e .
```

## Usage
To run tests
```console
$ pytest fastapi_crypto/
```
To run application
```console
$ cd fastapi_crypto/src
$ uvicorn main:app --reload
```

