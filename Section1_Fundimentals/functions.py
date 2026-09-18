def alphabet_only(s1:str):
    alphabet_string = ""

    for i in range(len(s1)):
        if 97 <= ord(s1[i]) <= 122 or 65 <= ord(s1[i]) <= 90:
            alphabet_string = alphabet_string + s1[i]

    return(alphabet_string)

alphabetised = alphabet_only("fen9g7prh")
print(alphabetised)

