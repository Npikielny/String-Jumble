"""
stringjumble.py
Author: Noah Pikielny
Credit: None

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
I = str(input("Please enter a string of text (the bigger the better): "))
print("You entered " + '"' + I + '". Now jumble it:')
letters = []
words = []
index = 0
newWord = 1
for i in I:
    if i != " " and newWord == 0:
        words[index] += i
    elif newWord == 1:
        words.append(i)
        newWord = 0
    else:
        newWord = 1
        index += 1
    letters.append(i)
    
print(letters[len(letters)::-1])
print(words[len(words)::-1])

index = 0 
newWord = 1
words2 = []
for i in words:
    l = list(i)
    words2.append(l[len(l)::-1])
print(words2)