from flask import Flask, render_template, request
import mensagens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome").title()
        mensagem = f"Olá {nome}!\nMensagem: {mensagens.obterMensagemAleatoria ()}"
        return render_template("index.html", texto=mensagem)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)