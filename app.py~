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
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool, ct='')

@app.route('/event',methods=['POST'])
def event():
    global ct
    ct=util.get(request.form['tool'])
    if request.method=="POST":
        return render_template('main.html',story=util.newEvent(),instruction='Use your tool or flee',ct=util.get(ct),opt='yes')
    else:
        return 'yo'

@app.route('/newtool')
def newtool():
    tool=[]
    for i in range(3):
        tool.append(util.tool())
    return render_template('main.html',story='Pick a new tool',tools=tool,ct=util.get(ct))

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

