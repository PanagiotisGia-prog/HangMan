import random

print("----------------------------------------------------------")
print("| WELCOME TO THE HANGMAN GAME - GAMING CONSOLES EDITION! |")
print("----------------------------------------------------------")

hp = 6
words = ["PLAYSTATION", "GAMEBOY", "ATARI", "GAMECUBE", "GENESIS", "XBOX", "NES", "SNES", "SWITCH", "WII"]
underscores = []
selected_word = random.choice(words)
used_words = []

for word in selected_word:
    underscores.append("_") 

underscore = "".join(underscores)

print(underscore)
print(f"You have {hp} lives!")

while True:
    counter = 0
    user = input("Guess a word: ").upper()

    if len(user) > 1:
        print("Enter only one word each turn!")
        continue

    if used_words.count(user):
        print("You've already used that word!")
        continue

    for i in range(len(selected_word)):
        if user == selected_word[i]:
            underscores[i] = selected_word[i]
            underscores.pop(i)
            underscores.insert(i, user)
            used_words.append(user)
            counter += 1
    
    if counter < 1:
        hp -= 1
        used_words.append(user)

    guessed_word = "".join(underscores)

    if guessed_word == selected_word:
        print(guessed_word)
        break
    elif hp == 0:
        break
    else:
        print(guessed_word)
        print(f"You have {hp} lives!")
        print(f"Words that you used: {used_words}")
        continue

if hp == 0:
    print(f"You lose! The word was: {selected_word}")
else:
    print("Congratulations! You Win!")

