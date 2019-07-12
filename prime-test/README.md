# Summary: Testing a Prime number program that outputs all prime number supplied by user. 
Testing objective of the program by focusing on tests that achieve a high percentage of Statement, Branch, or Path coverage.
Used [JEST](https://jestjs.io/) to unit test the program, which works with Typescript, React, Angular, Vue etc.

## System Description
Definition: A positive integer not divisible without a remainder by any positive integer other than itself and one.

The specification says the program should print all prime numbers provided by the user. A valid input is any number which is greater than argument1 and lesser than argument2

## Test Design
1: We would write the test case that would achieve high percentage of **Statement Coverage**. Asumming the prime number program has conditions and statment would be exectued based on it.
We can achieve 100% coverage with only one test (subject to the progam implementation, here we assume Sieve algorithm): where **Input=(-5, -2)**
But to list all the different edge cases we can list out the different input combinations as follows,
test 1: **input=(-1, -1)**
test 2: **input=('a', 'b')**
test 3: **input=(0.11, 12.2)**
test 4: **input=(0, 0)**
test 5: **input=(-2, 4)**
test 6: **input=(2, -4)**

2: We would write the test case that would achieve high percentage of **Branch Coverage**. the test coverage criteria which requires that for each decision point each possible branch be executed at least once. Assumming the prime number program has conditions
We can achieve 100% branch coverage with only 2 test (subject to the progam implementation, here we assume Sieve algorithm): where **Input=(0, 2), Input=(1, 10)**
But to list all the different edge cases we can list out the different input combinations as follows,
test 1: **input=(1, 10)**
test 2: **input=(97, 100)**

3: We would write the test cases that would achieve high percentange of **Path Coverage**. we measure by the percentage of different execution paths that have been taken through the source code
We can achieve 100% branch coverage with only 3 test (subject to the progam implementation, here we assume Sieve algorithm): where **Input=(1, 2), Input=(5, 10), Input=(3, 10)**
But to list all the different edge cases we can list out the different input combinations as follows,
test 1: **input=(3, 1)**
test 2: **input=(5, 7)**

## Acceptance Criteria
Program should accept two integer arguments where "x<y" and print all the prime numbers which greater than x and lesser than y.

## RUN
```sh
npm test
```
With coverage Jest collects information of statments, branches, functions, lines covered in %
```sh
npm test --coverage
```

**NOTE**
This is to be considered as a template to just define the progam test design.
Again even though we achieved 100% coverage, there are bugs that could be missed. As the program implementation is not known and also user input can be of different max range.

