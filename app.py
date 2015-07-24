from flask import Flask, render_template
import util

app=Flask(__name__)

@app.route('/')
def root():
    tool=[]
    for i in range(3):
        tool.append(util.tool())
        print tool
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool)


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

