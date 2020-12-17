# Programming Task 1
# Author: Stuart Hanson
# Date: 04/12/2020
# Contact: stuart_hanson@outlook.com

# Set up a try catch to reject invalid inputs
# Collect input about the main library branches
while True:
    try:
        branches = int(input("Enter the number of branches of the main library: "))
    except ValueError:
        print("Number of branches must be an integer")
        continue
    if branches < 1:
        print("Number of branches must be at least 1")
    else:
        break

# Initialize the count to 0 for the loops below.
# Initialize the list on each run to get clean data
count = 0
bookCount = []

# Set up a function with a try / catch to reject invalid inputs
def getInput(categories, count):
    count += 1
    while True:
        try:
            value = int(input('{} {} : '.format(categories, count)))
        except ValueError:
            print("Number of books must be an integer")
            continue
        if value < 0:
            print("Number of books must be non-negative")
        else:
            return value

# Iterate through the loop and add each set of inputs to a list
# This list will allow multiple enties under the same variable name
for count in range(branches):
    bookCount.append(getInput("Enter the number of books for computer of branch", count))
    bookCount.append(getInput("Enter the number of books for physics of branch", count))
    bookCount.append(getInput("Enter the number of books for chemistry of branch", count))
    bookCount.append(getInput("Enter the number of books for biology of branch", count))
    bookCount.append(getInput("Enter the number of books for arts of branch", count))


# Collect the total number of books entered
totalBooks = sum(bookCount)

# Average out the number of books
def average(bookCount):
    return sum(bookCount) / 5

# Show collected stats
# Format average output to always show 2 decimal places

print("\n""Following the information of all the branches of the main library: ")
print("Total number of books:", totalBooks)
print("Average numbers of books per category: "'{:.2f}'.format(average(bookCount)))
