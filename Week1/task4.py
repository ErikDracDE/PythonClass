zahl = int(input('Enter number you want to calculate factorial of: '));

result = 1;

for i in range(1, zahl + 1):
    result = result*i;

print("The factorial is: " + str(result))