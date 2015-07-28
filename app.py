from flask import Flask, render_template, request, redirect
import util,random

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def root():
    global ch
    ch=100 #Sets health to 100
    tool=[]
    for i in range(3):
        tool.append(util.tool().keys()[0])#Makes a list of 3 random tools
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool, health=util.get_health(ch))
#Loads main.html with the variables filled in

@app.route('/event',methods=['POST','GET'])
def event():
    if 'item' in request.form:
        global ch
        heal=request.form['item']#If an item was just used, increases your health
        ch+=float(heal[-1])*5
        if ch>100:
            ch=100#Insures health does not go above 100
    else:
        global ct
        ct=util.get(request.form['tool'])
    if request.method=="POST":
        global act
        act=util.newEvent()#Makes a global variable with the current event
        return render_template('main.html',story=act.keys()[0],instruction='Use your tool or flee',ct=util.get(ct.keys()[0]),opt='yes',health=ch)
    elif request.method=="GET":#util.get() stores the current tool in util.py
        return 'GET'
    else:
        return 'yo'

@app.route('/newtool', methods=['POST','GET'])
def newtool():
    dif=0
    if request.form['choice']=='Run away':
        if act.values()[0][1]>ct.values()[0][1]:#If the user runs away and their speed is lower than the event's, they lose the difference between the event's speed and their speed, times 10
            global ch
            dif=(act.values()[0][1]-ct.values()[0][1])*10
            ch-=dif
    elif request.form['choice']=='Use tool':
        if act.values()[0][2]==-1:#If the event has no scavenging, and the user uses tool, and the user's attack is lower than the event's, then the user loses the difference between the event's attack and theirs
            if act.values()[0][0]>ct.values()[0][0]:
                global ch
                dif=(act.values()[0][0]-ct.values()[0][0])*10
                ch-=dif
        else:#If the event has scavenging (is a store) redirects user to /store route
            if act.values()[0][2]<=ct.values()[0][2]:
                return redirect('/store')
    if ch<=0:
        return render_template('lose.html')
    tool=[]
    for i in range(3):#Selects 3 new random tools
        tool.append(util.tool().keys()[0])
    return render_template('main.html',story='Pick a new tool',tools=tool,ct=util.get(ct.keys()[0]),health=ch,action="You lost %s health"%dif)

@app.route('/store')
def store():
    item=[]
    scav=ct.values()[0][2]-act.values()[0][2]#sets the value of scav to the user's scavenging minus the event's scavenging and generates that number of options for potions
    for i in range(int(scav)+1):
        item.append('HPmk'+str(i+1))
    return render_template('main.html',items=item,ct=util.get(ct.keys()[0]),health=ch)

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

