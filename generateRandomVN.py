#!/usr/bin/env python

import string
import sys
from random import Random
random=Random()
gameName=sys.argv[1]

SCENE_COUNT=50
CHARACTER_COUNT=10

moods = ["happy", "sad", "surprised", "normal", "angry"]
adjectives = ["Happy", "Sad", "Surprised", "Normal", "Angry", "Vicious", "Intelligent", "Carnal", "Torpid", "Squamous", "Rugose", "Turgid", "Wild", "Wonderful", "Worldly", "Forced", "Creamy", "Crunchy", "Chewy", "Red", "Blue", "Green", "Orange", "Yellow", "Indigo", "Violet", "Black", "White", "Lupine", "Lapine", "Feline", "Corvine", "Fortunate", "New", "Old", "Illuminated", "Ancient", "Bavarian", "Wet", "Bad"]
nouns = ["Tentacle", "Center", "Stallion", "Coating", "Son", "Daughter", "Father", "Mother", "Sister", "Brother", "Uncle", "Aunt", "Pet", "Cemetary", "Mausoleum", "Equation", "Drug", "Day", "Week", "Month", "Name", "Lexicography", "Order", "Cream", "Sprocket", "Toad", "Medicine", "Fever", "Cat", "Dog", "Wolf", "Bird", "Crow", "Raven", "Jackdaw", "Corvid", "Storm", "Wind", "Warp", "Mountain", "Sugar", "Rock"]
firstNames = ["Jacob","Michael","Joshua","Matthew","Daniel","Christopher","Andrew","Ethan","Joseph","William","Anthony","David","Alexander","Nicholas","Ryan","Tyler","James","John","Jonathan","Noah","Brandon","Christian","Dylan","Samuel","Benjamin","Nathan","Zachary","Logan","Justin","Gabriel","Jose","Austin","Kevin","Elijah","Caleb","Robert","Thomas","Jordan","Cameron","Jack","Hunter","Jackson","Angel","Isaiah","Evan","Isaac","Luke","Mason","Jason","Jayden","Gavin","Aaron","Connor","Aiden","Aidan","Kyle","Juan","Charles","Luis","Adam","Lucas","Brian","Eric","Adrian","Nathaniel","Sean","Alex","Carlos","Ian","Bryan","Owen","Jesus","Landon","Julian","Chase","Cole","Diego","Jeremiah","Steven","Sebastian","Xavier","Timothy","Carter","Wyatt","Brayden","Blake","Hayden","Devin","Cody","Richard","Seth","Dominic","Jaden","Antonio","Miguel","Liam","Patrick","Carson","Jesse","Tristan","Alejandro","Henry","Victor","Trevor","Bryce","Jake","Riley","Colin","Jared","Jeremy","Mark","Caden","Garrett","Parker","Marcus","Vincent","Kaleb","Kaden","Brady","Colton","Kenneth","Joel","Oscar","Josiah","Jorge","Cooper","Ashton","Tanner","Eduardo","Paul","Edward","Ivan","Preston","Maxwell","Alan","Levi","Stephen","Grant","Nicolas","Omar","Dakota","Alexis","George","Collin","Eli","Spencer","Gage","Max","Cristian","Ricardo","Derek","Micah","Brody","Francisco","Nolan","Ayden","Dalton","Shane","Peter","Damian","Jeffrey","Brendan","Travis","Fernando","Peyton","Conner","Andres","Javier","Giovanni","Shawn","Braden","Jonah","Bradley","Cesar","Emmanuel","Manuel","Edgar","Mario","Erik","Edwin","Johnathan","Devon","Erick","Wesley","Oliver","Trenton","Hector","Malachi","Jalen","Raymond","Gregory","Abraham","Elias","Leonardo","Sergio","Donovan","Colby","Marco","Bryson","Martin","Emily","Madison","Emma","Olivia","Hannah","Abigail","Isabella","Samantha","Elizabeth","Ashley","Alexis","Sarah","Sophia","Alyssa","Grace","Ava","Taylor","Brianna","Lauren","Chloe","Natalie","Kayla","Jessica","Anna","Victoria","Mia","Hailey","Sydney","Jasmine","Julia","Morgan","Destiny","Rachel","Ella","Kaitlyn","Megan","Katherine","Savannah","Jennifer","Alexandra","Allison","Haley","Maria","Kaylee","Lily","Makayla","Brooke","Nicole","Mackenzie","Addison","Stephanie","Lillian","Andrea","Zoe","Faith","Kimberly","Madeline","Alexa","Katelyn","Gabriella","Gabrielle","Trinity","Amanda","Kylie","Mary","Paige","Riley","Leah","Jenna","Sara","Rebecca","Michelle","Sofia","Vanessa","Jordan","Angelina","Caroline","Avery","Audrey","Evelyn","Maya","Claire","Autumn","Jocelyn","Ariana","Nevaeh","Arianna","Jada","Bailey","Brooklyn","Aaliyah","Amber","Isabel","Mariah","Danielle","Melanie","Sierra","Erin","Molly","Amelia","Isabelle","Madelyn","Melissa","Jacqueline","Marissa","Shelby","Angela","Leslie","Katie","Jade","Catherine","Diana","Aubrey","Mya","Amy","Briana","Sophie","Gabriela","Breanna","Gianna","Kennedy","Gracie","Peyton","Adriana","Christina","Courtney","Daniela","Lydia","Kathryn","Valeria","Layla","Alexandria","Natalia","Angel","Laura","Charlotte","Margaret","Cheyenne","Mikayla","Miranda","Naomi","Kelsey","Payton","Ana","Alicia","Jillian","Daisy","Mckenzie","Ashlyn","Sabrina","Caitlin","Summer","Ruby","Rylee","Valerie","Skylar","Lindsey","Kelly","Genesis","Zoey","Eva","Sadie","Alexia","Cassidy","Kylee","Kendall","Jordyn","Kate","Jayla","Karen","Tiffany","Cassandra","Juliana","Reagan","Caitlyn","Giselle","Serenity","Alondra","Lucy","Bianca","Kiara","Crystal","Erica","Angelica","Hope","Chelsea","Alana","Liliana","Brittany","Camila","Makenzie","Lilly","Veronica","Abby","Jazmin","Adrianna","Delaney","Karina","Ellie","Jasmin"]

