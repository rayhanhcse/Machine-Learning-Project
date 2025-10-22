import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = "logs"  # Same directory as demo.py

os.makedirs(LOG_DIR, exist_ok=True)

LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logging.info("✅ Logger is working fine!")
print(f"Log file created at: {LOG_PATH}")
