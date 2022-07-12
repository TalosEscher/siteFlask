from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<user>")
def usuarios(user):
    return render_template("usuarios.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)

    