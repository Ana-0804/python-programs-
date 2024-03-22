'''
If and when you want to define, invent, create your own function yu use #def keyword'''

def hello( to):
    print("hello" , to)

name = input("What's your name ? ")
hello(name)


#Here, in the first lines, we are creating our hello function. 
#This time, however, we are telling the compiler that this function takes a single parameter: a variable called "to". 
#Therefore, when we call hello(name) the computer passes name into the hello function as to. 
#This is how we pass values into functions.
