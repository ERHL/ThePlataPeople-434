from flask import Flask, render_template
import util

app=Flask(__name__)

@app.route('/')
def root():
    return render_template('main.html',story=util.storyGen())


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

