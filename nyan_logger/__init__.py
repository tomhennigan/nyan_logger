import logging
from .nyan import infinite_nyan

nyan_colors = {
    ' ': "\033[48;5;17m",  # Blue background
    ',': "\033[0m",  # Reset styles.
    '.': "\033[48;5;15m",  # White stars
    "'": "\033[48;5;0m",  # Black border
    '@': "\033[48;5;230m",  # Tan poptart
    '$': "\033[48;5;175m",  # Pink poptart
    '-': "\033[48;5;162m",  # Red poptart
    '>': "\033[48;5;9m",  # Red rainbow
    '&': "\033[48;5;202m",  # Orange rainbow
    '+': "\033[48;5;11m",  # Yellow Rainbow
    '#': "\033[48;5;10m",  # Green rainbow
    '=': "\033[48;5;33m",  # Light blue rainbow
    ';': "\033[48;5;19m",  # Dark blue rainbow
    '*': "\033[48;5;8m",  # Gray cat face
    '%': "\033[48;5;175m",  # Pink cheeks
}


class NyanFormatter(logging.Formatter):

    def __init__(self, rainbow_length=2):
        super(NyanFormatter, self).__init__()
        self.animation = infinite_nyan(rainbow_length)

    def format(self, record):
        """Formats a log record with the backgound color of each character set
        as the corresponding pixel of the current row of the nyan cat
        animation.

        :param record: the record to format
        :returns: the formatted string message.
        :rtype: string
        """

        log_message = logging.Formatter.format(self, record)

        # Split the log message on line breaks.
        msgs = log_message \
            .replace('\r', '\n') \
            .rstrip('\n') \
            .split('\n')

        lines = []
        for msg in msgs:
            msg = iter(msg)

            # Turn msg into line by combining the animation coloring for each
            # "pixel" in the row with it's corresponding character in msg.
            line = ''
            for pixel in next(self.animation):
                try:
                    character = next(msg)
                except StopIteration:
                    character = ' '

                line += (nyan_colors[pixel] + character)

            # Append any additional chars from the message.
            for character in msg:
                line += character

            # Reset formatting.
            line += '\033[0m'

            lines.append(line)

        log_message = '\n'.join(lines)
        setattr(record, 'msg', log_message)

        return log_message
