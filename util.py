from random import choice

Characters=['Perry the Platypus','Dave the Sloth']
Objectives=['has to slay a dragon','has to save the princess']
Settings=['swamp','ocean','mountain']
#name:[attack, speed, charisma]
Tools={'jetpack':[0.5,4.0,2.0],'stick':[1.0,2.0,0.0],'hammer':[2.5,1.0,1.0],'afro':[-1.0,2.0,6.0],'crowbar':[1.5,2.5,1.5],'sword':[3.0,1.5,2.5],'scythe':[4.0,1.0,-1],'slingshot':[1.0,3.0,0.5]}

current_tool='stick'
current_health=10

EVENTS={'A creepy old man starts following you':[1.0,1.0,-1.0]}

def char():
    return choice(Characters)+" "

def obj():
    return choice(Objectives)+" "

def setting():
    return "in a %s "%choice(Settings)

def tool():
    Tool={choice(Tools.keys()):Tools[choice(Tools.keys())]}
    return Tool

def storyGen():
    return char()+obj()+setting()+tool()

#These functions pick a random item from the possible lists and combines it into a coherent 'story'
def store(ct):
    global current_tool
    current_tool=ct

def get(pt):
    store(pt)
    return current_tool

def newEvent():
    event={choice(EVENTS.keys()):Tools[choice(EVENTS.keys())]}
    return event

def store_health(ch):
    global current_health
    current_health=ch

def get_health(ph):
    store_health(ph)
    return current_health

if __name__=='__main__':#Print 10 sentences if running this file on its own
    print current_tool
    store(tool())
    print current_tool
