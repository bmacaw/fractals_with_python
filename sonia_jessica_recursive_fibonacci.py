# Recursive Algorithm for printing the Fibonacci Sequence
# Accept the value of the previous first and second Fibonacci number as the
# length to be printed; check if the length is 0 then terminate the function call';
# print the Fibonacci value by adding the previous 2 values received in the
# parameter of the function (first and second); recursively call the function for
# # the updated value of the first and second, as well as the decreased value of
# length.

def PrintFibonacci(first, second, length):

    #Stop the printiing and recursive calling if length reaches the end.
    if(length == 0):
        return

    #Printing the next Fibonacci number.
    print(first + second, end=" ")

    #Recursively calling the function by updating the value and
    #decrementing the length.
    PrintFibonacci(second, first+second, length-1)

if __name__ == "__main__":
    #Print initial 2 values.
    print(0,1,end=" ")

    #Calling the Function to print the remaining length
    #fibonacci series
    #PrintFibonacci(0,1,7-2)
    PrintFibonacci(0,1,11-2)

#nothing,oursun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto
#0 1 1 2 3 5 8 13 21 34 55 (dimensions); earth = 3 (3rd dimension), mars = 5 :)...?

