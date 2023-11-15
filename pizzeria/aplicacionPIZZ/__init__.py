from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Pizzería Ana la Rana, ¿qué quiere comer hoy?"

if __name__ == '__main__':
    app.run(debug=True)