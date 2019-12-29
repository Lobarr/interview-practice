from problems.callCenter import Respondent, Manager, Director, CallCenter, Call
from algo.bitManipulation import insertion
from random import randint

if __name__ == '__main__':
    respondant1 = Respondent()
    respondant2 = Respondent()
    manager = Manager()
    director = Director()
    callCenter = CallCenter()

    for employee in [respondant1, respondant2, manager, director]:
      callCenter.addEmployee(employee)
    
    for i in range(100):
      newCall = Call()
      callCenter.dispatchCall(newCall)

    callCenter._stopEngine()
    
