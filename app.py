from flask import Flask, render_template, request, redirect
import util,random

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def root():
    global event_number
    event_number=0
    global ch
    ch=100.0 #Sets health to 100
    tool=[]
    for i in range(3):
        tool.append(util.tool().keys()[0])#Makes a list of 3 random tools
    return render_template('main.html',story='Dave the superstar sloth has to save the princess in a forest.',instruction='What tool do you pick up?',tools=tool, health=util.get_health(ch))
#Loads main.html with the variables filled in


@app.route('/inv',methods=['POST','GET'])
def useItem():
    if inv==[]:
        inv.append("HPmk0")
    if request.method=="POST":
        global ch
        heal=request.form['itemUsed']#If an item was just used, increases your health
        inv.remove(heal)
        restore=float(heal[-1])*5
        if restore != 0:
            ch+=restore+5
        if ch>100.0:
            ch=100.0#Insures health does not go above 100
        global itemUsed
        itemUsed=True
        return redirect("/fight")
    elif request.method=="GET":
        return render_template('main.html',itemInv=inv,ct=util.get(ct.keys()[0]).keys()[0],health=ch,enmHealth=(act.values()[0][3])*10)

@app.route('/event',methods=['POST','GET'])
def event():
    if 'item' in request.form:
        global ch
        heal=request.form['item']#If an item was just used, increases your health
        ch+=float(heal[-1])*5
        if ch>100.0:
            ch=100.0#Insures health does not go above 100
    else:
        global ct
        ct=util.get(request.form['tool'])
    if request.method=="POST":
        global act
        act={}
        act=util.newEvent()#Makes a global variable with the current event
        return render_template('main.html',story=act.keys()[0],instruction='Use your tool or flee',ct=util.get(ct.keys()[0]).keys()[0],opt='yes',health=ch,enmHealth=(act.values()[0][3])*10)
    elif request.method=="GET":#util.get() stores the current tool in util.py
        return redirect('/')
    else:
        return 'yo'

@app.route('/newtool', methods=['POST','GET'])
def newtool():
    if request.method=='GET':
        return rediect('/')
    if event_number>=15:
        return redirect('/final')
    global dif
    dif=0
    if request.form['choice']=='Run away':
        if act.values()[0][1]>ct.values()[0][1]:#If the user runs away and their speed is lower than the event's, they lose the difference between the event's speed and their speed, times 10
            global ch
            dif=(act.values()[0][1]-ct.values()[0][1])*10
            ch-=dif
    elif request.form['choice']=='Use tool':
        if act.values()[0][2]==-1:#If the event has no scavenging (is a fight), and the user uses tool, redirects to route "/fight"
            return redirect("/fight")
        else:#If the event has scavenging (is a store) redirects user to /store route
            if act.values()[0][2]<=ct.values()[0][2]:
                return redirect('/store')
    if ch<=0:
        return render_template('lose.html')
    tool=[]
    for i in range(3):#Selects 3 new random tools
        tool.append(util.tool().keys()[0])
    tool.append(ct.keys()[0])
    return render_template('main.html',story='Pick a new tool',tools=tool,ct=util.get(ct.keys()[0]).keys()[0],health=ch,enmHealth=(act.values()[0][3])*10,action="You lost %s health"%dif)

@app.route('/store')
def store():
    item=[]
    scav=ct.values()[0][2]-act.values()[0][2]#sets the value of scav to the user's scavenging minus the event's scavenging and generates that number of options for potions
    item.append('HPmk0')
    for i in range(int(scav)+1):
        item.append("HPmk"+str(i+1))
    return render_template('main.html',items=item,ct=util.get(ct.keys()[0]).keys()[0],health=ch,enmHealth=(act.values()[0][3])*10)

@app.route("/fight")
def fight():
    if act.values()[0][0]>ct.values()[0][0]:
        global ch
        dif=(act.values()[0][0]-ct.values()[0][0])*10
        ch-=dif
    else:
        ch-=5
    enmDif=0
    enmDif=(ct.values()[0][0]-act.values()[0][0])+0.5
    if enmDif<0.5:
        enmDif=0.5
    act.values()[0][3]-=enmDif
    if ch<=0:
        return render_template('lose.html')
    elif act.values()[0][3]>0:
        return render_template('main.html',story=act.keys()[0],instruction='Use your tool or flee',ct=util.get(ct.keys()[0]).keys()[0],opt='yes',health=ch,enmHealth=(act.values()[0][3])*10)
    else:
        tool=[]
        for i in range(3):#Selects 3 new random tools
            tool.append(util.tool().keys()[0])
        global event_number
        event_number+=1
        if event_number>=15:
            return redirect('/final')
        tool.append(ct.keys()[0])
        return render_template('main.html',story='Pick a new tool',tools=tool,ct=util.get(ct.keys()[0]).keys()[0],health=ch,action="You win!",enmHealth=0.0)


@app.route('/final',methods=['POST','GET'])
def final():
    try:
        ct
    except NameError:
        return redirect('/')
    act={'Dragon':[3.0,3.0,-1,25.0]}
    if request.method=='GET':
        global ct
        global dh
        dh=act.values()[0][3]
        return render_template('final.html',health=ch,tool=ct,opt='yes',message='yes',enmHealth=dh*10)
    elif request.method=='POST':
        global ch
        global ct
        dif=0
        if request.form['choice']=='Run away':
            if act.values()[0][1]>ct.values()[0][1]:#If the user runs away and their speed is lower than the event's, they lose the difference between the event's speed and their speed, times 10
                global ch
                dif=(act.values()[0][1]-ct.values()[0][1])*10
                ch-=dif
        elif request.form['choice']=='Use tool':#If the user uses tool, and the user's attack is lower than the event's, then the user loses the difference between the event's attack and theirs
            if act.values()[0][0]>ct.values()[0][0]:
                global ch
                dif=(act.values()[0][0]-ct.values()[0][0])*10
                ch-=dif
            else:
                enmDif=0
                enmDif=(ct.values()[0][0]-act.values()[0][0])+0.5
                if enmDif<0.5:
                    enmDif=0.5
                global dh
                dh-=enmDif
        if ch<=0:
            return render_template('lose.html')
        elif dh<=0:
            return render_template("final.html",killDrag='yes')
        return render_template('final.html',health=ch,tool=ct,message='yes',opt='yes',enmHealth=dh*10,killDrag='no')

@app.route('/<url>')
def error(url):
    return redirect('/')


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

