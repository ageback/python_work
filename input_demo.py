# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# name = input("Please enter your name: ")
# print(f'\nHello, {name}')

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
