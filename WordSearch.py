print("python terms")
puzzle = """
fjvfloatdy
yopxednins
mspfycnnal
xeaeeukgei
slufryprlc
abeeiagcoi
buclqttbon
gojlivxobg
admyahgerj
stringwvrs
"""

print(puzzle)
print("word list")
word_list = "float, while, if, boolean, doubled, operators, string, slicing, index"
print (word_list)

word1_length = len("float")
word2_length = len("while")
word3_length = len("if")
word4_length = len("boolean")
word5_length = len("double")
word6_length = len("operators")
word7_length = len("string")
word8_length = len("slicing")
word9_length = len("index")


word1 = input("enter the index position of float: ")
i = 0
foundword = ""
while i < word1_length:
    index = word1[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word2 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word2_length:
    index = word2[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word3 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word3_length:
    index = word3[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word4 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word4_length:
    index = word4[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word5 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word5_length:
    index = word5[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word6 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word6_length:
    index = word6[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word7 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word7_length:
    index = word7[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word8 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word8_length:
    index = word8[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)

word9 = input("enter the index position of while: ")
i = 0
foundword = ""
while i < word9_length:
    index = word9[i]
    index = int(index)
    foundword = foundword + puzzle[index + 1]
    i+=1
print(foundword)






























input("press enter to exit")
