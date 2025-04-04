import random

# Adaptation of the game Farkle for ML training
class Dice:

	def __init__(self, value=1, held=False):
		self.value = value
		self.held = held
		self.held_on_round = 0

	def roll(self):
		self.value = random.randint(1, 6)
		return self.value

class GameManager:
	def __init__(self):
		self.round = 0
		self.unbanked_score = 0
		self.current_score = 0
		self.required_score = 1500
		self.scored_dice_values = []
		self.game_dice = [Dice() for i in range(6)]
	
	def start_game(self):
		print("-" * 20)
		print("Game started")
		print("-" * 20)

		while self.current_score < self.required_score:
			self.play_round()
		if self.current_score >= self.required_score:
			print("You won!")
		print(f"Final Score: {self.current_score}")
		print("-" * 20)


	def play_round(self):
		self.round += 1
		self.roll_dice()
		self.hold_dice()
		self.calculate_score()
		self.keep_rolling_or_bank()

	def print_score(self):
		print("-" * 20)
		print(f"Score Score: ({self.unbanked_score}) {self.current_score}/{self.required_score}")
		print("-" * 20)


	def roll_dice(self):
		# Roll all the dice and add it to self.dice
		for index, die in enumerate(self.game_dice):
			if(not die.held):
				die.roll()
				print(f"Die {index + 1}: {die.value}")
	
	def hold_dice(self):
		# Get player input on which dice to hold in a list like: '1 3 5' or '125'
		# read player input
		held_dice = input("Hold Dice: ")
		# Only accept numbers, between 1 and 6
		held_dice = list(set(filter(lambda a: a != " " and a.isdigit() and int(a) <= 6, held_dice)))
		for die in held_dice:
			self.game_dice[int(die) - 1].held = True
			self.game_dice[int(die) - 1].held_on_round = self.round

	def calculate_score(self):
		# Calculate the score of the current roll
		# Add score to current_score
		# Reset held
		# Print the score
		score = 0
		scoring_dice = []
		for die in self.game_dice:
			if die.held and die.held_on_round == self.round:
				scoring_dice.append(die.value)
		
		scoring_dice = sorted(scoring_dice)
		# print(f"Scoring Dice: {scoring_dice}")
		# Check for straight
		if all(x in scoring_dice for x in [1, 2, 3, 4, 5, 6]):
			scoring_dice.remove(1)
			scoring_dice.remove(2)
			scoring_dice.remove(3)
			scoring_dice.remove(4)
			scoring_dice.remove(5)	
			scoring_dice.remove(6)	
			score += 1500
		elif all(x in scoring_dice for x in [2, 3, 4, 5, 6]):
			scoring_dice.remove(2)
			scoring_dice.remove(3)
			scoring_dice.remove(4)
			scoring_dice.remove(5)	
			scoring_dice.remove(6)	
			score += 750
		elif all(x in scoring_dice for x in [1, 2, 3, 4, 5]):
			scoring_dice.remove(1)
			scoring_dice.remove(2)
			scoring_dice.remove(3)
			scoring_dice.remove(4)
			scoring_dice.remove(5)	
			score += 500

	
		# Check for triples, quadruples, quintuples, and sextuples
		for i in range(1, 7):
			count = scoring_dice.count(i)
			if count >= 3:
				if i == 1:
					score += 1000 * (2 ** (count - 3))
				else:
					score += i * 100 * (2 ** (count - 3))
				# Remove scored dice
				scoring_dice = list(filter(lambda a: a != i, scoring_dice))

		# Check for singles
		for i in range(1, 7):
			if i == 1:
				score += scoring_dice.count(i) * 100
			elif i == 5:
				score += scoring_dice.count(i) * 50
		# If no straight, calculate triples and singles
				
		self.unbanked_score += score

	def keep_rolling_or_bank(self):	
		self.print_score()
		# Count how many dice are left to roll
		remaining_dice = len(list(filter(lambda a: not a.held, self.game_dice)))
		print(f"Keep rolling or bank scored points and move to next round? {remaining_dice} dice left")
		while True:

			choice = input("K/B: ")
			if choice.lower() == "b":
				self.current_score += self.unbanked_score
				self.unbanked_score = 0
				self.game_dice = [Dice() for i in range(6)]
				self.print_score()
				break
			elif choice.lower() == "k":
				break

if __name__ == "__main__":
	gm = GameManager()
	gm.start_game()