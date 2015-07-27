from random import choice

Characters=['Perry the Platypus','Dave the Sloth']
Objectives=['has to slay a dragon','has to save the princess']
Settings=['swamp','ocean','mountain','forest']
#name:[attack, speed, scavenging]
Tools={'jetpack':[0.5,4.0,2.0],'stick':[1.0,2.0,3.0],'hammer':[3.5,1.0,2.0],'afro':[-1.0,2.0,10.0],'crowbar':[1.5,2.5,3.5],'sword':[3.0,1.5,3.5],'scythe':[4.0,1.0,2.5],'slingshot':[1.0,3.0,2.0]}
#Items={'Health Potion mark 1':5.0,'Health Potion mark 2':10.0}
Items=['HPmk1','HPmk2']

current_tool={'stick':Tools['stick']}
current_health=10

EVENTS={'A creepy old man starts following you':[1.0,1.5,-1.0],'A Zombie approaches you':[2.5,1.5,-1],'Grocery Store':[0.0,0.0,3.0]}

def char():
    return choice(Characters)+" "

def obj():
    return choice(Objectives)+" "

def setting():
    return "in a %s "%choice(Settings)

def tool():
    tool=choice(Tools.keys())
    Tool={tool:Tools[tool]}
    return Tool

def storyGen():
    return char()+obj()+setting()+tool()

def item():
    return choice(Items)
#These functions pick a random item from the possible lists and combines it into a coherent 'story'


def store(ct):
    global current_tool
    current_tool={str(ct):Tools[str(ct)]}

def get(pt):
    store(pt)
    return current_tool

def newEvent():
    event=choice(EVENTS.keys())
    Event={event:EVENTS[event]}
    return Event

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
