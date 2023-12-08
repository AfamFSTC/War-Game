class MyGame():
    def manual(self, printed):
        return printed
    def play(self, keeps, shoots, dribbles, defences, player, shoot, dribble, defence, keep, players, opposition,oppositions, teamname, oppname, goal_or_not, defence_text, goal_text, dribble_text, pass_text):
        pos=[0,1]
        goal1=0
        goal2=0
        ppos=0
        aa=0
        player_possesion=0
        opposition_possesion=0
        passes=0
        passes2=0
        p=0
        p2=0
        import random,time
        ppos=random.choice(pos)
        Start=time.time()
        while ((time.time()))-Start<=180:
            if ppos==0:
                player_possesion+=1
                b=random.choice(player)
                c=input(b+' [s]hoot, [d]ribble, [p]ass ')
                time.sleep(2)
                if c.lower()=='s':
                    e=[]
                    for i in shoot.keys():
                        e.append(i)
                    print(e)
                    d=input('which kind of shot ')
                    time.sleep(2)
                    if d.lower() not in shoot.keys():
                        print('wrong input')
                        time.sleep(2)
                    else:
                        if (shoot[d.lower()]) < (defence[random.choice(defences)]):
                            print('but',oppositions[1:2],'defends it')
                            time.sleep(2)
                            ppos=1
                        elif (shoot[d.lower()]) > (defence[random.choice(defences)]):
                            print('Your shot passed the defence nice')
                            e=random.choice(keeps)
                            print('keeping style-',e)
                            time.sleep(2)
                            if e.lower() not in keep.keys():
                                print('wrong input')
                                time.sleep(2)
                            else:
                                if (shoot[d.lower()]) < (keep[e.lower()]):
                                    print('but',oppositions[0:1],'saves it')
                                    ppos=1
                                    time.sleep(2)
                                elif (shoot[d.lower()]) > (keep[e.lower()]):
                                    print('Nice Shot')
                                    print(random.choice(goal_text))
                                    goal1+=1
                                    print('scores-',teamname,':',goal1,oppname,':',goal2)
                                    ppos=1
                                    time.sleep(2)
                                else:
                                    if random.choice(goal_or_not)==0:
                                        print('but',oppositions[0:1],'saves it')
                                        ppos=1
                                        time.sleep(2)
                                    else:
                                        print('Nice Shot')
                                        print(random.choice(goal_text))
                                        goal1+=1
                                        print('scores-',teamname,':',goal1,oppname,':',goal2)
                                        time.sleep(2)
                                        ppos=1
                        else:
                            if random.choice(goal_or_not)==0:
                                print('Your shot passed the defence Nice')
                                print('keeping style:',random.choice(keeps))
                                print('but',oppositions[0:1],'saves it')
                                ppos=1
                                time.sleep(2)
                            else:
                                print('Your shot passed the defence Nice')
                                print('keeping style-',random.choice(keeps))
                                print('Nice Shot')
                                print(random.choice(goal_text))
                                goal1+=1
                                print('scores-',teamname,':',goal1,oppname,':',goal2)
                                time.sleep(2)
                                ppos=1
                    aa+=1
                elif c.lower()=='d':
                    h=[]
                    for a in dribble.keys():
                        h.append(a)
                    print(h)
                    g=input('which dribble technique ')
                    time.sleep(2)
                    if g.lower() not in dribble.keys():
                        print('wrong input')
                        time.sleep(2)
                    else:
                        if (dribble[g.lower()]) > (opposition[random.choice(oppositions)]):
                            print(random.choice(dribble_text))
                            time.sleep(2)
                            ppos=0
                        elif (dribble[g.lower()]) > (opposition[random.choice(oppositions)]):
                            print('but he lost the ball')
                            time.sleep(2)
                            ppos=1
                        else:
                            if random.choice(pos)==0:
                                print(random.choice(dribble_text))
                                time.sleep(2)
                                ppos=0
                            else:
                                print('but he lost the ball')
                                time.sleep(2)
                                ppos=1
                    aa+=1
                elif c.lower()=='p':
                    p+=1
                    if players[b] > opposition[random.choice(oppositions)]:
                        print(random.choice(pass_text))
                        time.sleep(2)
                        ppos=0
                        passes+=1
                    elif players[b] < opposition[random.choice(oppositions)]:
                        print('but he missed the pass')
                        ppos=1
                        time.sleep(2)
                    else:
                        if random.choice(pos)==0:
                            print(random.choice(pass_text))
                            ppos=0
                            time.sleep(2)
                            passes+=1
                        else:
                            print('but he missed the pass')
                            ppos=1
                            time.sleep(2)
                aa+=1
            else:
                opposition_possesion+=1
                owner=random.choice(oppositions)
                print(owner,'is with the ball')
                time.sleep(2)
                c=random.choice(['s', 'd', 'p'])
                time.sleep(2)
                if c=='s':
                    d=random.choice(shoots)
                    print('shot:',d)
                    print(defences)
                    e=input('what kind of defence ')
                    time.sleep(2)
                    if e.lower() not in defence.keys():
                        print('wrong input ')
                        time.sleep(2)
                    else:
                        if (shoot[d.lower()]) < (defence[e.lower()]):
                            print(random.choice(defence_text))
                            ppos=0
                            time.sleep(2)
                        elif (shoot[d.lower()]) > (defence[e.lower()]):
                            print('sorry it passed your defence')
                            print(keeps)
                            e=input('what kind of keeping ')
                            time.sleep(2)
                            if e.lower() not in keep.keys():
                                print('wrong input')
                                time.sleep(2)
                            else:
                                if (shoot[d.lower()]) < (keep[e.lower()]):
                                    print('but',player[0:1],'saves it')
                                    ppos=0
                                    time.sleep(2)
                                elif (shoot[d.lower()]) > (keep[e.lower()]):
                                    print('it also passed through your keeper sorry')
                                    print(random.choice(goal_text))
                                    goal2+=1
                                    print('scores-',teamname,':',goal1,oppname,':',goal2)
                                    ppos=0
                                    time.sleep(2)
                                else:
                                    if random.choice(goal_or_not)==1:
                                        print('but',player[0:1],'saves it')
                                        ppos=0
                                        time.sleep(2)
                                    else:
                                        print(random.choice(goal_text))
                                        goal2+=1
                                        print('scores-',teamname,':',goal1,oppname,':',goal2)
                                        time.sleep(2)
                                        ppos=0
                        else:
                            if random.choice(goal_or_not)==1:
                                print(random.choice(defence_text))
                                ppos=0
                                time.sleep(2)
                            else:
                                print('sorry it passed your defence')
                                print(keeps)
                                e=input('what kind of keeping ')
                                time.sleep(2)
                                if e.lower() not in keep.keys():
                                    print('wrong input')
                                    time.sleep(2)
                                else:
                                    if (shoot[d.lower()]) < (keep[e.lower()]):
                                        print('but',player[0:1],'saves it')
                                        ppos=0
                                        time.sleep(2)
                                    elif (shoot[d.lower()]) > (keep[e.lower()]):
                                        print('it also passed through your keeper sorry')
                                        print(random.choice(goal_text))
                                        goal2+=1
                                        print('scores-',teamname,':',goal1,oppname,':',goal2)
                                        ppos=0
                                        time.sleep(2)
                                    else:
                                        if random.choice(goal_or_not)==1:
                                            print('but',player[0:1],'saves it')
                                            ppos=0
                                            time.sleep(2)
                                        else:
                                            print(random.choice(goal_text))
                                            goal2+=1
                                            print('scores-',teamname,':',goal1,oppname,':',goal2)
                                            time.sleep(2)
                                            ppos=0
                    aa+=1
                elif c=='d':
                    g=random.choice(dribbles)
                    print('dribble:',g)
                    if (dribble[g]) > (players[random.choice(player)]):
                        print(random.choice(dribble_text))
                        ppos=1
                        time.sleep(2)
                    elif (dribble[g]) > (players[random.choice(player)]):
                        print('but he lost the ball')
                        ppos=0
                        time.sleep(2)
                    else:
                        if random.choice(pos)==1:
                            print(random.choice(dribble_text))
                            ppos=1
                            time.sleep(2)
                        else:
                            print('but he lost the ball')
                            ppos=0
                            time.sleep(2)
                    aa+=1
                elif c=='p':
                    p2+=1
                    b=random.choice(player)
                    if opposition[owner] > players[b]:
                        print(random.choice(pass_text))
                        ppos=1
                        time.sleep(2)
                        passes2+=1
                    elif opposition[owner] < players[b]:
                        print('but he missed the pass')
                        ppos=0
                        time.sleep(2)
                    else:
                        if random.choice(pos)==0:
                            print(random.choice(pass_text))
                            ppos=1
                            time.sleep(2)
                            passes2+=1
                        else:
                            print('but he missed the pass')
                            ppos=0
                            time.sleep(2)
                    aa+=1
        print('And that\'s the end of the match \nBeautiful match if I say so myself\nAll players played their bits perfectly well\nAnd it was worth the effort')
        print('scores=',teamname,':',goal1,oppname,':',goal2)
        player_pos=round((player_possesion/(player_possesion+opposition_possesion))*100)
        opposition_pos=round((opposition_possesion/(player_possesion+opposition_possesion))*100,2)
        print(teamname+'\'s','possesion:',player_pos,oppname+'s','possesion:',opposition_pos)
        try:
            aps=(passes/p)*100
        except ZeroDivisionError:
            aps=0
        try:
            aps2=(passes2/p2)*100
        except ZeroDivisionError:
            aps2=0
        print(f'Accurate Passes:-{teamname}:{aps}% ; {oppname}:{aps2}%')
        print(f'{teamname}: {passes} accurate passes out of {p} passes ; {oppname}: {passes2} accurate passes out of {p2} passes')
        totm=random.randint(0,1)
        if totm==0:
            motm=random.choice(player)
        else:
            motm=random.choice(oppositions)
        print(f'Man of the match : {motm}')
