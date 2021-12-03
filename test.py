from environment import Environment
from brain import Brain
import numpy as np

waitTime = 75
nLastStates = 4
filepathToOpen = 'model2.h5'

env = Environment(waitTime)
brain = Brain((env.nColumns, env.nRows, nLastStates))
model = brain.loadModel(filepathToOpen)


def resetStates():
    
    currentState = np.zeros((1, env.nColumns, env.nRows, nLastStates))
    
    for i in range(nLastStates):
        currentState[0, :, :, i] = env.screenMap
        
    return currentState, currentState

while True:
     
    env.reset()
    currentState, nextState = resetStates()
    gameOver = False
    while not gameOver: 
        qvalues = model.predict(currentState)[0]
        action = np.argmax(qvalues)
        
        frame, _, gameOver = env.step(action)
        
        frame = np.reshape(frame, (1, env.nColumns, env.nRows, 1))
        nextState = np.append(nextState, frame, axis = 3)
        nextState = np.delete(nextState, 0, axis = 3)
        
        currentState = nextState

