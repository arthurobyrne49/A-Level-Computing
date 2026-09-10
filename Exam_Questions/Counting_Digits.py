"""
Q1. 
Write a program that asks the user how many numeric digits they would like to enter,
and then gets the user to enter that number of numeric digits.
The program should calculate and display the number of times the most frequently
entered numeric digit was input.
If more than one numeric digit had the same frequency and was the most requently
entered than instead of displaying the frequency, a message saying "Data was 
multimodal" should be displayed.
"""


total_digits = int(input("How many digits do you want to enter? "))
digits = str(input("Enter digits: "))
frequency = 0
mode = ""
for i in range(total_digits):
    num_current_digit = 1    
    for j in range(i+ 1, total_digits):
        if i != j and digits[i] == digits[j]:
            num_current_digit += 1
    if num_current_digit > frequency:
        frequency = num_current_digit
        mode = digits[i]
    elif num_current_digit == frequency and digits[i] not in mode:
        mode += digits[i]
if len(mode) > 1:
    print("Data was multimodal.")
else:
    print("Mode: " + mode)
    print("Frequency: " + str(frequency))