lastNames = ["Chekhov","Dostoyevsky","Gaunt","Goethe","Gogol","Gorky","Hesse","Pushkin","Sacher-Masoch","Tolstoy","Turgenev","Waldau","Wylie","Ainsworth","Austen","Bennett","Brontë","Brontë","Burney","Carlyle","Carroll","Collins","Conrad","Dickens","Disraeli","Eliot","Gissing","Godwin","Hudson","James","Kipling","Maugham","Oliphant","Radcliffe","Scott","Shelley","Shelley","Stevenson","Thackeray","Trollope","Adams","Adams","Aiken","Alcott","Bellamy","Brackenridge","Brown","Chesnutt","Chopin","Cooper","Crane","Davis","Dreiser","Dunbar","Fern","Hawthorne","Hopkins","Howells","James","Jewett","Lippard","Longfellow","Melville","Norris","Page","Poe","Sinclair","Sleeper","Smith","Stowe","Sturgis","Tarkington","Twain","Wharton","Wister","Abbey","Achebe","Acker","Ackerman","Adams","Agee","Aiken","Albee","Alexie","Algren","Allen","Allende","Alvarez","Amis","Andrews","Angelou","Apollinaire","Aragon","Arendt","Artaud","Asch","Ashbery","Asimov","Atwood","Auden","Auel","Auster","Ballard","Banks","Baraka","Barnes","Barrie","Barth","Barthelme","Barthes","Bataille","Baum","Beckett","Beerbohm","Bellow","Benchley","Bergson","Bester","Blanchot","Bloom","Blume","Bolaño","Borges","Bowles","Bradbury","Brautigan","Brecht","Breton","Brodsky","Bukowski","Bulgakov","Burroughs","Burroughs","Byatt","Calvino","Campbell","Camus","Capote","Card","Carroll","Carver","Cather","Céline","Cheever","Cherryh","Chesterton","Chomsky","Clancy","Clarke","Clark","Cocteau","Coetzee","Cohen","Collins","Conrad","Conroy","Coover","Cornwell","Cortázar","Coupland","Coward","Crane","Creeley","Crichton","Cronin","Cummings","Cunningham","Cussler","Dahl","Danticat","Davis","Delany","deBeauvoir","deSaint-Exupéry","DeLillo","Dick","Dickey","Didion","Dillard","Doctorow","Doolittle","Dorris","DosPassos","Douglass","Doyle","Dreiser","Drury","DuBois","Dufresne","DuMaurier","Dürrenmatt","Dunwich","Durkheim","Durrell","Dylan","Ebert","Eco","Eddings","Eliot","EastonEllis","Ellison","Ellroy","Éluard","Ephron","Epstein","Erdrich","Faulkner","Ferlinghetti","Fielding","Finney","Fitzgerald","Fleming","Follett","MadoxFord","Ford","Forester","Forster","Forsyth","Foucault","Fowler","Fowles","Fox","Franzen","Frazier","Freud","Friedan","Friedman","Fromm","Frost","Frye","Fuentes","Fugard","Fuller","Furst","Gaddis","Gaines","Galsworthy","Gandhi","Gardner","Gass","Seuss","Genet","Gibbons","Gide","Gilbert","Ginsberg","Ginzburg","Glück","Godwin","Golding","Goldman","Gordimer","Gordon","Gorky","Grass","Graves","Green","Greenberg","Greene","Grisham","Hailey","Hall","Hammett","Heidegger","Heinlein","Heller","Hemingway","Henry","Herr","Hersey","Hesse","Highsmith","Hitchens","Hoffman","Hornby","Housman","Howard","Hubbard","Hughes","Hurston","Huxley","Ionesco","Irving","Isherwood","Ishiguro","Joyce","Jung","Jünger","Kafka","Keneally","Kennedy","Kerouac","Kerr","Kesey","Keynes","Kilmer","Kincaid","King","Kingsolver","Kingston","Kinsey","Koestler","Koltès","Koontz","Kosinski","Krakauer","Kundera","L'Amour","Larkin","Laurence","Lawrence","Leary","leCarré","L'Engle","LeGuin","Leiris","Lem","Lessing","Lethem","Letts","Liebling","VargasLlosa","Lodge","London","GarcíaLorca","Lorde","Lott","Lovecraft","Lowell","Lowry","Loy","Ludlum","MacLeish","Mailer","Malamud","Malraux","Mamet","Mann","GarcíaMárquez","Matheson","SomersetMaugham","McCarthy","McCullers","McCullough","McEwan","McInerney","McMurtry","Mead","Mencken","Merton","Michener","St.VincentMillay","Miller","Milne","Miłosz","Mitchell","Molnár","Moorcock","Moore","Morrison","Mosley","Mumford","Müller","Munro","Murakami","Murdoch","Nabokov","Naipaul","Nash","Naylor","Némirovsky","Neruda","Nesbit","Neville","Niedecker","Nin","Noon","Nordhoff","Norman","Norris","Oates","O'Brian","O'Casey","O'Connor","Odets","O'Hara","Olmstead","Olson","O'Nan","Ondaatje","O'Neill","Ōe","Orwell","Ozick","Palahniuk","Paley","Pamuk","Parker","Pasternak","Pekar","PerkinsGilman","Piercy","Pinter","Pirandello","Plath","Platonov","Porter","Potok","Potter","Pound","Powell","Powers","Pratchett","Gaiman","Proulx","Proust","Pullman","Puzo","Pynchon","Queneau","Rand","Rawlings","Rhys","Rilke","Robbe-Grillet","Robbins","Roethke","Roth","Rowling","Rushdie","Russell","Russo","deSaint-Exupéry","Sagan","Salinger","Salzman","Sandburg","Saramago","Saroyan","Sartre","Scott-Heron","Sebald","Sebold","Sendak","Seton","Sexton","Shaara","Shapiro","Silko","BashevisSinger","Smiley","Smith","Snow","Snyder","Sokolov","Solzhenitsyn","Sontag","Soyinka","Spillane","Stein","Steinbeck","Stephenson","Stevens","Stewart","Stine","Stirling","Stone","Stoppard","Straub","Sturgeon","Styron","Talese","Tarkington","Tartt","Taylor","Teasdale","Thurber","Tolkien","Toller","Toole","Toomer","Trilling","Trumbo","Tsvetaeva","Turtledove","Tzara","Updike","Uris","Valéry","Vallejo","Vidal","Vonnegut","Walker","Wallace","Walser","Wambaugh","Warren","Waters","Waugh","Wells","Welty","West","Wharton","White","Whitehead","Wiesel","Wilbur","IngallsWilder","Williams","Willis","Wilson","Winterson","Winton","Wister","Wittig","Wodehouse","Wolfe","Woodward","Woolf","Wouk","Woollcott","Wren","Wright"]


