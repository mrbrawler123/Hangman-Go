import nltk
import time
nltk.download("words")
nltk.download("wordnet")
print("\033[2J\033[H")
def find_letters(letter, word):
  index = []
  for i in range(len(word)):
    if letter == word[i]:
      index.append(i)
    if letter != word[i]:
      continue
  return index
time.sleep(1)
print("HANGMAN GO")
time.sleep(3)
import random
print("I will think of a word. You have to guess it.")
time.sleep(2)
from nltk.corpus import words
from nltk.corpus import wordnet
words_list = words.words() + list(wordnet.words())
while True:
	word = random.choice(words_list)
	word = word.lower()
	print(f"You have {len(word) + 5} chances.")
	answer = ["_ "] * len(word)
	time.sleep(3)
	used = []
	tries = 0
	separator = ""
	correct = 0
	separator2 = ", "
	final_answer = separator.join(answer)
	while tries != len(word) + 5:
		print(f"This is your current status: {final_answer}")
		time.sleep(1)
		s = input("Guess a letter or a word: ")
		s = s.lower()
		time.sleep(1)
		if s in used:
			print("You have already guessed this letter. Try again!")
			continue
		else:
			used.append(s)
		used.sort()
		used_final = separator2.join(used)
		if len(s) > 1 and s == word:
			print(f"Congratulations! You guessed the word in {tries} chances!")
			break
		if len(s) == 1 and word.count(s) > 0:
			for a in find_letters(s,word):
				answer[a] = s
				correct = correct + 1
			print(f"Yay! You guessed correctly!")
			if correct == len(word):
				print(f"Congratulations! You guessed the word in {tries} chances!")
				break
			if tries == len(word) + 5:
				print(f"You have lost! The word was {word}!")
			print(f"You have {len(word) + 5 - tries} chances remaining. You have used: {used_final}")
		if word.count(s) == 0:
			tries = tries + 1  
			print(f"You guessed wrong!")
			if correct == len(word):
				print(f"Congratulations! You guessed the word in {tries} chances!")
				break
			if tries == len(word) + 5:
				print(f"You have lost! The word was {word}!")
			print(f"You have {len(word) + 5 - tries} chances remaining. You have used: {used_final}")  
		final_answer = separator.join(answer)