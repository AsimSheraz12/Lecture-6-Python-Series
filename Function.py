# Practice Question 1
numbers = [1, 2, 3, 4, 5, 6]

def findLength(num):
    return len(num)

def printElemant(num):
    for val in num:
        print(val)


length = findLength(numbers)


# print(length)

# printElemant(numbers)

def factorial(num1):
    result = 1
    for val in range(num1, 0, -1):
        result *= val
    return result

fact = factorial(5)

print(fact)

def currencyConvert(num2):
    print(f"Your Entered Price in {num2}$ is = in Pakistani {num2*278.00} rupee")

amount = int(input("Enter Your Amount in Dollars You Convert it"))

currencyConvert(amount)