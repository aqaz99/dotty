import unittest
from dotty import GameManager, Dice  

class TestFarkleGame(unittest.TestCase):

	def test_straight_scoring(self):
		gm = GameManager()

		# Test straight scoring for 1-5
		gm.game_dice = [Dice(1, True), Dice(2,True), Dice(3,True), Dice(4,True), Dice(5,True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 500)
		gm.unbanked_score = 0

		# Test straight scoring for 1-5 With an extra 1
		gm.game_dice = [Dice(1, True), Dice(1, True), Dice(2,True), Dice(3,True), Dice(4,True), Dice(5,True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 600)
		gm.unbanked_score = 0

		# Test straight scoring for 1-5 With an extra 5
		gm.game_dice = [Dice(1, True), Dice(2,True), Dice(3,True), Dice(4,True), Dice(5,True), Dice(5,True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 550)
		gm.unbanked_score = 0

		# Test straight scoring for 2-6
		gm.game_dice = [Dice(2,True), Dice(3,True), Dice(4,True), Dice(5,True), Dice(6, True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 750)
		gm.unbanked_score = 0

		# Test straight scoring for 2-6 With an extra 5
		gm.game_dice = [Dice(2,True), Dice(3,True), Dice(4,True), Dice(5,True), Dice(5,True), Dice(6, True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 800)
		gm.unbanked_score = 0
		
		# Test straight scoring for 1-6
		gm.game_dice = [Dice(1,True), Dice(2,True), Dice(3,True), Dice(4,True), Dice(5,True), Dice(6, True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 1500)

	def test_triple_scoring(self):
		gm = GameManager()
		
		# Test 1s
		for i in range(3, 7):
			gm.game_dice = [Dice(1, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 1000 * (2 ** (i - 3)) if i >= 3 else 0)
			gm.unbanked_score = 0

		# Test 2s
		for i in range(3, 7):
			gm.game_dice = [Dice(2, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 200 * (2 ** (i - 3)) if i >= 3 else 0)
			gm.unbanked_score = 0
		
		# Test 3s
		for i in range(3, 7):
			gm.game_dice = [Dice(3, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 300 * (2 ** (i - 3)) if i >= 3 else 0)
			gm.unbanked_score = 0

		# Test 3s
		for i in range(3, 7):
			gm.game_dice = [Dice(4, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 400 * (2 ** (i - 3)) if i >= 3 else 0)
			gm.unbanked_score = 0
		
		# Test 3s
		for i in range(3, 7):
			gm.game_dice = [Dice(5, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 500 * (2 ** (i - 3)) if i >= 3 else 0)
			gm.unbanked_score = 0
		
		# Test 6s
		for i in range(3, 7):
			gm.game_dice = [Dice(6, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 600 * (2 ** (i - 3)) if i >= 3 else 0)
			gm.unbanked_score = 0

	def test_single_scoring(self):
		gm = GameManager()
		gm.game_dice = [Dice() for _ in range(6)]

		for i in range(1, 3):
			gm.game_dice = [Dice(1, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 100 * i)
			gm.unbanked_score = 0
		
		for i in range(1, 3):
			gm.game_dice = [Dice(5, True)] * i 
			gm.calculate_score()
			self.assertEqual(gm.unbanked_score, 50 * i)
			gm.unbanked_score = 0
		

	def test_my_tests(self):
		gm = GameManager()

		# Test two 1s and 2 5s
		gm.game_dice = [Dice(1, True), Dice(1,True), Dice(5,True), Dice(5,True), Dice(6,True), Dice(6,True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 300)
		gm.unbanked_score = 0


		# Test three 1s and 2 5s
		gm.game_dice = [Dice(1, True), Dice(1,True), Dice(1,True), Dice(5,True), Dice(5,True), Dice(6,True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 1100)
		gm.unbanked_score = 0

		# Test two 5s and 1 1
		gm.game_dice = [Dice(1, True), Dice(5,True), Dice(5,True), Dice(2,True), Dice(2,True), Dice(6,True)]
		gm.calculate_score()
		self.assertEqual(gm.unbanked_score, 200)
		gm.unbanked_score = 0

if __name__ == "__main__":
	unittest.main()
