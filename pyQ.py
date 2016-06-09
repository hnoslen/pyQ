import numpy as np

class pyQ:
	weights = np.array([])
	gamma = 0.5
	def initialWeights(self,adjacencyMatrix):
		self.weights = -1*(adjacencyMatrix==0)
		return self.weights

	def actions(self, state):
		return np.arange(self.weights[state].size)[self.weights[state]>0)]

	def bestAction(self, state):
		poss = self.actions(state)
		if poss.size == 0:
			return None
		else:
			possvals = self.weights[state][poss]
			return poss[possvals.max()==possvals]

	def updateWeights(self, state, action, reward):
		if self.weights[state,action]<0:
			print "Invalid action"
			return
		else:
			self.weights[state,action] = reward + self.gamma*(self.weights[action][self.actions(action)].max())
		return self.weights

	def randomAction(self, state):
		poss = self.actions(state)
		if poss.size == 0:
			return None
		else:
			return poss[np.floor(poss.size*np.random.random())]

