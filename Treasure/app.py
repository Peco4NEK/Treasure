from flask import Flask, render_template, request, jsonify, redirect, url_for


app = Flask(__name__)

# Главная страница
@app.route("/main")
@app.route("/")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(port=5000)
