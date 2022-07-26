# For the following list of numbers:

from cgitb import small


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# Print only even numbers
for n in numbers:
    if n % 2 == 0:
        print(n)
        
numbers.sort()
smallest = numbers[0]
largest = numbers[-1]
difference = largest - smallest
# print(smallest)
# print(largest)
print()
print()

print(f"The difference between the smallest number of {smallest} and the largest number of {largest} is {difference}")