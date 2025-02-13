# Write a generator function called char_counter(text)
# that yields each unique character in a string along 
# with the count of how many times it appears in the text.

# aabbcd
# a-2,b-2,c-1,d-1


def char_counter(str):
    dict = {}
    for char in str:
        dict[char] = dict.get(char,0)+1
    
    for key in dict:
        yield key,dict.get(key)
        
str =  input("Enter the input string : ")       
gen = char_counter(str)

for char in gen:
    print(char)
