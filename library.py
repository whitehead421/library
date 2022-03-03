import time
import string
import random
import os
from termcolor import colored
from collections import Counter

clean_the_screen = ("cls" if os.name == "nt" else "clear")

# Function for listing books with their full information.
def listBooks():
	file = open("books.txt", "r")
	lines = file.readlines()
	file.close()

	for i in lines:
		splitted = i.split(",")
		numberISBN = colored(f"{splitted[0]}", "blue")
		nameBook = colored(f"{splitted[1]}", "magenta", "on_grey")
		nameAuthor = colored(f"{splitted[2]}", "yellow")
		checkOut = splitted[3]
		if checkOut == "T\n":
			checkOut = colored("Book is not in the library.", "red")
		if checkOut == "F\n":
			checkOut = colored("Book is in the library.", "green")
		print("-" * 115)
		print(f"Name: {nameBook} - Author: {nameAuthor} - Status: {checkOut} - ISBN: {numberISBN}\n")


# Function for showing the books those are checked out by students.
def listBooksChecked():
	file = open("books.txt", "r")
	lines = file.readlines()
	file.close()

	a = 0
	for i in lines:
		splitted = i.split(",")
		numberISBN = colored(f"{splitted[0]}", "blue")
		nameBook = colored(f"{splitted[1]}", "magenta", "on_grey")
		nameAuthor = colored(f"{splitted[2]}", "yellow")
		checkOut = splitted[3]
		if checkOut == "T\n":
			a += 1
			print("-" * 115)
			print(f"Name: {nameBook} - Author: {nameAuthor} - ISBN: {numberISBN}\n")
	if a == 0:
		print("-" * 115)
		print(colored("\tUhm..- Nobody reads books these days.\n", "blue"))
		print("There is no checked out book. All the books are in the library.")


# Function for adding new books to library's data.
def addBook():
	file = open("books.txt", "r")
	lines = file.readlines()
	file.close()
	
	isbn = input("Please enter the ISBN number: ")
	nameBook = input("Please enter the name of book: ")
	nameAuthor = input("Please enter the author name: ")
	
	for i in lines:
		splitted = i.split(",")
		isbnBook = splitted[0]
		nBook = splitted[1]
		if isbn == isbnBook:
			print(colored("There is already a book with this ISBN.", "red"))
			print(f"\t{isbn} - {nBook}")
			break
	else:
		print(colored("\nThe book succesfully added to the data.", "green"))
		status = "F\n"
		file = open("books.txt", "a+")
		file.write(f"{isbn},{nameBook},{nameAuthor},{status}")
		file.close()


# Function for searching books by their ISBN numbers in data.
def searchBookISBN():
	file = open("books.txt", "r")
	lines = file.readlines()
	file.close()

	searchingISBN = input("Enter the ISBN number of book which you are looking for.\n> ")
	a = 0
	for i in lines:
		splitted = i.split(",")
		numberISBN = colored(f"{splitted[0]}", "blue")
		nameBook = colored(f"{splitted[1]}", "magenta", "on_grey")
		nameAuthor = colored(f"{splitted[2]}", "yellow")
		checkOut = splitted[3]
		if checkOut == "T\n":
			checkOut = colored("is not in the library.", "red")
		if checkOut == "F\n":
			checkOut = colored("is in the library.", "green")

		if searchingISBN.upper() in numberISBN:
			print("-" * 95)
			print(colored(f"{numberISBN}", "blue"), "-", f"'{nameBook}' by {nameAuthor} {checkOut}")
			print("-" * 95)
			a += 1
	if a == 0:
		print("Sorry. There is no book with this ISBN number.")



