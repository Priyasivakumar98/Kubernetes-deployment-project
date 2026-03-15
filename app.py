from flask import Flask

app = Flask(__name__)

@app.route("/")
def devops():
    return "Hello Devops - Welcome to my CI/CD Pipeline Project"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
