# This fascinating sequence is widely associated with the mathematician Leonardo Pisano
# also known as Fibonacci. He was from the Republic of Pisa, which is why he is also known
# as Leonardo of Pisa. The sequence can be written to print in 2 different ways:
# Iteratively and recursively.

# F(n) = F(n-1) + F(n-2), where n > 1
def PrintFibonacci(length):
    # Initial variable for the base case
    first = 0
    second = 1

    #Printing the initial Fibonacci number.
    print(first, second, end=" ")

    #decreasing the length by two because the first 2 Fibonacci numbers
    # already printed.
    length -= 2

    # Loop until the length becomes 0.
    while length > 0:
        #Printing the next Fibonacci number.
        print(first + second, end=" ")

        #Updating the first and second variables for finding the next number.
        temp = second
        second = first + second
        first = temp

        #Decreasing the length that states the Fibonacci numbers to be
        #printed more.
        length -= 1

if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(7)
    pass