# Function for searching books by their names in data.
def searchBookName():
	file = open("books.txt", "r")
	lines = file.readlines()
	file.close()

	searchingName = input("Enter the name of book which you are looking for.\n> ")
	a = 0
	for i in lines:
		splitted = i.split(",")
		numberISBN = colored(f"{splitted[0]}", "blue")
		nameBook = colored(f"{splitted[1]}", "magenta", "on_grey")
		nameAuthor = colored(f"{splitted[2]}", "yellow")
		checkOut = splitted[3]

		if checkOut == "T\n":
			checkOut = colored("Book is not in the library.", "red")
		if checkOut == "F\n":
			checkOut = colored("Book is in the library.", "green")

		if searchingName.lower() in nameBook.lower():
			a += 1
			print(colored("-" * 95, "cyan"))
			print(f"ISBN: {numberISBN} - Name : {nameBook} - Author: {nameAuthor} - Status: {checkOut}\n")
			print(colored("-" * 95, "magenta"))
	if a == 0:
		print("Sorry. There is no book with this name.")


# Function for searching books by their authors' name in data.
def searchBookAuthor():
	file = open("books.txt", "r")
	lines = file.readlines()
	file.close()

	searchingAuthor = input("Enter the author name which you are looking for: ")
	a = 0
	for i in lines:
		splitted = i.split(",")
		numberISBN = colored(f"{splitted[0]}", "blue")
		nameBook = colored(f"{splitted[1]}", "magenta", "on_grey")
		nameAuthor = colored(f"{splitted[2]}", "yellow")
		checkOut = splitted[3]

		if checkOut == "T\n":
			checkOut = colored("Book is not in the library.", "red")
		if checkOut == "F\n":
			checkOut = colored("Book is in the library.", "green")

		if searchingAuthor.lower() in nameAuthor.lower():
			a += 1
			print("-" * 95)
			print(f"Author: {nameAuthor} - Name : {nameBook} - ISBN: {numberISBN} - Status: {checkOut}\n")
	if a == 0:
		print(colored("Sorry. There is no author with this name.", "red"))


# Function for generating tickets when checking out a book to check in book with. 
# Possibility of 2.176.782.336 tickets.
def ticketGenerator(student_id, book_name):
	chars = string.digits + string.ascii_uppercase
	ticket = "".join(random.sample(chars, 6))

	file = open("tickets.txt", "a+")
	lines = file.readlines()
	for i in lines:
		splitted = i.split("-")
		ticket2 = splitted[0]
		if ticket == ticket2:
			return ticketGenerator()
	else:
		file.write(f"{ticket}-{book_name}-{student_id}\n")
	file.close()
	return ticket