characters=[]
scenes=[]
backgrounds=["thing"]

charactersInScene=[]
characterMoods={}

def randomColor():
	color=""
	for i in range(0, 6):
		color += random.choice(string.hexdigits)
	return color

def randomName():
	return random.choice(firstNames)+" "+random.choice(lastNames)

def buildCharacter(name):
	escapedName="_".join(name.split())
	if not escapedName in characters:
		print("define "+escapedName+" = Character(\""+name+"\", color=\""+randomColor()+"\")")
		# Somehow produce a base image of the character
		# probably based on a corpus of anime heads/hair/bodies?
		# Then, name it escapedName_base.png
		for mood in moods:
			# Somehow produce an image for each mood.
			# probably based on a corpus of anime eyes/mouths?
			# Then, superimpose them on a base image of the character and name it escapedName_mood.png
			print("image "+escapedName+" "+mood+" = \""+escapedName+"_"+mood+".png\"")
		characters.append(escapedName)
		characterMoods[escapedName] = random.choice(moods)

def printCharacterDefs(n):
	for i in range(0, n):
		buildCharacter(randomName())

def produceInsult():
	return random.choice(["Fuck you", "You're so "+random.choice(["stupid", "ignorant", "ugly", "fat", "thin", "arrogant"])+random.choice(["", " that "+random.choice(["when you lay around the house you really lay around the house", "you can't even "+random.choice(["", random.choice(["walk", "talk", "think", "speak", "calculate"])+" "+random.choice(["straight", "correctly", "right", "2 + 2"])]), "even "+random.choice([random.choice([randomName(), "your "+random.choice(["mother", "father", "sister", "brother", "uncle", "aunt"])])+" "+random.choice(["can't stand you", "hates you", "vomits upon seeing you"])])])]), "Go fuck your "+random.choice(["mother", "father", "sister", "brother", "self", "uncle", "aunt"])+random.choice(["", ", you "+random.choice(["shit", "douche", "pussy", "fuck", "cock", "ass", "butt", "anus", "dunder"])+random.choice(["head", "wad", "sucker", "eater", "fuck", "brain", "fucker", "ass", "butt"])])])

