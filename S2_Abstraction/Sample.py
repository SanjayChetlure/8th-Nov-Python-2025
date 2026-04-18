from abc import ABC,abstractmethod

class Account(ABC):

    @abstractmethod
    def CD(self):
        pass

    @abstractmethod
    def CW(self):
        pass

class SBI(Account):
    def CD(self):
        print("SBI - CD limit: 1L")

    def CW(self):
        print("SBI - CW limit: 2L")

s=SBI()
s.CD()
s.CW()


