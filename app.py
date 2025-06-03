from flask import Flask, render_template, url_for
from markupsafe import Markup
import markdown
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/members_raw')
def members_raw():
    path = os.path.join(os.path.dirname(__file__), "markdown_pages", "members.md")
    try:
        with open(path, "r", encoding="utf-8") as f:
            html = markdown.markdown(f.read())
        return Markup(html)
    except FileNotFoundError:
        return "<p><strong>Error:</strong> Member directory not found.</p>", 404

if __name__ == '__main__':
    app.run(debug=False)
