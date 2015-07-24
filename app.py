from flask import Flask, render_template, request
import util,random

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def root():
    tool=[]
    for i in range(3):
        tool.append(util.tool())
    #if random.random()<.1:
        #return render_template('final.html')
    #else:
    if request.method=="GET":
        return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool, ct='')
    elif request.method=="POST":
        return render_template('main.html',story=util.newEvent(),instruction='Use your tool or flee',ct=util.get(request.form['tool']))
    else:
        return 'yo'


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

