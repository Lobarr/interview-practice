from problems.callCenter import Respondent, Manager, Director, CallCenter, Call
from algo.bitManipulation import insertion
from time import sleep
from random import randint

if __name__ == '__main__':
    respondant1 = Respondent()
    respondant2 = Respondent()
    respondant3 = Respondent()
    manager = Manager()
    manager2 = Manager()
    director = Director()
    director2 = Director()
    callCenter = CallCenter()

    for employee in [respondant1, respondant2, respondant3, manager, manager2, director, director2]:
      callCenter.addEmployee(employee)
    
    for i in range(100):
      newCall = Call()
      callCenter.dispatchCall(newCall)

    while callCenter._isProcessing():
      pass

    callCenter._stopEngine()
  