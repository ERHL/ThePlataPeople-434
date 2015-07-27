from flask import Flask, render_template, request
import util,random

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def root():
    global ch
    ch=10
    tool=[]
    for i in range(3):
        tool.append(util.tool())
    #if random.random()<.1:
        #return render_template('final.html')
    #else:
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool, health=util.get_health(10))

@app.route('/event',methods=['POST','GET'])
def event():
    global ct
    ct=util.get(request.form['tool'])
    if request.method=="POST":
        global act
        act=util.newEvent()
        return render_template('main.html',story=act,instruction='Use your tool or flee',ct=util.get(ct),opt='yes',health=ch,)
    elif request.method=="GET":
        return 'GET'
    else:
        return 'yo'

@app.route('/newtool', methods=['POST','GET'])
def newtool():
    if request.form['choice']=='Flee':
        if EVENTS[act][1]>=Tools[ct][1]:
            global ch
            ch-=EVENTS[act][1]-Tools[ct][1]
            if ch<=0:
                return render_template('lose.html')
    tool=[]
    for i in range(3):
        tool.append(util.tool())
    return render_template('main.html',story='Pick a new tool',tools=tool,ct=util.get(ct),health=ch)

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

