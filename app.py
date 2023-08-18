from flask import Flask, url_for, render_template
import os


app = Flask(__name__)


class Sound:
    def __init__(self, filename):
        self.name = filename
        self.url = url_for('static', filename=filename)


@app.route('/')
def main():
    urls = []

    for filename in os.listdir('./static/sounds'):
        if filename.lower().endswith('.mp3'):
            urls.append(Sound(filename))

    return render_template('site.html', sounds=urls)


if __name__ == '__main__':
    app.run()
