# Determine whether a provided credit card number is valid
# AMEX - 15 digits long - starts with 34 or 37
# MC -16 digits long - starts with 51, 52, 53, 54 or 55
# VISA - 13 or 16 digit long - starts with 4

def main():
	cardNumber = getNumber()
	if checkSum(cardNumber):
		print(getCompany(cardNumber))
	else:
		print("INVALID")

def getNumber():
	number = input("Number: ")
	while not number.isdigit():
		number = input("Number: ")
	return number

# Check if card number is valid using Luhn's algorithm
def checkSum(cardNumber):
	digit_sum = ""
	checksum = 0

	# Multiply every other digit by 2, starting by second to last
	for i in range(len(cardNumber) - 2, -1, -2):
		digit_sum += str(int(cardNumber[i]) * 2)

	# Sum the digits of the last operation
	for i in digit_sum:
		checksum += int(i)

	# Sum the result of checksum with the digits that weren't read in the first iteration
	for i in range(len(cardNumber) - 1, -1, -2):
		checksum += int(cardNumber[i])

	# Card is valid if checksum ends in 0
	return checksum % 10 == 0

def getCompany(cardNumber):
	length = len(cardNumber)
	if length == 15:
		# must be AMEX
		if cardNumber[:2] == "34" or cardNumber[:2] == "37":
			return "AMEX"
	elif length == 13:
		# must be a VISA
		if cardNumber[0] == "4":
			return "VISA"
	elif length == 16:
		# could be a VISA or a MC
		if cardNumber[0] == "4":
			return "VISA"
		elif int(cardNumber[:2]) > 50 and int(cardNumber[:2]) < 56:
			return "MASTERCARD"
	return "INVALID"

if __name__ == "__main__":
	main()