# Function for checking out books to students' data.
def checkOutBook():
	file = open("books.txt", "rt")
	dataBooksLines = file.readlines()
	file.close()
	file = open("students.txt", "r")
	dataStudentsLines = file.readlines()
	file.close()
	dataCheckOut = open("checkouts.txt", "a")

	bookToCheckOut = input("Please enter the ISBN number of book that you want to check out: ")

	isBookToCheckOut = False
	isBookToStudent = False

	# Controlling if there is a book with this ISBN or not.
	for i in dataBooksLines:
		splitted = i.split(",")
		numberISBN = splitted[0]
		if bookToCheckOut == splitted[0]:
			isBookToCheckOut = True
			break
	else:
		print(colored("There is no book with this ISBN number.", "red"))
		pass
		
	
	if isBookToCheckOut == True:
		bookToStudent = input("Please enter the student ID to check out: ")
		for i in dataStudentsLines:
			splitted = i.split(maxsplit= 1)
			studentID = splitted[0]
			studentName = splitted[1]
			if bookToStudent == studentID:
				isBookToStudent = True
				break
		else:
			print(colored("There is no student with this ID. Try again.", "red"))
			pass

		
	if isBookToStudent == True:
		for i in dataBooksLines:
			splitted = i.split(",")
			numberISBN = splitted[0]
			nameBook = splitted[1]
			nameAuthor = splitted[2]
			checkOut = splitted[3]
			if bookToCheckOut == numberISBN:
				if checkOut == "T\n":
					print(colored("Oops! This book is already checked out.", "red"))
				else:
					print(colored("Are you sure to check out this book?\n", "blue", "on_grey"))
					print("ISBN:", colored(numberISBN, "blue"), "-", "Name :", colored(nameBook, "magenta", "on_grey"), "-", "Author:", colored(nameAuthor, "yellow"))
					print(f"\nThis book will checked out to: " + colored(studentName, "white", "on_grey", attrs=['blink']))
					verify = ""
					while verify != "Y" or verify != "N" or verify != "y" or verify != "n":
						verify = input("\nEnter Y or N\n" + colored("> ", "grey", attrs=['blink']))
						if verify == "N" or verify == "n":
							break
						if verify == "Y" or verify == "y":
							
							# Generating ticket and giving it to student.
							ticketnumber = ticketGenerator(student_id= bookToStudent, book_name= nameBook)
							os.system(clean_the_screen)
							print(f"""
	____/         \ /         \____
	/| ------------- |  ----------- |\
	||| ------------- | --->{colored(ticketnumber, "red", "on_cyan", attrs=['reverse', 'blink'])} |||
	||| ------------- | ------------- |||
	||| ------- ----- | --Here is---- |||
	||| ------------- | -your-ticket--|||
	||| ------------- | ----number.---|||
	|||  ------------ | --Use-it------|||
	||| ------------- |  -when-you--- |||
	||| ------------- | -checking-in--|||
	||| ------------- | ---the-book.--|||
	||| ------------  | ------------- |||
	|||_____________  |  _____________|||
	/_____/--------\\_//--------\_____\
							""")
							

							dataCheckOut.write(f"{numberISBN}-{ticketnumber}-{bookToStudent}-{nameBook}-{nameAuthor}\n")
							dataCheckOut.close()
							print(colored("\nThe book succesfully checked out to the student.", "green"))


	# TO WRITE "T" ON BOOKS FILE WHEN CHANGED
							for i in dataBooksLines:
								splitted = i.split(",")
								numberISBN = splitted[0]
								nameBook = splitted[1]
								nameAuthor = splitted[2]
								checkOut = splitted[3]
								if bookToCheckOut == numberISBN:
									file = open("books.txt", "r")
									content = file.read()
									content = content.replace("{},{},{},{}".format(numberISBN, nameBook, nameAuthor, checkOut), "{},{},{},T\n".format(numberISBN, nameBook, nameAuthor))
									file.close()
									file = open("books.txt", "w")
									file.write(content)
									file.close()
							break

# Function for listing students by their names with the books they checked out under their names.
def listStudents():
	file = open("checkouts.txt", "r")
	checkOutsLines = file.readlines()
	file.close()
	file = open("students.txt", "r")
	studentsLines = file.readlines()
	file.close()
	file = open("checkins.txt", "r")
	checkInsLines = file.readlines()
	file.close()


	isCheckInsLines = False
	if len(checkInsLines) == 0:
		isCheckInsLines = True

	for i in studentsLines:
		splitted = i.split()
		sNumber = splitted[0]
		sName = splitted[1]
		sLastname = splitted[2]
		print(colored("-" * 80, "grey"))
		print(colored(f"{sName} {sLastname}", "blue"))
		for x in checkOutsLines:
			splitted = x.split("-")
			nameBook = splitted[3]
			scNumber = splitted[2]
			ticket1 = splitted[1]
			if isCheckInsLines:
				if sNumber == scNumber:
					print(colored("-" * 80, "grey"))
					print(colored(f"\t-{nameBook}", "magenta", "on_grey"))
			else:
				for z in checkInsLines:
					splitted = z.split("-")
					ticket2 = splitted[1]
					if ticket1 == ticket2:
						break
				else:
					if sNumber == scNumber and ticket1 != ticket2:
						print(colored("-" * 80, "grey"))
						print(colored(f"\t-{nameBook}", "magenta", "on_grey"))

