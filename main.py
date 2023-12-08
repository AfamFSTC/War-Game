from deck import MyGame
a=MyGame()
aa=0
bb=0
print(a.manual('''

'''))
shoot={'jet stream':210,'penguin god and devil':200,'golden gull':130,'daruma boomer':120,'patriot shoot':40,'fire tornado':100,'fireball storm':130,'triangle z':100,'penguin volley':100,'perfect penguin':120,'the detonator':120,'meteor strike':110,'rabbit run':110,'tripple blizzard':120,'polar bear no.2':150,'emperor penguin no.2':155,'royal lancer':165,'death zone':130,'ursa rager':120,'cold front':110,'fire lemonade':180,'flying colors':160,'ninja frog':110,'god alone knows':120,'inazuma three':130}
dribble={'circuit charge':120,'flash dash':130,'sparky spin':130,'zoom dash':135,'sky walker':140,'divine dummy':120,'zoned out':145,'omega maelstrom':160}
defence={'the wall':120,'wall for one':160,'wind trapper':100,'ursa bear stopper':160,'frakenstun':100,'tiki header':100}
keep={'splash guard':50,'drill puncher':120,'mermaid spell':130,'lunar eclipse':130,'savage beast fang':100,'worm hole':120,'majin the hand':120,'mega majin':150,'god hand':100,'descerator':100,'fur trapper':80,'diamond hand':200}
players={'mark evans':130,'shawn froste':110,'aiden froste':130,'xavier schiller':110,'hunter foster':130,'bryon love':110,'david samford':130,'nathan swift':110,'axel blade':130,'heath moore':110,'duske grayling':130,'elliot ember':110,'jude sharp':130,'basile hardy':110,'sonny wright':130}
opposition={'sandra fischer':100,'adriano donati':80,'oscar pio':90,'mickey way':100,'reid rivers':80,'solomon owle':90,'toby damian':90,'alfred meenan':100,'caleb stonewall':99,'apollo light':90,'ben blowton':80,'jack sawyer':60}
opposition2={'sandra fischer':110,'adriano donati':110,'oscar pio':120,'mickey way':130,'reid rivers':110,'solomon owle':110,'toby damian':120,'alfred meenan':130,'caleb stonewall':110,'apollo light':110,'ben blowton':120,'jack sawyer':130}
oppname='Opponent'
keeps=['splash guard','drill puncher','mermaid spell','lunar eclipse','savage beast fang','worm hole','majin the hand','mega majin','god hand','descerator','fur trapper','diamond hand']
shoots=['penguin god and devil','golden gull','daruma boomer','patriot shoot','fire tornado','fireball storm','triangle z','penguin volley','perfect penguin','the detonator','meteor strike','rabbit run','tripple blizzard','polar bear no.2','emperor penguin no.2','royal lancer','death zone','ursa rager','cold front','fire lemonade','flying colors','ninja frog','god alone knows','inazuma three']
shoots2=['penguin god and devil','golden gull','daruma boomer','patriot shoot','fire tornado','fireball storm','triangle z','penguin volley','perfect penguin','the detonator','meteor strike','rabbit run','tripple blizzard','polar bear no.2','emperor penguin no.2','royal lancer','death zone','ursa rager','cold front','fire lemonade','flying colors','ninja frog','god alone knows','inazuma three']
shoots3=['jet stream','penguin god and devil','the detonator','meteor strike','tripple blizzard','polar bear no.2','emperor penguin no.2','royal lancer','death zone','fire lemonade','flying colors','ninja frog','inazuma three']
dribbles=['circuit charge','flash dash','sparky spin','zoom dash','sky walker','divine dummy']
defences=['the wall','wall for one','wind trapper','ursa bear stopper','frakenstun','tiki header']
player=['mark evans','shawn froste','aiden froste','xavier schiller','hunter foster','bryon love','david samford','nathan swift','axel blade','heath moore','duske grayling','elliot ember','jude sharp','basile hardy','sonny wright']
goal_or_not=[0,1]
goal_text=['and he has scored a beauty','and it is a goal','goallllllllllllllllllllllllllll']
dribble_text=['awww nasty dribbling given there', 'and he dribbled him badly and goes away with the ball','woww what a dribble']
defence_text=['oh nobody can pass through that defence','a walllll !!!','what a wall !!!']
oppositions=['sandra fischer','adriano donati','oscar pio','mickey way','reid rivers','solomon owle','toby damian','alfred meenan','caleb stonewall','apollo light','ben blowton','jack sawyer']
pass_text=['a straight pass given','what a flawless pass there','clean pass there clearly given nice pass']
teamname=input('teamname:')
b=input('what settings [d]ifficult or [e]asy ')
if b.lower()=='d':
    a.play(keeps, shoots3, dribbles, defences, player, shoot, dribble, defence, keep, players, opposition2, oppositions, teamname, oppname, goal_or_not, defence_text, goal_text, dribble_text, pass_text)
elif b.lower()=='e':
    a.play(keeps, shoots2, dribbles, defences, player, shoot, dribble, defence, keep, players, opposition, oppositions, teamname, oppname, goal_or_not, defence_text, goal_text, dribble_text, pass_text)