def produceCompliment():
	return "I really like your "+random.choice(nouns)+"!"+random.choice(["", " It's "+random.choice(["so", "very"])+" "+random.choice(adjectives)])

def produceSentence():
	return random.choice([produceInsult(), produceCompliment()])

def produceDialogue(character):
	dialogue=""
	mood=""
	if (character=="player"):
		mood=random.choice(moods)
	else:
		mood=characterMoods[character]
	if (mood=="angry"):
		return produceInsult()
	elif (mood=="happy"):
		return produceCompliment()
	else:
		return produceSentence()

def buildScene(sceneName):
	print(sceneName+":")
	for i in range(0, random.choice(range(1, 500))):
		mode=random.choice(["background", "dialogue", "transition", "characterState", "choose"])
		if (mode=="background"):
			print("\tscene bg "+random.choice(backgrounds))
		elif (mode=="dialogue"):
			if(len(charactersInScene)==0):
				charactersInScene.append(random.choice(characters))
			character=random.choice(charactersInScene)
			print("\tshow "+(" ".join(character.split("_")))+" "+characterMoods[character])
			print("\t"+character+" \""+produceDialogue(character)+"\"")
		elif (mode=="transition"):
			print("\twith "+random.choice(["fade", "dissolve", "pixellate"]))
		elif (mode=="characterState"):
			if(len(charactersInScene)==0):
				charactersInScene.append(random.choice(characters))
			character=random.choice(charactersInScene)
			newMood=random.choice(moods)
			if(random.choice(range(1, len(moods)+2))>len(moods)):
				print("\thide "+(" ".join(character.split("_")))+" "+characterMoods[character])
			else:
				characterMoods[character]=newMood
				print("\tshow "+(" ".join(character.split("_")))+" "+characterMoods[character])
		elif (mode=="choose"):
			if(len(scenes)>0):
				print("\tmenu:")
				for j in range(0, random.choice(list(range(0, len(scenes))))%5):
					print("\t\t\""+produceDialogue("player")+"\":")
					print("\t\t\t"+random.choice(scenes))
	scenes.append(sceneName)

def buildScenes(n):
	for i in range(0, n):
		buildScene(random.choice(adjectives)+random.choice(nouns))

printCharacterDefs(CHARACTER_COUNT)
buildScenes(SCENE_COUNT)
print(buildScene("init"))
