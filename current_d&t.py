from flask import Flask
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def current_time():
    return f"Текущие дата и время: {datetime.now().strftime('%d.%m.%Y - %H:%M:%S')}"

if __name__ == "__main__":
    app.run()