from flask import Flask, render_template
from os import environ

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/'

@app.route('/')
def show_love():
    love = environ.get('LOVE')
    if love == 'mills':
        return render_template('love.html', img='mills')
    elif love == 'tulips':
        return render_template('love.html', img='tulips')
    else:
        return render_template('love.html', img='clogs')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)