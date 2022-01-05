from flask import Flask, request
from flask import render_template

app = Flask("Netflix generator")


@app.route("/erfassen")
def watchlist_empfehlung():
    return render_template('Filmerfassen.html', name="Netflix Filmgenerator")


@app.route("/erfassen", methods=['GET', 'POST'])
def erfassung_ausgeben():
    if request.method == 'GET':
        return render_template('Filmerfassen.html')
    if request.method == 'POST':
        erfasste_eingabe = request.form['filmname']
        rueckgabe_string = "Eingaben für " + erfasste_eingabe + " werden gespeichert und der Filmauswahl hinzugefügt!"
        return rueckgabe_string


@app.route("/vorschlagen")
def watchlist_vorschlag():
    return render_template('Filmvorschlag.html', vorschlag="Netflix Generator")


@app.route("/test")
def test():
    return "passt!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
