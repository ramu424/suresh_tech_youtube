"""marks=[50,'ram',85]
print(type(marks))
friends=["raj","mitt","Bittu"]
print(friends)
dislikers=[]
print(len(dislikers))
biodata=[29,"999999","27.7777",friends]
print(biodata)
print(biodata[3][1])
marks[1]=55
print(marks)
"Concatanenation"
print(marks + friends)
"Repetation"
print(marks * 2)
friends.append("robinHood")
print(friends)
friends.extend(["Rami reddy","Bhanu"])
print(friends)
friends.insert(1,"Hareesh")
print(friends)
friends[1:4]=["sam","gam"]
print(friends)
friends.remove('Bhanu')
print(friends)
friends.pop(0)
print(friends)"""
from tkinter.font import names

'''marks=(20,80,"tyoe")
print(type(marks))
friends=("sam","peter","john")
print(friends)
print(marks[0])
print(friends[0])'''
'''print('=====DICTIONARY======')
has={"channel":2,"Subscrition":True,"info":{"Name":"Sarangapani","Age":32,"College":"mit"}}
print(has)
print(type(has))
print("printing channel name:", has["channel"])
print("Channel owner is:",has["info"]["Name"])'''
'''print("===DICTIONARY EXERCISE====")
D1={12:{"CLASS":"B.COM","PERCENTAGE":70},14:{"CLASS":"B.COM","PERCENTAGE":60},15:{"CLASS":"B.COM","PERCENTAGE":80},13:{"CLASS":"B.COM","PERCENTAGE":50}}
rollnumber=int(input("Enter your Roll Number: "))
percentage=D1[rollnumber]["PERCENTAGE"]
if percentage > 40:
    print("passed")
else:
    print("failed")'''
'''number=int(input("Enter your Number: "))
if (number%2==0):
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")'''
'''range(0,10,1)
print(range(0,10,1))
print(range(10))'''

'''numbers=range(0,11,1)

for i in numbers:
    print(i*8)'''

'''name=input("Enter your Name: ")

for character in name:
    print(character)'''

'''name=input("Enter Your Name: ")
#print(name[-2:])
l2=name[-2:]
for i in range(1,11):
    print(i*l2)'''
'''for iterating over list'''

'''friends=["sam","bandari","kansai"]
for i in friends:
    print(i)'''
#Iterating over Dictionary

'''stand={1:'ram',2:'sam',3:'man'}

for i in stand:
    print(i)
    print("Key value pair is", stand[i])'''
#Find vowels and consonant in your name:

'''name=input("Enter your Name: ")
print(f"Your name is '{name}' and we are finding vowels and consonants in your Name below")
vowelslist=["a","e","i","o","u"]
for i in name:
    if i in vowelslist:
        print(i,'It is vowel')
    else:
        print(i,"it is consonant")'''
#Find your name has vowel in your name

name=input("Enter your Name: ")
print(f"Finding your '{name}' is vowel is present or not")
vowelslist=["a","e","i","o","u"]
for i in name:
    if i in vowelslist:
        print(i,'vowel is present')

