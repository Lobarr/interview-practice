from enum import Enum
from uuid import uuid4
from queue import Queue

class EmployeeStatus(Enum):
  BUSY = 1
  FREE = 2


class EscalationLevel(Enum):
  Respondent = 1
  Manager = 2
  Director = 3


class Call:
  def __init__(self):
    self.id = uuid4().hex
    self.escalationLevel = EscalationLevel.Respondent

  def getId(self):
    return self.id

  def getEscalationLevel(self):
    return self.escalationLevel

  def setEscalationLevel(self, escalationLevel: EscalationLevel):
    self.escalationLevel = escalationLevel

  def escalate(self):
    if self.getEscalationLevel() == EscalationLevel.Respondent:
      self.setEscalationLevel(EscalationLevel.Manager)
    elif self.getEscalationLevel() == EscalationLevel.Manager:
      self.setEscalationLevel(EscalationLevel.Director)
    else:
      self.setEscalationLevel(EscalationLevel.Respondent)

    print('Call escalated')


class Employee:
  def __init__(self):
    self.status = EmployeeStatus.FREE

  def getStatus(self):
    return self.status

  def getType(self):
    return 'base'

  def setStatus(self, status: EmployeeStatus):
    self.status = status

  def handleCall(self, call: Call):
    self.setStatus(EmployeeStatus.BUSY)
    print(f'Call {call.getId()} handled by {self.getType()}')
    self.setStatus(EmployeeStatus.FREE)

  def isFree(self):
    return self.getStatus() == EmployeeStatus.FREE


class Respondent(Employee):
  def __init__(self):
    Employee.__init__(self)

  def getType(self):
    return 'Respondant'


class Manager(Employee):
  def __init__(self):
    Employee.__init__(self)

  def getType(self):
    return 'Manager'


class Director(Employee):
  def __init__(self):
    Employee.__init__(self)

  def getType(self):
    return 'Director'


class CallCenter:
  def __init__(self):
    self.respondents = Queue()
    self.managers = Queue()
    self.directors = Queue()

  def addEmployee(self, employee):
    if isinstance(employee, Respondent):
      self.respondents.put(employee)
    elif isinstance(employee, Manager):
      self.managers.put(employee)
    else:
      self.directors.put(employee)

  def _getNextEmployee(self, employeeQueue: Queue):
    return None if employeeQueue.empty() else employeeQueue.get()

  def getNextRespondant(self):
    return self._getNextEmployee(self.respondents)

  def getNextManager(self):
    return self._getNextEmployee(self.managers)

  def getNextDirector(self):
    return self._getNextEmployee(self.directors)

  def _handleCall(self, nextEmployee, call):
    if not nextEmployee:
      call.escalate()
      self.dispatchCall(call)
    else:
      nextEmployee.handleCall(call)
      self.addEmployee(nextEmployee)

  def dispatchCall(self, call: Call):
    if call.getEscalationLevel() == EscalationLevel.Respondent:
      nextRespondent = self.getNextRespondant()
      self._handleCall(nextRespondent, call)
    elif call.getEscalationLevel() == EscalationLevel.Manager:
      nextManager = self.getNextManager()
      self._handleCall(nextManager, call)
    else:
      nextDirector = self.getNextDirector()
      self._handleCall(nextDirector, call)

