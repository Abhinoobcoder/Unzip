# Copyright (c) 2022 - 2024 EDM115
import logging
import time
import socket
import threading

from pyrogram import Client
from pyromod import listen  # skipcq: PY-W2000

from config import Config

boottime = time.time()

plugins = dict(root="modules")
unzipperbot = Client(
    "UnzipperBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins,
    sleep_threshold=10,
    max_concurrent_transmissions=3,
)


# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
s.bind(('0.0.0.0', 10000))

# Listen for incoming connections
s.listen(5)

def handle_incoming_connections():
    while True:
        # Accept incoming connections
        conn, addr = s.accept()

        # Handle incoming requests
        request = conn.recv(1024)
        response = "HTTP/1.1 200 OK\n\nHello, world!"
        conn.sendall(response.encode())

        # Close the connection
        conn.close()

# Create a thread to handle incoming connections
t = threading.Thread(target=handle_incoming_connections)
t.start()

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler("unzip-log.txt"), logging.StreamHandler()],
    format="%(asctime)s - %(levelname)s - %(name)s - %(threadName)s - %(message)s",
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("asyncio").setLevel(logging.WARNING)
logging.getLogger("aiohttp").setLevel(logging.WARNING)
logging.getLogger("aiofiles").setLevel(logging.WARNING)
logging.getLogger("dnspython").setLevel(logging.WARNING)
logging.getLogger("GitPython").setLevel(logging.WARNING)
logging.getLogger("motor").setLevel(logging.WARNING)
logging.getLogger("Pillow").setLevel(logging.WARNING)
logging.getLogger("psutil").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
