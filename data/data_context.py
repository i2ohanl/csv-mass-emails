from strategies import AbsStrategy
from email_logging import log

class DataContext():
  def __init__(self, strategy: AbsStrategy, path: str = None):
    self.set_strategy(strategy)
    self._path = path

  def set_strategy(self, strategy: AbsStrategy):
    self._strategy = strategy()

  def execute_strategy(self):
    try:
      data = self._strategy.read_data(self._path)
      log.info('Data read successful')
      return data
    except Exception:
      log.error(f'Error occured in reading data: {Exception}')
      return Exception(f'Error occured in reading data: {Exception}')