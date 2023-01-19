#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The objective of the homework assignment is to design and implement a function
that reads some strings contained in a series of files and generates a new
string from all the strings read.
The strings to be read are contained in several files, linked together to
form a closed chain. The first string in each file is the name of another
file that belongs to the chain: starting from any file and following the
chain, you always return to the starting file.

Example: the first line of file "A.txt" is "B.txt," the first line of file
"B.txt" is "C.txt," and the first line of "C.txt" is "A.txt," forming the
chain "A.txt"-"B.txt"-"C.txt".

In addition to the string with the name of the next file, each file also
contains other strings separated by spaces, tabs, or carriage return
characters. The function must read all the strings in the files in the chain
and construct the string obtained by concatenating the characters with the
highest frequency in each position. That is, in the string to be constructed,
at position p, there will be the character with the highest frequency at
position p of each string read from the files. In the case where there are
multiple characters with the same frequency, consider the alphabetical order.
The generated string has a length equal to the maximum length of the strings
read from the files.

Therefore, you must write a function that takes as input a string "filename"
representing the name of a file and returns a string.
The function must construct the string according to the directions outlined
above and return the constructed string.

Example: if the contents of the three files A.txt, B.txt, and C.txt in the
directory test01 are as follows


test01/A.txt          test01/B.txt         test01/C.txt
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite
garden                park                 hello
kitchen               affair               portrait
balloon                                    angel
                                           surfing

the function most_frequent_chars ("test01/A.txt") will return "hareennt".
"""


def most_frequent_chars(file):
    search_list = []
    list_string = []

    # assign next file path until reaching first file
    next_file = create_search_list(filename=file, search_list=search_list)

    while next_file != file:
        next_file = create_search_list(filename=next_file, search_list=search_list)

    # find the longest string length
    longest_string = max(search_list, key=len)
    counter = len(longest_string)

    appendable = ""
    for i in range(0, counter):
        # empty char list
        char_list = []
        for word in search_list:
            try:
                # append each word's ith char to char list
                char_list.append(word[i])
            except IndexError:
                pass
        # create 2D list contains char and frequency
        char_counts = [[x, char_list.count(x)] for x in list(set(char_list))]
        char_counts.sort(key=lambda x: x[0])

        # find the highest frequency char
        max_count = 0
        for item in char_counts:
            if item[1] > max_count:
                appendable = item[0]
                max_count = item[1]
        # append the highest frequency char to list_string
        list_string.append(appendable)
        char_counts.clear()
        appendable = ""
    # turn list to string
    new_string = "".join(list_string)
    return new_string


def create_search_list(filename, search_list):

    with open(filename, "r") as f:
        lines = (line.strip() for line in f)
        lines = list(line for line in lines if line)

    for line in lines[1:]:
        # split lines with multiple words
        line = line.split()
        for word in line:
            # append words to search list
            search_list.append(word)
    # return next file path
    return lines[0]


if __name__ == '__main__':
    print(most_frequent_chars("test06/strums.txt"))

