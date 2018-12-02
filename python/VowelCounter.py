# Vamsi Sridhar
# 17/03/17
# SentenceProgram.py

"""
Pseudocode:

var sentence = input("Sentence")
sentence ==> convert to array
var length = length of sentence
array vowelcount = ["a","e","i","o","u"]
var vowelcheck = 0
REPEAT:
    var counter = 0
    FOR chr in sentence:
        IF chr == vowelcount[vowelcheck]:
            counter += 1
        END IF
    END FOR
    vowelcount[vowelcheck] = counter
    vowelcheck += 1
UNTIL vowelcheck == 5
print vowelcount >>>> The order of the numbers shown is a,e,i,o,u
"""

sentence = input("Your Sentence: ")
length = len(sentence)
vowelcount = ["a","e","i","o","u"]
vowelcheck = 0
while vowelcheck < 5:
    counter = 0
    for char in sentence:
        if char == vowelcount[vowelcheck]:
            counter += 1
    vowelcount[vowelcheck] = str(counter)
    vowelcheck += 1

print("\na: "+vowelcount[0]+"\ne: "+vowelcount[1]+"\ni: "+vowelcount[2]+"\no: "+vowelcount[3]+"\nu: "+vowelcount[4])