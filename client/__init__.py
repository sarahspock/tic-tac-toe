from flask import Flask, render_template
import traceback
import sys

app = Flask(__name__)


@app.route("/")
def hello_world():
    try:
        return render_template("games/index.html")
    except:
        traceback.print_exc(file=sys.stdout)

if __name__ == '__main__':
    app.run(threaded=True)


