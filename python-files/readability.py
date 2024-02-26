# program outputs reading grade level of text using Coleman-Liau index
# Coleman-Liau index: is computed as 0.0588 * L - 0.296 * S - 15.8
# L is the average number of letters per 100 words in the text
# S is the average number of sentences per 100 words in the text
from cs50 import get_string
import re
import sys

# asks the user to type in some text
# outputs the grade level for the text
#  according to the Coleman-Liau formula


# get user input
text = get_string("Text: ")

# count the number of letters, words, and sentences in the text
letters = 0
words = 1
sentences = 0

text_length = len(text)
# print("text length: ", text_length)

# letter - any lowercase character from a to z or any uppercase character from A to Z
# word - any sequence of characters separated by spaces
for i in range(len(text)):
    if text[i].isalpha():
        letters += 1

# print("letters:", letters)

# punctuation
punc = ".!?"
punc_total = [text.count(c) for c in punc]
# sentence - characacters followed by any occurrence of a period, exclamation point, or question mark
sentences = sum(punc_total)
# print("sentences: ", sentences)

words += text.count(' ')
# print("words: ", words)

L = (letters / words) * 100
S = (sentences / words) * 100

# print("L: ", L)
# print("S: ", S)

# compute Coleman-Liau index
index = .0588 * L - 0.296 * S - 15.8
# print("index: ", index)
grade = round(index)
# print("grade: ", grade)

# print as output "Grade X"
# where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer
# If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level)
# program should output "Grade 16+"
# If the index number is less than 1
# your program should output "Before Grade 1"
# output grade level

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print(" Grade 16+")
else:
    print("Grade ", grade)