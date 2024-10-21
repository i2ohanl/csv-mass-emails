from .abs_strategy import AbsStrategy
import pandas as pd
from email_logging import log

log = log()

class XlsxStrategy(AbsStrategy):
  def read_data(self, path):
    log.info('Reading XLSX data')
    return pd.read_excel(path)