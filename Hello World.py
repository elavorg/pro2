from flask import Flask
from flask import render_template

app = Flask("Netflix generator")


@app.route("/erfassen")
def watchlist_empfehlung():
    return render_template('Filmerfassen.html', name="Netflix Filmgenerator")

@app.route("/vorschlagen")
def watchlist_vorschlag():
    return render_template('Filmvorschlag.html', vorschlag="Netflix Generator")

@app.route("/test")
def test():
    return "passt!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)



