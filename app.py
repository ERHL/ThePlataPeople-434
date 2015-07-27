from flask import Flask, render_template, request, redirect
import util,random

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def root():
    global ch
    ch=100
    tool=[]
    for i in range(3):
        tool.append(util.tool().keys()[0])
    #if random.random()<.1:
        #return render_template('final.html')
    #else:
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool, health=util.get_health(ch))

@app.route('/event',methods=['POST','GET'])
def event():
    if 'item' in request.form:
        global ch
        heal=request.form['item']
        ch+=float(heal[-1])*5
        if ch>100:
            ch=100
    else:
        global ct
        ct=util.get(request.form['tool'])
    if request.method=="POST":
        global act
        act=util.newEvent()
        return render_template('main.html',story=act.keys()[0],instruction='Use your tool or flee',ct=util.get(ct.keys()[0]),opt='yes',health=ch)
    elif request.method=="GET":
        return 'GET'
    else:
        return 'yo'

@app.route('/newtool', methods=['POST','GET'])
def newtool():
    dif=0
    if request.form['choice']=='Flee':
        if act.values()[0][1]>ct.values()[0][1]:
            global ch
            dif=(act.values()[0][1]-ct.values()[0][1])*10
            ch-=dif
    elif request.form['choice']=='Tool':
        if act.values()[0][2]==-1:
            if act.values()[0][0]>ct.values()[0][0]:
                global ch
                dif=(act.values()[0][0]-ct.values()[0][0])*10
                ch-=dif
        else:
            if act.values()[0][2]<=ct.values()[0][2]:
                return redirect('/store')
    if ch<=0:
        return render_template('lose.html')
    tool=[]
    for i in range(3):
        tool.append(util.tool().keys()[0])
    return render_template('main.html',story='Pick a new tool',tools=tool,ct=util.get(ct.keys()[0]),health=ch,action="You lost %s health"%dif)

@app.route('/store')
def store():
    item=[]
    scav=ct.values()[0][2]-act.values()[0][2]
    for i in range(int(scav)+1):
        item.append(util.item())
    return render_template('main.html',items=item,ct=util.get(ct.keys()[0]),health=ch)

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

