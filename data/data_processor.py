import strategies
from .data_context import DataContext
from email_logging import log

log = log()

class DataProcessor():
  def __init__(self, path):
    self._path = path
    self._setup_context()

  def _setup_context(self):
    extension = self._path.split('.')[-1]
    if extension == "csv":
      strategy = strategies.CsvStrategy
    elif extension == "xlsx":
      strategy = strategies.XlsxStrategy
    else:
      log.error('Error in processing data: File format unsupported')
      raise Exception(f'File format unsupported: {extension}. Please choose a .csv or .xlsx file')
    
    self._context = DataContext(strategy, self._path)