# Function for printing the top three most checked out books.
def topThreeBook():
	file = open("checkouts.txt", "r")
	checkoutsLines = file.readlines()
	file.close()
	file = open("books.txt", "r")
	booksLines = file.readlines()
	file.close()

	isbns = []

	for i in checkoutsLines:
		splitted = i.split("-")
		isbn = splitted[0]
		isbns.append(isbn)
	dictionary = Counter(isbns)

	val_list = list(dictionary.values())
	for i in range(3):
		print("_" * 105)
		if i == 0:
			print(colored("THE MOST CHECKED OUT BOOK(S)!", "red", "on_yellow", attrs=['blink']))
		elif i == 1:
			print(colored("THE SECOND MOST CHECKED OUT BOOK(S)!", "red", "on_yellow", attrs=['blink']))
		elif i == 2:
			print(colored("THE THIRD MOST CHECKED OUT BOOK(S)!", "red", "on_yellow", attrs=['blink']))
		try:
			if len(val_list) != 0:
				print("_" * 105)
				print(colored(f"This/these book(s) has/have checked out for [{str(max(val_list))}] time(s)!", "cyan"))
				print("_" * 105)
				print("\n")
				if val_list.count(max(val_list)) > 1:
					for key, value in dictionary.items():
						if max(val_list) == value:
							for z in booksLines:
								splitted2 = z.split(",")
								bookISBN = splitted2[0]
								bookName = splitted2[1]
								if key == bookISBN:			
									key = bookName # key = isbn
							print(key)
					for i in range(val_list.count(max(val_list))):
						val_list.remove(max(val_list))
				elif val_list.count(max(val_list)) == 1:
					for key, value in dictionary.items():
						if max(val_list) == value:
							for z in booksLines:
								splitted2 = z.split(",")
								bookISBN = splitted2[0]
								bookName = splitted2[1]
								if key == bookISBN:			
									key = bookName # key = isbn
							print(key)
							val_list.remove(max(val_list))
							break
		except:
			print("There is no other books.")

# Function for printing top three students who checked out most.
def topThreeStudents():
	dataCheckOut = open("checkouts.txt", "r")
	dataCheckOutsLines = dataCheckOut.readlines()
	dataCheckOut.close()
	dataStudents = open("students.txt", "r")
	dataStudentsLines = dataStudents.readlines()
	dataStudents.close()

	studentNumbers = []

	for i in dataCheckOutsLines:
		splitted = i.split("-")
		stNumber = splitted[2]
		studentNumbers.append(stNumber)
	studentNumbers = Counter(studentNumbers)


	val_list = list(studentNumbers.values())
	for i in range(3):
		print("_" * 105)
		if i == 0:
			print(colored("THE TOP #1 STUDENT(S)!", "red", "on_yellow", attrs=['blink']))
		elif i == 1:
			print(colored("THE TOP #2 STUDENT(S)!", "red", "on_yellow", attrs=['blink']))
		elif i == 2:
			print(colored("THE TOP #3 STUDENT(S)!", "red", "on_yellow", attrs=['blink']))
		try:
			if len(val_list) != 0:
				print("_" * 105)
				print(colored(f"This/these student(s) has/have checked out for [{str(max(val_list))}] time(s)!", "cyan"))
				print("_" * 105)
				print("\n")
				if val_list.count(max(val_list)) > 1:
					for key, value in studentNumbers.items():
						if max(val_list) == value:
							for z in dataStudentsLines:
								splitted2 = z.split(maxsplit= 1)
								sNumber = splitted2[0]
								sName = splitted2[1]
								if key == sNumber:			
									key = sName
							print(key)
					for i in range(val_list.count(max(val_list))):
						val_list.remove(max(val_list))
				elif val_list.count(max(val_list)) == 1:
					for key, value in studentNumbers.items():
						if max(val_list) == value:
							for z in dataStudentsLines:
								splitted2 = z.split(maxsplit= 1)
								sNumber = splitted2[0]
								sName = splitted2[1]
								if key == sNumber:			
									key = sName
							print(key)
							val_list.remove(max(val_list))
							break
		except:
			print("There is no other students who has checked out before.")



