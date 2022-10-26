from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey our first take on Flask \n Jaivignesh \n James Prince \n Venugoapl \n Jayasurya'

app.run(host='0.0.0.0', port=81)
