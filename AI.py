
class State():
	def __init__(self, m , c, b ):
		self.m = m #Missionaries to the left
		self.c = c #Cannibals to left
		self.b = b #Location of the boat (0 = left and 1 = right)

def is_goal(self):
	if self.m == 0 and self.c == 0:
		return True
	else:
		return False


def is_valid(self):
	if ((self.m >= self.c) or self.m == 0) and (((3-self.m) >= (3-self.c)) or (3-self.m) == 0) and self.m >= 0 and (3 - self.m >= 0) and self.c >= 0 and (3 - self.c >= 0):
	#if (self.m >= 0 and (3 - self.m >= 0) and self.c >= 0 and (3 - self.c >= 0) and (self.m == 0 or self.m >= self.c) and (((3 - self.m >= 0) == 0) or ((3 - self.m >= 0) >= (3 - self.c >= 0))):
		return True
	else:
		return False


def nextState(state):
	successors = [];
	if state.b == 0: #Barque à Gauche
		print("b = 0")

		#1
		new_state = State(state.m, state.c - 1, state.b + 1)


		if is_valid(new_state):
			successors.append(new_state)

		#2
		new_state = State(state.m, state.c - 2, state.b + 1)

		if is_valid(new_state):
			successors.append(new_state)

		#3
		new_state = State(state.m - 1, state.c, state.b + 1)

		if is_valid(new_state):
			successors.append(new_state)

		#4
		new_state = State(state.m - 2, state.c, state.b + 1)

		if is_valid(new_state):
			successors.append(new_state)

		#5
		new_state = State(state.m - 1, state.c - 1, state.b + 1)

		if is_valid(new_state):
			successors.append(new_state)

	else:
		print("b = 1")
		#1
		new_state = State(state.m, state.c + 1, state.b - 1)

		if is_valid(new_state):
			successors.append(new_state)

		#2
		new_state = State(state.m, state.c + 2, state.b - 1)

		if is_valid(new_state):
			successors.append(new_state)

		#3
		new_state = State(state.m + 1, state.c, state.b - 1)

		if is_valid(new_state):
			successors.append(new_state)

		#4
		new_state = State(state.m + 2, state.c, state.b - 1)

		if is_valid(new_state):
			successors.append(new_state)

		#5
		new_state = State(state.m + 1, state.c + 1, state.b - 1)

		if is_valid(new_state):
			successors.append(new_state)

	return successors



#Main
initial_state = State(3,3,0) #Setting up initial state
final_state = State(0,0,1) #Defining end state
s = nextState(initial_state)

for i in s:
	print(f"({i.m},{i.c},{i.b})")
