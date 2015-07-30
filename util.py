from random import choice

Characters=['Perry the Platypus','Dave the Sloth']
Objectives=['has to slay a dragon','has to save the princess']
Settings=['swamp','ocean','mountain','forest']
#name:[attack, speed, scavenging]
Tools={'jetpack':[0.5,4.0,2.0],'stick':[1.0,2.0,3.0],'hammer':[3.5,1.0,2.0],'afro':[-1.0,2.0,10.0],'crowbar':[1.5,2.5,3.5],'sword':[3.0,1.5,3.5],'scythe':[4.0,1.0,3.5],'slingshot':[1.0,3.0,2.0],'whip':[2.5,3.5,2.0],'mohawk':[4.5,2.0,0.0]}
#Items={'Health Potion mark 1':5.0,'Health Potion mark 2':10.0}
Items=['HPmk1','HPmk2']

#common_tools=['jetpack','stick','crowbar','slingshot']
common_tools={'jetpack':[0.5,4.0,2.0],'stick':[1.0,2.0,3.0],'crowbar':[1.5,2.5,3.5],'slingshot':[1.0,3.0,2.0]}
for i in common_tools.keys():
    for z in [' ','  ','   ']:
        Tools[i+z]=Tools[i]



current_tool={'stick':Tools['stick']}
current_health=10

#EVENTS={'A creepy old man starts following you':[1.0,1.5,-1.0,1.0],'A Zombie approaches you':[2.5,1.5,-1,3.0],'You find an abandoned grocery store':[0.0,0.0,3.0,0.0]}

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
#Stores the user's current tool that needs to be used later

def newEvent():
    event=choice({'You encounter an air elemental':[1.5,10.0,-1.0,2.0,'airele.jpg'],'A large bear jumps out of the trees':[3.0,2.0,-1.0,5.0,'bear.jpg'],'A creepy old man starts following you':[1.0,1.5,-1.0,1.0,'crazyold.jpg'],'A Zombie approaches you':[2.5,1.5,-1,3.0,'zombie.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You encounter an air elemental':[1.5,10.0,-1.0,2.0,'airele.jpg'],'A large bear jumps out of the trees':[3.0,2.0,-1.0,5.0,'bear.jpg'],'A creepy old man starts following you':[1.0,1.5,-1.0,1.0,'crazyold.jpg'],'A Zombie approaches you':[2.5,1.5,-1,3.0,'zombie.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You encounter an air elemental':[1.5,10.0,-1.0,2.0,'airele.jpg'],'A large bear jumps out of the trees':[3.0,2.0,-1.0,5.0,'bear.jpg'],'A creepy old man starts following you':[1.0,1.5,-1.0,1.0,'crazyold.jpg'],'A Zombie approaches you':[2.5,1.5,-1,3.0,'zombie.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'A pirate attacks you':[2.5,2.5,-1,3.5,'arr.jpg'],'An insane hipster challenges you':[2.0,6.5,-1,2.0,'hipster.jpg'],'You notice a boulder rolling towards you':[10.0,3.0,-1,100.0,'boulder.jpg'],'A baby dragon approaches you':[2.0,3.0,-1,7.5,'babydragon.jpg'],'You feel a sharp pricking':[2.0,5.0,-1,0.5,'vines.jpg'],'A pirate attacks you':[2.5,2.5,-1,3.5,'arr.jpg'],'An insane hipster challenges you':[2.0,6.5,-1,2.0,'hipster.jpg'],'You notice a boulder rolling towards you':[10.0,3.0,-1,100.0,'boulder.jpg'],'A baby dragon approaches you':[2.0,3.0,-1,7.5,'babydragon.jpg'],'You feel a sharp pricking':[2.0,5.0,-1,0.5,'vines.jpg'],'A wild platypus appears':[6.0,7.0,-1,1.0,'benji.jpg'],"Ultrax Blade, interdimensional overlord, appears from a tear in space-time and challenges you!":[9999.9,0.0,-1.0,9999.9,'ultraxlord.jpg']}.keys())
    Event={event:{'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You encounter an air elemental':[1.5,10.0,-1.0,2.0,'airele.jpg'],'A large bear jumps out of the trees':[3.0,2.0,-1.0,5.0,'bear.jpg'],'A creepy old man starts following you':[1.0,1.5,-1.0,1.0,'crazyold.jpg'],'A Zombie approaches you':[2.5,1.5,-1,3.0,'zombie.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You encounter an air elemental':[1.5,10.0,-1.0,2.0,'airele.jpg'],'A large bear jumps out of the trees':[3.0,2.0,-1.0,5.0,'bear.jpg'],'A creepy old man starts following you':[1.0,1.5,-1.0,1.0,'crazyold.jpg'],'A Zombie approaches you':[2.5,1.5,-1,3.0,'zombie.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'You encounter an air elemental':[1.5,10.0,-1.0,2.0,'airele.jpg'],'A large bear jumps out of the trees':[3.0,2.0,-1.0,5.0,'bear.jpg'],'A creepy old man starts following you':[1.0,1.5,-1.0,1.0,'crazyold.jpg'],'A Zombie approaches you':[2.5,1.5,-1,3.0,'zombie.jpg'],'You find an abandoned grocery store':[0.0,0.0,2.0,0.0,'grocery.jpg'],'A pirate attacks you':[2.5,2.5,-1,3.5,'arr.jpg'],'An insane hipster challenges you':[2.0,6.5,-1,2.0,'hipster.jpg'],'You notice a boulder rolling towards you':[10.0,3.0,-1,100.0,'boulder.jpg'],'A baby dragon approaches you':[2.0,4.0,-1,7.5,'babydragon.jpg'],'You feel a sharp pricking':[5.0,5.0,-1,5.0,'vines.jpg'],'A pirate attacks you':[2.5,2.5,-1,3.5,'arr.jpg'],'An insane hipster challenges you':[2.0,6.5,-1,2.0,'hipster.jpg'],'You notice a boulder rolling towards you':[10.0,3.0,-1,100.0,'boulder.jpg'],'A baby dragon approaches you':[2.0,3.0,-1,7.5,'babydragon.jpg'],'You feel a sharp pricking':[2.0,5.0,-1,0.5,'vines.jpg'],'A wild platypus appears':[4.0,3.0,-1,1.0,'benji.jpg'],"Ultrax Blade, interdimensional overlord, appears from a tear in space-time and challenges you!":[9999.9,0.0,-1.0,9999.9,'ultraxlord.jpg']}[event]}
    return Event
#Selects a new event from the list

def store_health(ch):
    global current_health
    current_health=ch

def get_health(ph):
    store_health(ph)
    return current_health
#Stores the user's current health that needs to be used later

