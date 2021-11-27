from enviroment import Environment 
from brain import Brain
from dqn import Dqn
import numpy as np
import matplotlib.pyplot as pit

#Defining the parameters
learningRate = 0.0001
maxMemory = 60000
gamma = 0.9
batchSize = 32
nLastStates = 4

epsilon = 1.
epsilonDecayRate= 0.0002
minEpsilon = 0.05

filepathToSave = 'model2.h5'

#Initializing the Environment, the Brain and the Experience Replay Memory
env = Environment(0)
brain = Brain((env.nColumns, env.nRows, nLastStates), learningRate)
model = Brain.model
DQN = Dqn(maxMemory, gamma)

#Building a function that will reset current state and next state
def resetStates():
    
    currentState = np.zeros((1, env.nColumns, env.nRows, nLastStates))
    
    for i in range(nLastStates):
        currentState[0, :, :, i] = env.screenMap
        
    return currentState, currentState


        
