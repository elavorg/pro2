from flask import Flask
from flask import render_template

app = Flask("Netflix generator")


@app.route("/generator")
def watchlist_empfehlung():
    return render_template('index.html', name="Netflix Generator")

@app.route("/test")
def test():
    return "passt!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)



