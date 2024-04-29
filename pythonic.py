'''
In the programming world, there are types of programming that are called “Pythonic” in nature. 
That is, there are ways to program that are sometimes only seen in Python programming. 
'''

def main():
    x=int(input("enter x "))
    if is_even(x):
        print("even")
    else:
        print("odd")
            
#A function named 'is_even' is defined below which checks whether a number is even or not. 
def is_even(n):
    return True if n % 2 == 0 else  False


main()

