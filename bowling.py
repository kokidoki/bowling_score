# Program plan:
# player input
# scan through input
# check for spare or strike 
# if spare or strike do math for it taking new input and skipping the rest of the other steps
# keep adding input to total
player_input = input("Enter your bowling scores here: ")
total_score = 0
strike_counter = 1
strike = False
for score in player_input:
	if strike == True:
		total_score += score * 2
		strike_counter += 1
		if strike_counter == 3:
			strike_counter = 1
			strike = False
	if score == 'X':
		strike = True
	else:
		total_score += score	  
print(score)