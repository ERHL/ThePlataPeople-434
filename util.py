from random import choice

Characters=['Perry the Platypus','Dave the Sloth']
Objectives=['has to slay a dragon','has to save the princess']
Settings=['swamp','ocean','mountain']
Tools=['jetpack','stick','hammer']

def char():
    return choice(Characters)+" "

def obj():
    return choice(Objectives)+" "

def setting():
    return "in a %s "%choice(Settings)

def tool():
    return "with a %s!"%choice(Tools)

def storyGen():
    return char()+obj()+setting()+tool()

#These functions pick a random item from the possible lists and combines it into a coherent 'story'

if __name__=='__main__':#Print 10 sentences if running this file on its own
    for i in range(10):
        print storyGen()
