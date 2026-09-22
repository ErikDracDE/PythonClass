s1 = input("Enter any string: ")

sumOfDigits = 0
countOfDigits = 0

for char in s1:
    if char.isdigit():
        sumOfDigits += int(char)
        countOfDigits += 1

if countOfDigits > 0:
    average = sumOfDigits / countOfDigits
else:
    average = 0

print("Sum of the digits in the string is: ", sumOfDigits)
print("Average is: ", average)