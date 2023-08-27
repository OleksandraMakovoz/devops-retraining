from flask import Flask, render_template
import random
app = Flask(__name__)
# list of cat images
images = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXA1am15cGF5MDBnOThnMjZ2ODk5OGxlYjc1d3VwaTlvYWxkZW1lMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6Zt481isNVuQI1l6/giphy.gif",
    "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif",
    "https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/ES4Vcv8zWfIt2/giphy.gif",
    "https://media.giphy.com/media/MWSRkVoNaC30A/giphy-downsized-large.gif",
    "https://media.giphy.com/media/BBNYBoYa5VwtO/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/RhrAmVUHxjTQvEPBWi/giphy.gif",
    "https://media.giphy.com/media/12PA1eI8FBqEBa/giphy.gif",
    "https://media.giphy.com/media/TA6Fq1irTioFO/giphy.gif",
    "https://media.giphy.com/media/LtxpWeNNneL0A/giphy.gif"
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")