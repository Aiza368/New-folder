# -Simple Message
name:str= "Aiza"
print(name)
# -Simple Messages
# Assign a message to a variable and print that message
a="hy"
print(a)
# Change the value of the variable to a new message, and print the new message.
a="hello"
print(a)
#  Personal Message
# Use a variable to represent a person’s name
N:str="Fahad" # type: ignore
print(N)
# Print a message to that person
print(f"Hey {N} how's your job going")
# Name Cases
# Use a variable to represent a person’s name
j:str="mArIa"
#Print the person’s name in lowercase
print(j.lower())
# uppercase
print(j.upper())
# title case
print(j.title())
# Famous Quote
P:str="Franklin D. Roosevelt" 
Q:str="The only thing we have to fear is fear itself"
# Print the quote and the name of its author
print(f'{P} once said, "{Q}" ')
# Famous Quote 2
# variable called famous_person to represent the famous person’s name
famous_person:str="Ralph Waldo Emerson"
#Compose the message and represent it with a variable called message
message:str="""To be yourself in a world that is constantly 
           trying to make you something else is the 
           greatest accomplishment."""
# Print the message
print(f'{famous_person} once said, "{message}"')
# Stripping Names
# person’s name, and include some whitespace characters at the beginning and end of the name
k:str="   Franklin D. Roosevelt    "
#  character combination, \t and \n, at least once
l="Franklin \t D. \n Roosevelt"
print(l)
#Print the name
print(k)
#  lstrip()
print(k.lstrip())
# rstrip()
print(k.rstrip())
# strip()
print(k.strip())
# Variable Sum
# Assign the values 5, 10, and 15 to three variables x, y, and z
x:int=5
y:int=10
z:int=15
# Print their sum
sum=x+y+z
print(sum)
# Swap the values of two variables a and b. Print the values before and after the swap
f:int=2
g:int=3
#before swap
print(f"before swap f={f} and g={g}")
#swap
f=f+g
g=f-g
f=f-g
#after swap
print(f"after swap f={f} and g={g}")
#Favorite Color
#Create a variable with your favorite color and print it 
color="blue"
print(f"my favorite color is : {color}")
# change the variable name to something else and print the color again
newcolor=color
print(newcolor)
#Changing Pet Name
#  Create a variable pet_name and set it to "Buddy".
#Change the value of pet_name to"Max" and print the new value.
pet_Name="Buddy"
pet_Name="Max"
print(pet_Name)
# Assign the value "Sunshine" to a variable and print it. 
# Then, mistakenly try to print a variable with a different name (like sunsine) and observe the error.
Sunshine:str="wow"
print(Sunshine)

#NameError: name 'sunsine' is not defined

# Reassigning Score
# Assign the value 100 to a variable score and print it
score=100
print(score)
#assign a new value to score and print it again.
score=80
print(score)
# City Name
#Create a string variable city and assign it the name of a city you like. 
#Print the city name.
city:str="Lahore"
print(city)
#Title Case Text
# Create a variable text with the value "python programming" and print it in title case
i:str="python programming"
print(i.title())
#  Lowercase Conversion
# Assign a string with mixed cases to a variable and print it in all lowercase letters
p:str= "RahEEl"
print(p.lower())
# Uppercase
# Assign a string with mixed cases to a variable and print it in all uppercase letters
r:str= "RahEEl"
print(r.upper())
# Current Temperature
#  Create a variable temperature with the value 25. 
# Print "The current temperature is [temperature] degrees." using the variable.
temperature:int=25
print(f'"The current temperature is, {temperature} degrees "')
# Printing a Poem
#Create a variable poem with a short poem that has multiple lines. 
# Print the poem with each line starting on a new line.
poem:str="""As morning light begins to play,
The night last shadows fade away.
A soft, new hope stirs in the sky,
A promise in the sun first cry."""
print(poem)



