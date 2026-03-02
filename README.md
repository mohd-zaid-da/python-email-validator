# Python Email Validator

A Python project that validates email addresses using two different approaches:

- Manual string validation (without regex)
- Regular Expression (Regex) based validation

This project demonstrates fundamental Python logic building and pattern matching using the re module.

--------------------------------------------------

## Features

Manual Validation:
- Checks minimum length
- Ensures only one '@' symbol
- Prevents spaces
- Validates domain structure
- Allows only valid characters
- Verifies top-level domain length

Regex Validation:
- Uses regular expressions for pattern matching
- Validates username format
- Validates domain name
- Ensures valid top-level domain (TLD)

--------------------------------------------------

## How to Run

Manual Version:
python manual_email_validator.py

Regex Version:
python email-validator-regex.py

--------------------------------------------------

## Project Structure

python-email-validator/
│
├── manual_email_validator.py
├── email-validator-regex.py
└── README.md

--------------------------------------------------

## Future Improvements

- Add advanced RFC-compliant email validation
- Convert script into reusable functions
- Add unit testing
- Create a simple CLI version
- Add GUI version (Tkinter)

--------------------------------------------------

Author:
Mohd Zaid
