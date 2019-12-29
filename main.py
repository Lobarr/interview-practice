from problems.callCenter import Respondent, Manager, Director, CallCenter, Call
from algo.bitManipulation import insertion
from random import randint

if __name__ == '__main__':
    respondant = Respondent()
    manager = Manager()
    director = Director()
    callCenter = CallCenter()

    for employee in [respondant, manager, director]:
      callCenter.addEmployee(employee)
    
    for i in range(100):
      newCall = Call()
      callCenter.dispatchCall(newCall)
    

