#packages
import random
import time

#Some text formatting stuff
big_spacer = "\n"*5
small_spacer = "\n"*2
ribbon = "~"*5
#short_pause = time.sleep(5)
#long_pause = time.sleep(8)

class player:
	def __init__(self):
		self.alive = True
		self.kingdom = {"military": 5, "religion": 5, "economy": 5}
		self.date = 0
	def dead(self):
		self.alive = False

def welcome():
	print(
	big_spacer
	,"Cue the jesters, it's time to play..."
	,ribbon,"COURTROOM!",ribbon
	,small_spacer,"Are your friends close enough?  Your enemies may be closer..."
	)

def day(player):
	date = player.date
	kingdom = player.kingdom
	alive = player.alive

	while True:
		time.sleep(2)
		print(
		big_spacer,"It is day",date
		,small_spacer,"A new day dawns, heralded by a messenger's news..."
		,small_spacer,ribbon
		)
		time.sleep(3)

		for i in kingdom:
			if kingdom[i] == 0:
				alive = False
				break

		if alive is False:
			print(
			small_spacer,"Good morning, my liege!"
			,big_spacer,"....My liege?"
			,big_spacer,"...."
			,big_spacer,"ALACK! Oh, calamitous day!  My liege has been slain in the night!"
			,small_spacer
			)
			time.sleep(5)
			print(
			"Your score was",date
			,small_spacer,"Thanks for playing!",ribbon*3
			)
			quit()
		if alive is True:
			print(
			small_spacer,"Good morning, my liege!"
			)
			for i in kingdom:
					print("The",i,"is:",kingdom[i])
			dilemma(player)
			date += 1

def dilemma(player):
	kingdom = player.kingdom
	kingdom_list = list(kingdom.keys())
	first_area = random.choice(kingdom_list)
	second_area = ""
	while True:
		i = random.choice(kingdom_list)
		if i != first_area:
			second_area = i
			break
	print(
	"You must improve your",first_area,"at the expense of your",second_area
	,small_spacer,"Or your",second_area,"at the expense of your",first_area
	,small_spacer,"Which will you pick?")

	while True:
		choice = input()
		if choice not in (first_area, second_area):
			print("Please pick either",first_area,"or",second_area,", my liege.")
		else:
			print("Very well, my liege.")
			break

	if choice == first_area:
		first_area_outcome = 1
	else:
		first_area_outcome = -1
	second_area_outcome = 0 - first_area_outcome

	kingdom[first_area] += first_area_outcome
	kingdom[second_area] += second_area_outcome
	#print(kingdom)

player = player()
welcome()
day(player)
