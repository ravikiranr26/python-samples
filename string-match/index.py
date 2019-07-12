#!/usr/bin/env python

# import modules -- access the definitions in the 'sys' module and 're' for regular expression
import sys
import re


def string_print_count(filename, option):
    """Returns a word/print/count matching the option for this filename."""
    # opens and returns a file handle.
    input_file = open(filename, 'r')
    # reads the whole file into a single string
    text = input_file.read()
    # since file reading is done we close when finished.
    input_file.close()
    # splits on all whitespace chars, since no delimiters and store it in List
    words = text.split()
    # for word count we assign and start from 0
    wordcount = 0
    # iterating over all the string in the input file.
    for word in words:
        # transform all the string to uppercase since the input would be Upper case
        word = word.upper()
        # Special case when the search is for BEE string.
        if option == '--BEE':
            # using findAll and RegEx to find and match the string with regular expression for performance gains and efficiency
            match = re.findall(r'BEE', word)
            for word in match:
                # do something with each found match with the BEE string
                wordcount += 1
                print word
        # Special case when the search is for 4 Char string starting with A and ending with G
        elif option == '--4CharAG':
            # match the string with the regular expression for performance and effiency
            # instead of [a-zA-Z] we can also use \D in the Regex, which matches non digit
            match = re.findall(r'^A[a-zA-Z][a-zA-Z]G', word)
            for word in match:
                # do something with each found match with the AXXG string
                wordcount += 1
                print word
        # Special case when the search is for 8 Char string starting with D and ending with B and having CC sequence between DB
        elif option == '--8CharDB':
            # match the string with the regular expression for performance and effiency
             # instead of [a-zA-Z] we can also use \D in the Regex, which matches non digit
            match = re.findall(r'(^D[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]B)\1', word)
            for word in match:
                # do something with each found match with the DXXXXXXB and CC in XXXXXX string
                if 'CC' in word:
                 wordcount += 1
                 print word
        else:
            print 'unknown option:' + option
    return wordcount

def print_bee(filename, option):
    """Prints one per line '<word> <count>' for the given file."""
    bee_count = string_print_count(filename, option)
    bee_word = "bee count is:"
    print bee_word, bee_count

def print_4charAG(filename, option):
    """Prints one per line '<word> <count>' for the given file."""
    axxg_count = string_print_count(filename, option)
    axxg_word = "4Char count is:"
    print axxg_word, axxg_count

def print_8charDB(filename, option):
    """Prints one per line '<word> <count>' for the given file."""
    dxxxxxxb_count = string_print_count(filename, option)
    dxxxxxxb_word = "8Char count is:"
    print dxxxxxxb_word, dxxxxxxb_count

# main() function
"""
    Program prints and counts the string matching the user provided variants.

    Parameters
    ----------
    arg1 : str
        The user string to search and match, can be BEE, AXXG (XX can be [A-Z, a-z]), DXXXXXXB (XXXXXX can string with CC sequence)
    arg2 : str
        The filename which contains the strings provided by the user to be search in for matches.

    Returns
    -------
    str
    int
        Prints all the matching string in the file
        Counts the number of matching string in the file

"""
def main():
    if len(sys.argv) != 3:
        print 'usage: python index.py {--BEE | --4CharAG | --8CharDB } filename'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '--BEE':
        print_bee(filename, option)
    elif option == '--4CharAG':
        print_4charAG(filename, option)
    elif option == '--8CharDB':
        print_8charDB(filename, option)
    else:
        print 'unknown option:' + option
        sys.exit(1)

# call the main() function to begin the program.
if __name__ == '__main__':
    main()
