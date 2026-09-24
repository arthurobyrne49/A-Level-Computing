"""
Q1.
Write a program that uses a transposition cipher to encrypt a string entered by the user.

After the user enters the script to encrypt, they enter the number of columns to use. Different
numbers of columns result in different encrypted versions of the same string.

Any non-alphabetic characters in the string entered by the user are ignored and will not appear in
the encrypted text.

To encrypt the string, the characters from the user's input are written into a grid (left to right, top
to bottom) of cells which has the number of columns specified by the user. The characters are
then read from the grid in a different order (top to bottom, left to right)."""


s1 = input("Enter string to encrypt: ")
alphabet_string = ""
columns = int(input("How many columns? "))
transposed_string = ""
position = 0
shift = 0

for i in range(len(s1)):
    if 97 <= ord(s1[i]) <= 122 or 65 <= ord(s1[i]) <= 90:
        alphabet_string = alphabet_string + s1[i]

while shift < columns:
    while position < len(alphabet_string) and position + shift < len(alphabet_string):
        transposed_string = transposed_string + alphabet_string[position + shift]
        position += int(columns)
    shift += 1
    position = 0

print(transposed_string)