import random
import re
from threading import Timer
import signal

signal.signal(signal.SIGINT, keyboardInterruptHandler)

states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

user_array = {
	'correct': 0,
	'incorrect': 0,
	'count': 0,
}

for item in states:
	item['count'] = 0
	item['incorrect'] = 0
	item['correct'] = 0

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up and stopping timer...".format(signal))
    t.cancel()
    exit(0)

def clear_user(arr):
		arr['count'] = 0
		arr['incorrect'] = 0
		arr['correct'] = 0

def clear_main(arr):
	for item in arr:
		item['count'] = 0
		item['incorrect'] = 0
		item['correct'] = 0

def done(arr):
	for item in arr:
		if (item['count'] == 0):
			stop_loop = 0
			break
		else:
			stop_loop = 1
	return stop_loop

def guess(cap):
    print(f"HINT: {cap[0:3]}")


def cow():
	while (done(states) == 0):

		random_array = random.sample(list(range(len(states))), 1)[0]
		user_array['count'] += 1
		print(f"What is the capital of {states[random_array]['name']}?")
		global t 
		t = Timer(5.0, guess, args=[ f"{states[random_array]['capital']}"] )
		t.start()
		x = input()
		t.cancel()
		

		p = re.search(f"{states[random_array]['capital']}", x,re.IGNORECASE)

		if p:
			print("right")
			user_array['correct'] += 1
			states[random_array]['correct'] += 1
		else:
			print("wrong")
			user_array['incorrect'] += 1
			states[random_array]['incorrect'] += 1

		states[random_array]['count'] += 1

		print(f"You have {user_array['correct']} out of {user_array['count']} correct!\n")

print("----------------Welcome to the State Matching Game----------------\n")

while(True):
	cow()
	print("Game Over.  Play Again?")
	x = input()
	p = re.search("y", x,re.IGNORECASE)

	if p:
		clear_user(user_array)
		clear_main(states)
		cow()
	else:
		break


#if x != main_array[random_array]['Capital']:
	
#else:

#for item in main_array:
#	print(item['State'])


#blah = main_array[0].keys()
#print(blah)

#for item in main_array[1]:

#	print(f"What is the Capital name of {item}?")
#x = input()
#print(x)


#main_array = [ 
#	{'State': 'Georgia' , 'Capital': 'Atlanta', 'correct': 0, 'incorrect': 0, 'count': 0}, 
#	{'State': 'New York' , 'Capital': 'New York', 'correct': 0, 'incorrect': 0, 'count': 0}, 
#	{'State': 'Texas' , 'Capital': 'Austin', 'correct': 0, 'incorrect': 0, 'count': 0},  
#	]