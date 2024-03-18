
'''
input("what's your name")
print("hello, world")
'''
'''
return value feature in talk
what will you return if you don't have a feature to hold it ? Presenting you THE VARIABLES *clapclapclappclapclap *heroicentryofvariable
'''
'''
name= input("what's your name") #name is the  variable that stores user's input. 
print("hello,")
print(name)                     #return value
'''

#next comes PSEUDO CODE , it'sbasically structuring  of code without actual implementation breaking bigger  tasks into smaller ones.
#Let's prettify the code above. 
'''
name = input ("what's your name? ")
print("hello, " + name )   #we can use the '+' operator to concatenate strings</s>
'''

#Eh heh but there's a better way  to do this using a simple "comma(,)"

name = input ("what's your name? ")
print("hello ," , name)

'''
Et voila !! it worked. So how does it make any  difference ?
So basically comma(,) method uses 2 arguments that is hello  and then whatever comes next which is name. It prints them both together separated by space.
Whereas when we used concatenation method (+) , it had two arguments, weird i know  . But here , there is only 1 argument  in the sense that as mathematicians 
going to do what is inside the paranthses first , so if inside thhe paranthses we have "hello" , space and a plus (+) which is not plus but
a concatenation which ultimately turns into one string  with two words separated by a comma, and then what's ultimately passed to the the function 
is print("Ananya"(i.e the name)) which is all being done dynamically.It is all being done dynamically that what it is that concatnates with
Hello wiwth the value of variable name and then passing it ultimately to print as the the solo argument.

'''