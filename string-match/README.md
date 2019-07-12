## Prequites: Python Set Up
Python is free and open source, available for all operating systems from [python.org](http://python.org/)
Please install based on your operating system.

Before running, please check that Python is installed, open a command line (typically by running the "Terminal" program) and type
```sh
python
```

## Introduction: String print and count program which implements the following functionality as follows
This program would match for the string provided by the user, and prints the matched string and gives the count
Program takes the input string and text file as input.

## Count and Print string "BEE":
From the given input "exercise_data.txt" we print and count the string "BEE" occurance in the file.
To Run: please issue the following command,
```sh
python index.py --BEE exercise_data.txt
```

**Output:**
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
BEE
bee count is: 45

## Count and Print string of 4 characters that starts with A and ends with G, with any two characters in between.
From the given input "exercise_data.txt" we print and count the string to accomplish the statement above.
**To Run:**
```sh
python index.py --4CharAG exercise_data.txt
```

**Output**
ABCG
AHHG
AFGG
AFGG
ABDG
ABDG
ACEG
4Char count is: 7 

## Count and Print string of 8 characters that starts with D and ends with B, with the sequence "CC" present somewhere in the string.
From the given input "exercise_data.txt" we print and count the string to accomplish the statement above.
**To Run:**
```sh
python index.py --8CharDB  exercise_data.txt
``` 

**Output**
8Char count is: 0


**TODO**
The code where it checks for option == "" and matches the string can be extracted to a higher order function and make it resuable 

**CHANGELOG**
v0.1 = this is the inital version and contains functions which matches string provides