#And let's unroll the curtains
'''
input("what's your name")
print("hello, world")
'''
#_______________________________________________________________________________________________________________________________________________________________________________________________
'''
return value feature in talk
what will you return if you don't have a feature to hold it ? Presenting you THE VARIABLES *clapclapclappclapclap *heroicentryofvariable
'''
                                         
'''
name= input("what's your name")           #name is the  variable that stores user's input. 
print("hello,")
print(name)                               #return value
'''
#_______________________________________________________________________________________________________________________________________________________________________________________________


                                                #Let's prettify the code above. 

'''
name = input ("what's your name? ")
print("hello, " + name )                  #we can use the '+' operator to concatenate strings</s>
'''
#Eh heh but there's a better way  to do this using a simple "comma(,)"

'''
name = input ("what's your name? ")
print("hello ," , name)


Et voila !! it worked. So how does it make any  difference ?
So basically comma(,) method uses 2 arguments that is hello  and then whatever comes next which is name. It prints them both together separated by space.
Whereas when we used concatenation method (+) , it had two arguments, weird i know  . But here , there is only 1 argument  in the sense that as mathematicians 
going to do what is inside the paranthses first , so if inside thhe paranthses we have "hello" , space and a plus (+) which is not plus but
a concatenation which ultimately turns into one string  with two words separated by a comma, and then what's ultimately passed to the the function 
is print("Ananya"(i.e the name)) which is all being done dynamically.It is all being done dynamically that what it is that concatnates with
Hello wiwth the value of variable name and then passing it ultimately to print as the the solo argument.

'''
#_______________________________________________________________________________________________________________________________________________________________________________________________




                                                        #PARAMETERS AND ARGUMENTS

'''
PARAMETERS : What we can pass in the parantheses and what those i\p are called is Parameters.  
These are two types, Named Parameters(sep, end) ; Positional Parameters  (ip1, ip2).
ARGUMENTS  : When we actually use the function and pass values inside those parantheses , those i\p are called arguments.

#In above examples we saw that output we were receiving was one line after other ,because
Print automatically assumed that we wanted the cursor to the next line after we pass some argument.

Functions take arguments which influence their behaviour.

name = input(" What's your name ?")
print("hello" , end='')      #end parameter tells python not to go to new line after printing something .
print(",",name)             #We can also pass multiple parameters separated by comma.

#There are two special parameters:
#1. End - It specifies what should be printed at last before going to new line. By default it is \n (newline).
#1. End - It tells Python where to put the cursor after printing something.
#2. Separator - It tells Python what should be printed between different parameters passed separately.By Default it prints nothing.
'''
#_______________________________________________________________________________________________________________________________________________________________________________________________



                                                        #F-string format
'''
name=input("What's your name? ")
print(f"Hello {name}!")     #Here f before string is used for using variables inside a string using curly braces {}
'''
#_______________________________________________________________________________________________________________________________________________________________________________________________
    
                                                        #STRING METHODS
'''
name = input("Enter Your Name : ")
name = name.strip( )                     #This method removes any leading or trailing spaces from a string.
name = name.capitalize( )                #This method converts first character of a string into capital letter.
name = name.title(  )                    #This method converts first character of each word to Uppercase & remaining characters to Lower
print(f"Hello,{name}")
'''                                                     
                                                        #CHAINING STRING METHODS
'''
name = input("Enter Your Name : ").strip().title()     #Here strip() remove all the leading & trailing spaces & title() convert first character of each
print(f"Hello, {name}")

'''

#_______________________________________________________________________________________________________________________________________________________________________________________________

                                                        #SPLITTING INTO TWO SMALLER SUBSTRINGS
'''
name = input( " Enter Your Full Name : " )

first , last =name.split(" ")                #By default split() function splits at white space but it takes an optional separator as itsfirst_name , last_name = name.first_name, last_name = name.first_name, last_name = name.first_name , last_name = name. 
print(f"hello , {first}")
'''


#_______________________________________________________________________________________________________________________________________________________________________________________________

                                                        #INTEGERS
'''
Includes numbers from -9999999999 ... to +99999999999 excluding decimals
Can perfom all sort of mathematical operations +,-,/,%


x = int(input("what's x ?"))    #we can nest various functions
y = int(input("What's y?"))
print( x+y )
'''

#_______________________________________________________________________________________________________________________________________________________________________________________________
                                                        
                                                        #FLOATS

'''
All the decimal values are taken care of under this data type

x = float(input("what's x ?"))    
y = float(input("What's y?"))
z = x+y
print(f"{z:,}")


x = float(input("what's x ?"))    
y = float(input("What's y?"))
z = x/y
print(f"{z:.2f}")
'''
#_______________________________________________________________________________________________________________________________________________________________________________________________

                                                    



