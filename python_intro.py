print("Hello, Django girls!")

if 2>3:
    print("It works!")
else:
    print("5 n'est pas plus grand que 2")
name="Astrid"
if name=="Astrid":
    print("Hey Ola!")
elif name=="Sonja":
    print("Hey Sonja")
else:
    print("Hey anonymous!")



volume=25
if volume <20 and volume==14:
    print("C'est plutôt calme.")
elif 20<= volume and volume < 40:
    print("Une jolie musique de fond.")
elif 40<=volume < 60:
    print("Parfait, je peux entendre.")
elif 60 <= volume < 80:
    print("Un peu trop fort !")
else:
    print("Au secours! Mes oreilles!:(")


def hi():
    print("Hi there!")
    print("How are you?")

hi()

def hi(name):
    print("Hi " + name+ "!")


hi("Astrid")


def hi(name):

    print("Hi "+ name +"!")
    for i in range (1,6):
        print(i)
hi("ola")
