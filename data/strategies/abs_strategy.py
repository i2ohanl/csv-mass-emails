from abc import ABC, abstractmethod

class AbsStrategy(ABC):
  
  @abstractmethod
  def read_data(self, path):
    pass
