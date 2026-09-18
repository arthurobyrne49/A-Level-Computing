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