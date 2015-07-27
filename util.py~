from random import choice

Characters=['Perry the Platypus','Dave the Sloth']
Objectives=['has to slay a dragon','has to save the princess']
Settings=['swamp','ocean','mountain']
Tools=['jetpack','stick','hammer','afro','crowbar','sword','wrench','scythe','scimitar','slingshot','ammo']

current_tool='stick'

EVENTS=['A creepy old man starts following you']

def char():
    return choice(Characters)+" "

def obj():
    return choice(Objectives)+" "

def setting():
    return "in a %s "%choice(Settings)

def tool():
    return choice(Tools)

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
    return choice(EVENTS)

if __name__=='__main__':#Print 10 sentences if running this file on its own
    print current_tool
    store(tool())
    print current_tool
