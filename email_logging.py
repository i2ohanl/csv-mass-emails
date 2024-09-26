class log:
    def __init__(self):
        self.prefixes = {
            'info': "[INFO]",
            'debug': "[DEBUG]",
            'warning': "[WARN]",
            'error': "[ERROR]",
            'email_sent': "[EMAIL SENT]"
        }

    def _prefix_string(self, level, *messages):
        formatted_message = ' '.join(map(str, messages))
        return f"{self.prefixes.get(level, '[UNKNOWN]')} {formatted_message}"

    def info(self, *messages):
        print(self._prefix_string('info', *messages))

    def debug(self, *messages):
        print(self._prefix_string('debug', *messages))

    def warning(self, *messages):
        print(self._prefix_string('warning', *messages))

    def error(self, *messages):
        print(self._prefix_string('error', *messages))

    def email_sent(self, *messages):
        print(self._prefix_string('email_sent', *messages))
    
