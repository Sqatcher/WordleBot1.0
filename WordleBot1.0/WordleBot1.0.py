# 1) Prepare the words list [words]

words = []
with open("five_letter_words.txt", 'r') as f:
	for line in f:
		word = line.rstrip("\n")
		words.append(word)
	
#print(words[0], words[2555], words[len(words) - 1], end="", sep=".")

# 2) Count the possibilities for each outcome for each word

def printPossibleAnswers():
	for i in range(3):
		for j in range(3):
			for h in range(3):
				for k in range(3):
					for l in range(3):
						print("[", i, ", ", j, ", ", h, ", ", k, ", ", l, "]", sep="", end=",\n")

#printPossibleAnswers()
answers = [[0, 0, 0, 0, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 2],
[0, 0, 0, 1, 0],
[0, 0, 0, 1, 1],
[0, 0, 0, 1, 2],
[0, 0, 0, 2, 0],
[0, 0, 0, 2, 1],
[0, 0, 0, 2, 2],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 1],
[0, 0, 1, 0, 2],
[0, 0, 1, 1, 0],
[0, 0, 1, 1, 1],
[0, 0, 1, 1, 2],
[0, 0, 1, 2, 0],
[0, 0, 1, 2, 1],
[0, 0, 1, 2, 2],
[0, 0, 2, 0, 0],
[0, 0, 2, 0, 1],
[0, 0, 2, 0, 2],
[0, 0, 2, 1, 0],
[0, 0, 2, 1, 1],
[0, 0, 2, 1, 2],
[0, 0, 2, 2, 0],
[0, 0, 2, 2, 1],
[0, 0, 2, 2, 2],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 2],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 1],
[0, 1, 0, 1, 2],
[0, 1, 0, 2, 0],
[0, 1, 0, 2, 1],
[0, 1, 0, 2, 2],
[0, 1, 1, 0, 0],
[0, 1, 1, 0, 1],
[0, 1, 1, 0, 2],
[0, 1, 1, 1, 0],
[0, 1, 1, 1, 1],
[0, 1, 1, 1, 2],
[0, 1, 1, 2, 0],
[0, 1, 1, 2, 1],
[0, 1, 1, 2, 2],
[0, 1, 2, 0, 0],
[0, 1, 2, 0, 1],
[0, 1, 2, 0, 2],
[0, 1, 2, 1, 0],
[0, 1, 2, 1, 1],
[0, 1, 2, 1, 2],
[0, 1, 2, 2, 0],
[0, 1, 2, 2, 1],
[0, 1, 2, 2, 2],
[0, 2, 0, 0, 0],
[0, 2, 0, 0, 1],
[0, 2, 0, 0, 2],
[0, 2, 0, 1, 0],
[0, 2, 0, 1, 1],
[0, 2, 0, 1, 2],
[0, 2, 0, 2, 0],
[0, 2, 0, 2, 1],
[0, 2, 0, 2, 2],
[0, 2, 1, 0, 0],
[0, 2, 1, 0, 1],
[0, 2, 1, 0, 2],
[0, 2, 1, 1, 0],
[0, 2, 1, 1, 1],
[0, 2, 1, 1, 2],
[0, 2, 1, 2, 0],
[0, 2, 1, 2, 1],
[0, 2, 1, 2, 2],
[0, 2, 2, 0, 0],
[0, 2, 2, 0, 1],
[0, 2, 2, 0, 2],
[0, 2, 2, 1, 0],
[0, 2, 2, 1, 1],
[0, 2, 2, 1, 2],
[0, 2, 2, 2, 0],
[0, 2, 2, 2, 1],
[0, 2, 2, 2, 2],
[1, 0, 0, 0, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 2],
[1, 0, 0, 1, 0],
[1, 0, 0, 1, 1],
[1, 0, 0, 1, 2],
[1, 0, 0, 2, 0],
[1, 0, 0, 2, 1],
[1, 0, 0, 2, 2],
[1, 0, 1, 0, 0],
[1, 0, 1, 0, 1],
[1, 0, 1, 0, 2],
[1, 0, 1, 1, 0],
[1, 0, 1, 1, 1],
[1, 0, 1, 1, 2],
[1, 0, 1, 2, 0],
[1, 0, 1, 2, 1],
[1, 0, 1, 2, 2],
[1, 0, 2, 0, 0],
[1, 0, 2, 0, 1],
[1, 0, 2, 0, 2],
[1, 0, 2, 1, 0],
[1, 0, 2, 1, 1],
[1, 0, 2, 1, 2],
[1, 0, 2, 2, 0],
[1, 0, 2, 2, 1],
[1, 0, 2, 2, 2],
[1, 1, 0, 0, 0],
[1, 1, 0, 0, 1],
[1, 1, 0, 0, 2],
[1, 1, 0, 1, 0],
[1, 1, 0, 1, 1],
[1, 1, 0, 1, 2],
[1, 1, 0, 2, 0],
[1, 1, 0, 2, 1],
[1, 1, 0, 2, 2],
[1, 1, 1, 0, 0],
[1, 1, 1, 0, 1],
[1, 1, 1, 0, 2],
[1, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 2],
[1, 1, 1, 2, 0],
[1, 1, 1, 2, 1],
[1, 1, 1, 2, 2],
[1, 1, 2, 0, 0],
[1, 1, 2, 0, 1],
[1, 1, 2, 0, 2],
[1, 1, 2, 1, 0],
[1, 1, 2, 1, 1],
[1, 1, 2, 1, 2],
[1, 1, 2, 2, 0],
[1, 1, 2, 2, 1],
[1, 1, 2, 2, 2],
[1, 2, 0, 0, 0],
[1, 2, 0, 0, 1],
[1, 2, 0, 0, 2],
[1, 2, 0, 1, 0],
[1, 2, 0, 1, 1],
[1, 2, 0, 1, 2],
[1, 2, 0, 2, 0],
[1, 2, 0, 2, 1],
[1, 2, 0, 2, 2],
[1, 2, 1, 0, 0],
[1, 2, 1, 0, 1],
[1, 2, 1, 0, 2],
[1, 2, 1, 1, 0],
[1, 2, 1, 1, 1],
[1, 2, 1, 1, 2],
[1, 2, 1, 2, 0],
[1, 2, 1, 2, 1],
[1, 2, 1, 2, 2],
[1, 2, 2, 0, 0],
[1, 2, 2, 0, 1],
[1, 2, 2, 0, 2],
[1, 2, 2, 1, 0],
[1, 2, 2, 1, 1],
[1, 2, 2, 1, 2],
[1, 2, 2, 2, 0],
[1, 2, 2, 2, 1],
[1, 2, 2, 2, 2],
[2, 0, 0, 0, 0],
[2, 0, 0, 0, 1],
[2, 0, 0, 0, 2],
[2, 0, 0, 1, 0],
[2, 0, 0, 1, 1],
[2, 0, 0, 1, 2],
[2, 0, 0, 2, 0],
[2, 0, 0, 2, 1],
[2, 0, 0, 2, 2],
[2, 0, 1, 0, 0],
[2, 0, 1, 0, 1],
[2, 0, 1, 0, 2],
[2, 0, 1, 1, 0],
[2, 0, 1, 1, 1],
[2, 0, 1, 1, 2],
[2, 0, 1, 2, 0],
[2, 0, 1, 2, 1],
[2, 0, 1, 2, 2],
[2, 0, 2, 0, 0],
[2, 0, 2, 0, 1],
[2, 0, 2, 0, 2],
[2, 0, 2, 1, 0],
[2, 0, 2, 1, 1],
[2, 0, 2, 1, 2],
[2, 0, 2, 2, 0],
[2, 0, 2, 2, 1],
[2, 0, 2, 2, 2],
[2, 1, 0, 0, 0],
[2, 1, 0, 0, 1],
[2, 1, 0, 0, 2],
[2, 1, 0, 1, 0],
[2, 1, 0, 1, 1],
[2, 1, 0, 1, 2],
[2, 1, 0, 2, 0],
[2, 1, 0, 2, 1],
[2, 1, 0, 2, 2],
[2, 1, 1, 0, 0],
[2, 1, 1, 0, 1],
[2, 1, 1, 0, 2],
[2, 1, 1, 1, 0],
[2, 1, 1, 1, 1],
[2, 1, 1, 1, 2],
[2, 1, 1, 2, 0],
[2, 1, 1, 2, 1],
[2, 1, 1, 2, 2],
[2, 1, 2, 0, 0],
[2, 1, 2, 0, 1],
[2, 1, 2, 0, 2],
[2, 1, 2, 1, 0],
[2, 1, 2, 1, 1],
[2, 1, 2, 1, 2],
[2, 1, 2, 2, 0],
[2, 1, 2, 2, 1],
[2, 1, 2, 2, 2],
[2, 2, 0, 0, 0],
[2, 2, 0, 0, 1],
[2, 2, 0, 0, 2],
[2, 2, 0, 1, 0],
[2, 2, 0, 1, 1],
[2, 2, 0, 1, 2],
[2, 2, 0, 2, 0],
[2, 2, 0, 2, 1],
[2, 2, 0, 2, 2],
[2, 2, 1, 0, 0],
[2, 2, 1, 0, 1],
[2, 2, 1, 0, 2],
[2, 2, 1, 1, 0],
[2, 2, 1, 1, 1],
[2, 2, 1, 1, 2],
[2, 2, 1, 2, 0],
[2, 2, 1, 2, 1],
[2, 2, 1, 2, 2],
[2, 2, 2, 0, 0],
[2, 2, 2, 0, 1],
[2, 2, 2, 0, 2],
[2, 2, 2, 1, 0],
[2, 2, 2, 1, 1],
[2, 2, 2, 1, 2],
[2, 2, 2, 2, 0],
[2, 2, 2, 2, 1],
[2, 2, 2, 2, 2]]
# 265 - 23 + 1 = 243
def checkWordv1(ans, word, words):
	wordsSum = 0
	for wordCheck in words:       # for each word
		if word != wordCheck:     # if word is not the same
			pos = -1
			isValid = True
			for j in ans:         # start checking the letters
				pos += 1
				# if black
				if j == 0:
					for wordCheckPos in range(5):
						if wordCheck[wordCheckPos] == word[pos]:   # if a black letter is in the word
							isValid = False
							#print("hah", pos, word)
							break
				# if yellow
				elif j == 1:
					if wordCheck[pos] == word[pos]:						# we dont want the same letter on the same position
						isValid = False
					else:
						isLetterInWord = False
						for wordCheckPos in range(len(wordCheck)):
							if wordCheckPos == pos:						# we dont want the same letter on the same position
								continue
							if wordCheck[wordCheckPos] == word[pos]:    # if a yellow letter is in the word
								isLetterInWord = True
								break
						if isLetterInWord == False:
							isValid = False
				# if green
				elif j == 2:
					if wordCheck[pos] != word[pos]:
						isValid = False
				# after evaluating the colours
				if isValid == False:
					break
			# if isValid after all the answers - add to the valid words
			if isValid:
				wordsSum += 1
	return wordsSum

