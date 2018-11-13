from random import sample

class Card():
	"""Class for single card, storing question, answer, 
	and boolean flag status."""

	def __init__(self, question='', answer=''):
		"""Instantiate Card class."""
		self.question = question
		self.answer = answer
		self.flag = False
		self.remove = False

	def add_question(self, q): 	# Add question and answer, stored as string
		self.question = str(q)

	def add_answer(self, a):	###
		self.answer = str(a)

	def get_question(self): 	# Returns question or answer string
		return self.question

	def get_answer(self):		###
		return self.answer

	def ch_flag(self): 			# Change flag status
		self.flag *= -1

	def get_flag(self): 		# Returns flag status (default is False)
		return self.flag

	def remove_card():			# Sets card for removal from flagging
		self.remove = True	


class Deck(Card):
	"""Class for deck of Card objects, including 'run_menu' function, 
	which drills cards on either side, allows user to flag for further review."""

	def __init__(self):
		self.cards = []					# Empty list
		self.hr = '\n'+'-'*25			# Horizontal rule -
		self.m_hr = '\n'+'*'*25			# Horizontal rule *
		self.gate = False				# To alternate handling of flags across runs
		self.yn = ''					# Flag request input value
		self.new_flag_round = False		# To indicate new flag round
		self.menu_response = ''			# Input receiver

	def add_card(self, c):
		self.cards.append(c)			# Adds card to deck list

	def shuffle(self):
		self.cards = sample(self.cards, len(self.cards))	# Shuffles deck

	def reset_flags(self):			# Resets flagged cards in deck to False
		for card in self.cards:
			if card.get_flag(): card.ch_flag()

	def reset_remove(self):			# Reset remove status to False
		for card in self.cards:
			if card.remove: card.remove = False

	def drill(self, rev=False):		# Runs a drill of all cards and allows flagging
		self.reset_flags()			# Resets flags for new run
		self.reset_remove()			# Resets remove status to False for new run
		self.shuffle()				# Shuffles deck
		for card in self.cards:
			print(self.hr)
			if rev: print(card.get_answer())	# If running answers
			else: print(card.get_question())	# Otherwise just do questions
			input('\n--(press return to flip)--\n')
			if rev: print(card.get_question())	# If running answers
			else: print(card.get_answer())		# Otherwise just show the answer
			print(self.hr)
			self.yn = input('\nFlag card for review? (y/n)\n')
			if self.yn == 'y' or self.yn == 'Y':
				card.ch_flag()					# Flag card for review if 'Y/y'
		print(self.hr)
		print("End of deck\n")
		print(self.hr)

	def drill_flags(self, rev=False):
		self.new_flag_round = False				# Reset new round indicator
		self.shuffle()							# Shuffle for new flag round

		if self.gate == False:	
			for card in self.cards:				# If no gate: Remove unflagged cards
				if card.get_flag() == False: card.remove_card()
												# Generates list alternating
			self.flagged_cards = [card for card in self.cards 	# flagged and
				if card.get_flag()]								# unflagged
		else:									# If gate: Remove flagged cards
			for card in self.cards:
				if card.get_flag(): card.remove_card()
			self.flagged_cards = [card for card in self.cards 
				if not card.get_flag()]
		for card in self.flagged_cards:			# For flagged cards to run
			print(self.hr)
			if rev: print(card.get_answer())
			else: print(card.get_question())
			input('\n---(press return to flip)---\n')
			if rev: print(card.get_question())
			else: print(card.get_answer())
			print(self.hr)
			self.yn = input('\nFlag card for review (y/n)\n')
			if self.yn == 'y' or self.yn == 'Y':
				new_flag_round = True			# Sets to remove unflagged cards
				card.ch_flag()					# Change flag to differentiate
		print(self.hr)
		print("End of deck\n")
		print(self.hr)				
		if new_flag_round: self.gate *= -1		# Change gate to look at other flag


	def run_menu(self):
		while True:								# Run until 'break'
			print(self.m_hr)
			print("FLASHCARDS MENU")
			print("1: Run Questions")
			print("2: Run Answers")
			print("Q: Quit")
			print(self.m_hr)
			self.menu_response = input()
			try:
				if int(self.menu_response) == 1: 
					self.drill()
					self.run_flags = input("Review flagged cards? (y/n)\n")
					while self.run_flags == 'y' or self.run_flags == 'Y':
						self.drill_flags()
				elif int(self.menu_response) == 2: 
					self.drill(rev=True)
					self.run_flags = input("Review flagged cards? (y/n)\n")
					while self.run_flags == 'y' or self.run_flags == 'Y':
						self.drill_flags(rev=True)
			except:
				if self.menu_response == 'q' or self.menu_response == 'Q': break

py_study = Deck()
new_cards = []

# Definitions for card objects
new_cards.append(Card('List Comprehension', 
	'[i for i in range(min, max)]'))
new_cards.append(Card('Bernoulli Distribution', 
	'Probability distribution with binary outcomes over a single trial'))
"""
new_cards.append(Card('Binomial Distribution', 
	'Probability distribution with binary outcomes over multiple trials'))
new_cards.append(Card('Poisson Distribution', 
	'Probability distribution with binary outcomes given lambda over time'))
new_cards.append(Card('Discrete Probability Distribution', 
	'Probability distribution with finite (countable) possible outcomes'))
new_cards.append(Card('Continuous Probability Distribution', 
	'Probability distribution with infinite (float) possible outcomes'))
new_cards.append(Card('Probability Mass Function', 
	'Probability that discrete outcome will occur over X number of trials'))
new_cards.append(Card('Cumulative Density Function',
	'Probability that discrete/continuous outcome X or less will occur'))
"""

# Adds all cards to master deck
for card in new_cards:
	py_study.add_card(card)

py_study.run_menu()							# Runs program

