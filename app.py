from flask import Flask, render_template
import util

app=Flask(__name__)

@app.route('/')
def root():
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest')


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

