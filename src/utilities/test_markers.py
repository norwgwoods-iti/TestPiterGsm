import logging
from datetime import datetime
import re

logger = logging.getLogger(__name__)


_ESCAPE_RE = re.compile(r'\\u([0-9a-fA-F]{4})|\\U([0-9a-fA-F]{8})|\\x([0-9a-fA-F]{2})')


def _unescape_pytest_id(s: str) -> str:
    """Разворачивает \\uXXXX / \\UXXXXXXXX / \\xXX, которые pytest оставляет в nodeid."""
    def repl(m):
        hex_val = m.group(1) or m.group(2) or m.group(3)
        return chr(int(hex_val, 16))
    return _ESCAPE_RE.sub(repl, s)

def log_test_start(method: str, test_name: str | None = None):
    test_name = test_name or method           # ← если не передали, берём method
    logger.info(
        '-------\n'
        'Test name: %s\n'
        'Start time: %s\n'
        
        '-------',
        _unescape_pytest_id(test_name),
        datetime.now().strftime('%Y.%m.%d %H-%M-%S'),

    )


def log_test_end(method: str, current_url: str, test_name: str | None = None):
    logger.info(
        '-------\n'
        'End time: %s\n'
        'End test name: %s\n'
        
        'URL: %s\n'
        '-------',
        datetime.now().strftime('%Y.%m.%d %H-%M-%S'),
        _unescape_pytest_id(test_name or method),

        current_url,
    )