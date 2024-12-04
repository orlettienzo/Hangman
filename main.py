#Jodo da Forca em Python
import random

#1 - lista com as palavras possíveis
filename = "dictionary.txt"
with open(filename, 'r') as file:
    lines = file.readlines()

words = []
for line in lines:
    line = line.strip().lower().replace("\n", "")
    words.append(line)

#print(words)

#2- escolha da palavra secreta
index = random.randint(0, len(words) - 1)
secret_word = words[index]
#print(secret_word)

#3 stockar em uma lista
l=[]
for letter in secret_word:
    l.append(letter)
#print(l)

l_copie = [ "_" for element in l]
#print(l_copie)



#4- limite de tentativas
limite = len(secret_word) + 5

#5- começo do jogo
chutes = 0
while chutes < limite:

    goal = ""
    for element in l_copie:
        goal = goal + element

    if "_" in goal:
        print(goal)

    a = input("Enter a letter: ")
    if a in l:
        for index, element in enumerate(l):
            if element == a:
                l_copie[index] = a
                #print(goal)
                chutes += 1
                if "_" not in l_copie:
                    print("="*35)
                    print("## YOU WON ##")
                    print()
                    print(f"The word was {secret_word}")
                    print("=" * 35)
                    break
                print("You still have " + str(limite - chutes) + " chance(s)")
    else:
        chutes += 1
        if limite - chutes == 0:
            print("="*35)
            print("## YOU LOST ##")
            print()
            print(f"The word was {secret_word}")
            print("=" * 35)

        else:
            print("You still have " + str(limite - chutes) + " chance(s)")