# Function for adding new students to data.
def addStudent():
	file = open("students.txt", "r")
	lines = file.readlines()
	file.close()

	numberStudent = input("Please enter the ID of a student to add.\n> ")
	nameStudent = input("\nPlease enter the name of a student to add.\n> ")
	for i in lines:
		splitted = i.split(maxsplit= 1)
		nStudent = splitted[0]
		naStudent = splitted[1]
		if numberStudent == nStudent:
			print("This student ID is already exist.")
			print(f"\t{nStudent} - {naStudent}")
			break
	else:
		print(colored("\nThe student succesfully added to the data.", "green"))
		file = open("students.txt", "a+")
		file.write(f"{numberStudent} {nameStudent}\n")
		file.close()

# Function for checking in a book with the ticket given when checked out.
def checkInBook():
	ticket = input("Please enter the ticket to check in book.\n> ")

	dataBooks = open("books.txt", "r")
	dataBooksLines = dataBooks.readlines()
	dataBooks.close()

	file = open("checkouts.txt", "r")
	checkoutsLines = file.readlines()
	file.close()
	a = 0
	for i in checkoutsLines:
		splitted = i.split("-")
		isbn = splitted[0]
		tNumber = splitted[1]
		studentID = splitted[2]
		nameBook = splitted[3]
		if ticket == tNumber:
			a += 1
			print(colored("Thank you for bringing back the book!", "green"))
			file = open("checkins.txt", "a")
			file.write(f"The book in-{ticket}-came back.\n")
			file.close()

			# TO WRITE "F" ON BOOKS FILE WHEN CHANGED
			for i in dataBooksLines:
				splitted = i.split(",")
				numberISBN = splitted[0]
				nameBook = splitted[1]
				nameAuthor = splitted[2]
				checkOut = splitted[3]
				if isbn == numberISBN:
					file = open("books.txt", "r")
					content = file.read()
					content = content.replace("{},{},{},{}".format(numberISBN, nameBook, nameAuthor, checkOut), "{},{},{},F\n".format(numberISBN, nameBook, nameAuthor))
					file.close()
					file = open("books.txt", "w")
					file.write(content)
					file.close()
			break
	if a == 0:
		print(colored(f"Sorry. There is no ticket as '{ticket}'.", "red"))


maxims = [
			"'I have always imagined that Paradise will be a kind of a Library.' - Jorge Luis Borges ",
			"'Nothing is pleasanter than exploring a library.' - Walter Savage Landor ",
			"'The only thing that you absolutely have to know, is the location of the library.' - Albert Einstein",
			"'When in doubt go to the library.' - J.K. Rowling ",
			"'I have found the most valuable thing in my wallet is my library card.' - Laura Bush",
			"'Google can bring you back 100,000 answers, a librarian can bring you back the right one.' - Neil Gaiman",
			"'The most important asset of any library goes home at night – the library staff.' - Timothy Healy",
			"'Librarians are tour-guides for all of knowledge.' - Patrick Ness",

]


slider = colored("-" * 48, "red")
version = colored("library.py-v1.0", "green")
menu = f"""{version}
{random.choice(maxims)}
	


		       .--.                   .---.
		   .---|__|           .-.     |~~~|
		.--|===|--|_          |_|     |~~~|--.
		|  |===|  |'\     .---!~|  .--|   |--|
		|%%|   |  |.'\    |===| |--|%%|   |  |
		|%%|   |  |\.'\   |   | |__|  |   |  |
		|  |   |  | \  \  |===| |==|  |   |  |
		|  |   |__|  \.'\ |   |_|__|  |~~~|__|
		|  |===|--|   \.'\|===|~|--|%%|~~~|--|
		^--^---'--^    `-'`---^-^--^--^---'--'

		
			{colored("HELLO FROM WORLD LIBRARY!", "white", "on_blue", attrs=['blink'])}

		{colored("[1]", "blue")} List all the books in the library.
		{colored("[2]", "blue")} List all the books those are checked out.
		{colored("[3]", "blue")} Add a new book.
		{colored("[4]", "blue")} Search a book by ISBN number.
		{colored("[5]", "blue")} Search a book by name.
		{colored("[6]", "blue")} Check out a book to a student.
		{colored("[7]", "blue")} List all the students.
		{slider}
		{colored("[8] List top 3 most checked out books.", "cyan", attrs=['blink'])}
		{colored("[9] List top 3 student.", "cyan", attrs=['blink'])}
		{slider}
		{colored("[10]", "blue")} Add new student.
		{colored("[11]", "blue")} Search an author by name.
		{colored("[12]", "blue")} Check in a book to a library.	
		{slider}
		{colored("[0]", "red")} Exit

"""

