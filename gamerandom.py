import random
my_file = open('gamelist.txt', 'r')
text = my_file.read()
my_file.close()
games = text.split('\n')
if games[-1]=='':
    games.pop()

def main():
    seegames()
    addgames()
    randomgame()
    
def seegames():
    seelist = input("Would you like to see your current game list? y/n: ")
    if seelist == "y":
        print(f"current games: {games}") 
    else: 
        print("okay")
        
def addgames(): 
    addlist = input("would you like to add another game to the list? y/n: ")
    if addlist == "y":
        games.append(input("name of game: "))
        write_file = open('gamelist.txt', 'w')
        write_file.write("\n".join(games))
        write_file.close()
        addgames()
    else:
        print("okay")
        
def randomgame():
    gamechoice = random.choice(games)
    print("Today you should play:", gamechoice)
    
if __name__=="__main__":
    main()
