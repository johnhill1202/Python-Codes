string1=input("Enter string 1: ")
string2=input("Enter string 2: ")

string_1=sorted(string1.lower())
string_2=sorted(string2.lower())

print(string2 + " and " + string1 + " are anagrams" if (string_1==string_2) else string2 + " and " + string1 + " are not anagrams")

#string function ".join not available in this version of python