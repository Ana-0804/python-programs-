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

x = int(input("what's x?"))
y = int(input("what's y? "))

if x>y or y>x:  #this means if either of the conditions in () is true then it will execute this block.
    print ("values are not equal")
else:
    print("both are equal")