import json

jsonfile = open("bibletopics.json", "r")

topic = json.load(jsonfile)
jsonfile.close()
topicinput = input("topic: " )
newVerses = []

def addVerse(inputBook, inputChapter, inputVerse):
	verseDic = {"book" : inputBook.capitalize(), "chapter" :
	inputChapter, "verse": inputVerse}
	newVerses.append(verseDic)
	topic[topicinput] = newVerses
	print(topic)
	outfile = open("bibletopics.json", "w")
	json.dump(topic, outfile)
	outfile.close()
try:
	newVerses = topic[topicinput]
except:
	topic[topicinput] = newVerses
while True:
	inputBook = input("book: ")
	if inputBook=="exit":
		break
	inputChapter = int(input("chapter: "))
	inputVerse = input("verse : ")
	start = 0
	end = 0
	if "-" in str(inputVerse):
		split = inputVerse.split("-")
		start = int(split[0])
		end = int(split[1])
		for x in range(start, end+1):
			addVerse(inputBook, inputChapter, x)
	else:
		addVerse(inputBook, inputChapter, int(inputVerse))
	