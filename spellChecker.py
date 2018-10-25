

import stdarray
import stdio
import readWords as rw
import edit_distance as ed
import multiprocessing

path= "C:\Users\cheta\Desktop\Aniket\Spell_Suggestion\english_words.txt"

	


def chunkList(myWord,chunkSize):
	chunkSize=len(myWord)//chunkSize
	return [myWord[i:i + chunkSize] for i in range(0, len(myWord), chunkSize)]
	
def spellChecker(listWords):
	minDistance=999999
	for word in listWords:
		distance=ed.dynamicSolution(word,myword)
		if distance< minDistance:
			suggestion=word
			minDistance=distance
	return suggestion

listOfWords= rw.readFileAsList(path)
myword="hypercola"
print "hi"
if __name__== '__main__':
	#print spellChecker(listOfWords)
	
	pool=multiprocessing.Pool()
	
	resultList= pool.map(spellChecker,chunkList(listOfWords,500))
	
	print "Correct spell is",spellChecker(resultList)
	
	
	#print "Suggestion is",suggestion
