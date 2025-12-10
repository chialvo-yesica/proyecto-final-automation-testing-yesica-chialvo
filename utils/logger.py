import logging
from pathlib import Path
from config.settings import REPORTS_FOLDER

LOG_OUTPUT_FILE = REPORTS_FOLDER / "automation_events.log"

#Devuelve una instancia de logger configurada
def setup_logger(log_name: str = "default_log") -> logging.Logger:
    logger_instance = logging.getLogger(log_name)

    if not logger_instance.handlers:
        logger_instance.setLevel(logging.INFO)

        log_format = logging.Formatter(
            "[%(asctime)s] - %(levelname)s - (%(name)s) - MSG: %(message)s", 
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Handler para archivo
        file_writer = logging.FileHandler(LOG_OUTPUT_FILE, encoding="utf-8")
        file_writer.setFormatter(log_format)

        # Handler para consola
        console_writer = logging.StreamHandler()
        console_writer.setFormatter(log_format)

        logger_instance.addHandler(file_writer)
        logger_instance.addHandler(console_writer)

    return logger_instance