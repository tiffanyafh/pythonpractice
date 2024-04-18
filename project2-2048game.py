def summation(num):
    return sum(range(1, num+1))

num = int(input("Enter a positive integer greater than 0: "))
result = summation(num)
print("The summation of every number from 1 to", num, "is", result)