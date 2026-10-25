import logging
from datetime import datetime
from pathlib import Path

def setup_logging(log_dir: Path) -> Path:
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / f'log_{datetime.now():%Y-%m-%d_%H-%M-%S}.log'

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s [%(levelname)8s] (%(name)s:%(lineno)s) -> %(message)s',
    ))

    logging.getLogger().addHandler(file_handler)

    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)

    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('selenium').setLevel(logging.WARNING)

    return log_file