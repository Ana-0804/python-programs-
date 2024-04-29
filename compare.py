'''
x = int(input("what's x?"))
y = int(input("what's y? "))

if x>y:
    print("Y is smaller")
elif x<y:
    print("Xis smaller than y")
elif x==y:
    print("Both are equal")
    '''

                                                #OR
'''
x = int(input("what's x?"))
y = int(input("what's y? "))

if x>y or y>x:  #this means if either of the conditions in () is true then it will execute this block.
    print ("values are not equal")
else:
    print("both are equal")
    '''

                                                #NOTEQUAL
'''
x = int(input("what's x?"))
y = int(input("what's y? "))
if x!=y :   #not equal to '!=' operator
    print("Values are not equal")
else:
    print("Values are equal")
    '''
                                                #EQUALEQUAL
'''
x = int(input("what's x?"))
y = int(input("what's y? "))
if x==y :   #EQUAL equal to '==' operator
    print("Values are  equal")
else:
    print("Values are not equal")
    '''

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()