# Validates credit card number using Luhn's algorithm
from cs50 import get_string
# prompt user for ccn
ccn = get_string("Number: ")

# add the digits of the products together (not products themselves)
# return the sum
even_sum = 0
edigit = 0
# Add the digits not multiplied by 2
# return the sum
odd_sum = 0
odigit = 0

# get all of the even digits starting w/2nd to last digit
# slicing string w/stride of 2. this keeps the whole string w/in
# range, and skips 2 chars from the end
# returns a list of strings
# multiply every other digit by 2
# get a list of the odd digits
# iterate through the odd digits and return the sum
# add the odd and even digits
# return the sum
odigit = int(ccn[-1::-2])
odd_sum += odigit

edigit = int(ccn[-2::-2])
if edigit > 9:
	edigit = (edigit - 9)
	even_sum += edigit

tot_digits = odd_sum + even_sum

# validate credit card
# check the credit card length
ccnLength = len(ccn)
# get the first and second digits
first_digit = ccn[0]
second_digit = ccn[1]
valid_card = tot_digits % 10 == 0

card = ""

if ccnLength >= 13 and ccnLength <= 16:
	if first_digit == "3" and second_digit == "4" or second_digit == "7":
		card = "AMEX"
	elif first_digit == "4":
		card = "VISA"
	elif first_digit == "5" and second_digit == "1" or second_digit >= "1" or second_digit <= "5":
		card = "MASTERCARD"
else:
	card = "INVALID"

# check card # and print card
if valid_card and card == True:
	print(card)
else:
	print(card)

 # test: 378282246310005
