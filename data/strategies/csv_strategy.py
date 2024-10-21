from .abs_strategy import AbsStrategy
import pandas as pd
from email_logging import log

log = log()

class CsvStrategy(AbsStrategy):
  def read_data(self, path):
    log.info('Reading CSV data')
    return pd.read_csv(path)