password = "123456"

def login():
	os.system(clean_the_screen)
	print(colored("""

   ____________________________________________________
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |   |||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|
  | _____________________  ||      __   __  _  __    _ |
  ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
  || | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |
  ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
  |____________________ /\~()/()~//\ __________________|
  | __   __    _  _     \_  (_ .  _/ _    ___     _____|
  ||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |
  ||--|+|^^|==| || | | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
  ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
  |_________________ _/    \/\/\/    \_ _______________|
  | _____   _   __  |/      \../      \|  __   __   ___|
  ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
  ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
  ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
  |_________ __________\___\____/___/___________ ______|
  |__    _  /    ________     ______           /| _ _ _|
  |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
  | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
__|  \/\|/   /(____|/ //                    /  /||~|~|~|__
  |___\_/   /________//   ________         /  / ||_|_|_|
  |___ /   (|________/   |\_______\       /  /| |______|
      /                  \|________)     /  / | |

	""", "yellow"))
	login = input("Please enter the password to log in.\n> ")
	if password == login:
		print(colored("Succesfully logged in!", "green", attrs=['reverse', 'blink']))
		time.sleep(2)
		global isLogIn
		isLogIn = True
	else:
		print(colored("Wrong password!", "red", attrs=['reverse', 'blink']))
		print("Exiting...")
		time.sleep(2)
		os.system(clean_the_screen)
		exit()

enterToGo = colored("Press 'Enter' to continue to the menu...", "white", "on_grey", attrs=['blink'])
if True:
	isLogIn = False
	login()
	while isLogIn:
		os.system(clean_the_screen)
		print(menu)

		choice = input("What would you like to do?\n> ")
		choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "10", "11", "12"]
		
		if choice in choice_list:
			if choice == "1":
				os.system(clean_the_screen)
				listBooks()
				print("-" * 112)
				input(enterToGo)
			elif choice == "2":
				os.system(clean_the_screen)
				listBooksChecked()
				print("-" * 115)
				input(enterToGo)
			elif choice == "3":
				os.system(clean_the_screen)
				addBook()
				input(enterToGo)
			elif choice == "4":
				os.system(clean_the_screen)
				searchBookISBN()
				input(enterToGo)
			elif choice == "5":
				os.system(clean_the_screen)
				searchBookName()
				input(enterToGo)
			elif choice == "6":
				os.system(clean_the_screen)
				checkOutBook()
				input(enterToGo)
			elif choice == "7":
				os.system(clean_the_screen)
				listStudents()
				print("-" * 80)
				input(enterToGo)
			elif choice == "8":
				os.system(clean_the_screen)
				topThreeBook()
				print("-" * 80)
				input(enterToGo)
			elif choice == "9":
				os.system(clean_the_screen)
				topThreeStudents()
				print("-" * 80)
				input(enterToGo)
			elif choice == "10":
				os.system(clean_the_screen)
				addStudent()
				print("-" * 80)
				input(enterToGo)
			elif choice == "11":
				os.system(clean_the_screen)
				searchBookAuthor()
				print("-" * 80)
				input(enterToGo)
			elif choice == "12":
				os.system(clean_the_screen)
				checkInBook()
				print("-" * 80)
				input(enterToGo)



			elif choice == "0":
				print("Saving all the changes...")
				time.sleep(3)
				os.system(clean_the_screen)
				print("See you soon!\n")
				exit()
		else:
			print("Please enter a number in menu. (1-12)")
			input(enterToGo)