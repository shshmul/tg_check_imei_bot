# main.py
from api import app
from bot import main as run_bot
from threading import Thread

if __name__ == '__main__':
    Thread(target=lambda: app.run(port=5000)).start()
    run_bot()
