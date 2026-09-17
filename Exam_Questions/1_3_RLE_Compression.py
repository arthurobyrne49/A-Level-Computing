"""
Q1.
One method that can be used to compress text data is run length encoding (RLE). When RLE is
used the compressed data can be represented as a set of character/frequency pairs. When the 
same character appears in consecutive locations in the original text it is replaced in the
compressed text by a single instance of the character followed by a number indicating the 
number of consecutive instances of that character. Single instances of a character are
represented by the character followed by the number 1.

Write a program that will perform the compression process described above. The program
should display a suitable prompt asking the user to input the text to compress and then output 
the compressed text.
"""




s1 = str(input("Input Original String: ")) 
print(s1) 
s2 = "" 
position = 0 
while position < len(s1): 
    slider = 0 
    while position + slider < len(s1) and s1[position] == s1[position + slider]: 
        slider += 1 
    s2 = s2 + s1[position] + " " + str(slider) +" "
    position += slider
print(s2)
