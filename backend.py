# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять его контентом.

from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def main_page():
    context = {
        'current_hour': int(datetime.now().strftime('%H')),
        'active_page': 'home'
    }
    return render_template("home.html", **context)

@app.route("/about/")
def about_page():
    return render_template("about.html", active_page='about')

if __name__ == "__main__":
    app.run()