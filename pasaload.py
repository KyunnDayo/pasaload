import threading
import time
import random
from threading import Thread, Lock
lock = Lock()

load_bal = 0
if load_bal == 0:
	rand_load = random.randint(1,50)
	load_bal = rand_load


	def transact(amount):
		lock.acquire()	
		global load_bal
		load_bal += amount
		print("Processing... Please wait. ")
		time.sleep(2)
		print("Your current Balance is: ", load_bal)
		lock.release()

	def checkBal():
		lock.acquire()	
		print(load_bal)

		lock.release()

	def addLoad():
		lock.acquire()

		print("How much load you want? ")
		print("1. P20")
		print("2. P50")
		print("3. P100")
		print("5. EXIT")

		x = True
		while x == True:
			userInput = input("Enter number of choice: ")
			if (userInput == '1'):
				thread1 = threading.Thread(target=transact, args=(20,))
				thread1.start()
				thread1.join()
			elif (userInput == '2'):
				thread2 = threading.Thread(target=transact, args=(50,))
				thread2.start()
				thread2.join()
			elif (userInput == '3'):
				thread3 = threading.Thread(target=transact, args=(100,))
				thread3.start()
				thread3.join()
			elif (userInput == '5'):
				x = False;
				break;
		lock.release()		

	def main():
		
		print("Garena Pasaload Service: ")
		userNum = int(input("Enter your Phone number: "))
		print("Checking Load Balance, Please Wait..")
		time.sleep(3)
		checkBal()

		choice = input("Gusto mo ba ng load? (y/n)")
		if choice == 'y' or 'Y':
			addLoad()
		elif choice == 'n' or 'N':
			print("Thank you for using our service.")
		else:
			print("Select a valid Option.")
			main()

		pass

	while True:
		main()
		choice = input("Do you want to rerun the program? (y/n)")
		if choice.lower != "y":
			break