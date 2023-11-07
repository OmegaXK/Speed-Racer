from flask import Flask, render_template 

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    """Speed Racer Home."""
    return render_template('home.html')

@app.route('/download')
def download():
    """Speed Racer Download."""
    return render_template('download.html')

@app.route('/credits')
def credits():
    """Speed Racer Credits."""
    return render_template('credits.html')

if __name__ == '__main__':
    app.run(port=5001)