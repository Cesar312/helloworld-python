from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date and time
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return f'Hello World! Current time: {formatted_now}'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