def checkWord(ans, word, words):
	wordsSum = 0
	for wordCheckWord in words:				# for each word
		if word != wordCheckWord:			# if word is not the same
			wordCheck = []
			for i in range(len(wordCheckWord)):   # create wordCheck as a list
				wordCheck.append(wordCheckWord[i])
			dynamicLetterDictionary = {}
			for letter in wordCheck:	# create the letter dictionary
				if letter in dynamicLetterDictionary:       
					dynamicLetterDictionary[letter] += 1
				else:
					dynamicLetterDictionary[letter] = 1
			isValid = True

			pos = -1
			for j in ans:				# start checking the letters
				pos += 1
			# if green
				if j == 2:
					if wordCheck[pos] != word[pos]:
						isValid = False
					else:
						dynamicLetterDictionary[wordCheck[pos]] -= 1
						wordCheck[pos] = '0'
			# after evaluating the colours
			if isValid == False:
				continue
			pos = -1
			for j in ans:
				pos += 1
				# if yellow
				if j == 1:
					if wordCheck[pos] == word[pos]:						# we dont want the same letter on the same position
						isValid = False
						break
					else:
						isLetterInWord = False
						for wordCheckPos in range(len(wordCheck)):
							if wordCheckPos == pos:						# we dont want the same letter on the same position
								continue
							if wordCheck[wordCheckPos] == word[pos]:    # if a yellow letter is in the word
								isLetterInWord = True
								dynamicLetterDictionary[wordCheck[wordCheckPos]] -= 1
								if dynamicLetterDictionary[wordCheck[wordCheckPos]] < 0:
									isValid = False
								wordCheck[wordCheckPos] = '0'
								break
						if isLetterInWord == False:
							isValid = False
			# after evaluating the colours
			if isValid == False:
				continue
			pos = -1
			for j in ans:				# start checking the letters
				pos += 1
				# if black
				if j == 0:
					if word[pos] in dynamicLetterDictionary:
						if dynamicLetterDictionary[word[pos]] != 0:
							isValid = False
							#print(ans, word, wordCheck, wordCheckWord, pos)
							break
				
			# after evaluating the colours
			if isValid == False:
				continue
			# if isValid after all the answers - add to the valid words
			if isValid:
				wordsSum += 1
	return wordsSum

#words = ["aabbc", "aabbd", "aabba"]

resultFileName = "results.txt"
results = {}
wordNum = 0
with open(resultFileName, 'w') as f1:  # clear file
	pass
for word in words:
	wordNum += 1
	results[word] = []
	for i in range(len(answers)):
		results[word].append(checkWord(answers[i], word, words))
		percent = wordNum*100/len(words)
	print("Checking words... currently at %.2f%%" % percent)
	with open(resultFileName, 'a') as f:
		for i in range(len(answers)):
			line = str(i+1) + ':' + str(word) + ':' + str(results[word][i])
			f.write(line)
			f.write("\n")
"""
for word in words:
	letters = {}
	for letter in word:
		letters[letter] = 1
	suma = 0
	for key in letters:
		suma += 1
	if suma < 3:
		print(word)
"""		