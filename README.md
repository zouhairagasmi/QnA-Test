# QnA-Test
You are asked to write a program that counts unique words from an English text file, treating hyphen and apostrophe as part of the word. Your program should output the ten most frequent words and mention the number of occurrences.

## Installation
install [python3](https://www.python.org/downloads/release/python-382/).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install any required packages.

```bash
pip install requirmentname
```

## Usage
in order to run this project you need to open Terminal in project directory and run the following command :
```bash
python qna_solution.py
```
## Solution
This python program is using both the RegEx and Collections modules. 
Regex will return all the words in the file, but since we could have some words that are starting with Uppercase, so we transformed our output to lowercase. after that comes the Collections part where we have used the Counter() method which counts the frequency of each word and then I have used "most_common()" to sort them by frequency and only show the first 10 words.
I could implement a different program, where I create all these functions manually, but since it is written in python, it would be better to take advantage of the built-in packages at our disposal which will make the code: well structured, simple, and understandable.
