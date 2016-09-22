from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello C4E6!'

@app.route('/school')
def school():
    return redirect("http://techkids.vn/")

if __name__ == '__main__':
    app.run()
