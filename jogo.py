from stands import *


#Variáveis
rounds = 0
player = ()
inimigo = Inimigo()
timeStoped = False
Curar = False
Armor = 150
blade = True
Sha = False
mosquito = False
soco = False
timeerased = False
Epitaph = False
linha = False
Sono = False
lovetrain = False
bolhac = False
Azar = False


#Aleatorizar stands
if(dado  <= 5):
    player = Player(Za_Warudo)
    print("Seu stand é", player.stand.nome)
elif(dado <= 12):
    player = Player(Star_Platinum)
    print("Seu stand é", player.stand.nome)
elif(dado <= 25):
    player = Player(Silver_Chariot)
    print("Seu stand é", player.stand.nome)
elif(dado <= 50):
    player = Player(Crazy_Diamond)
    print("Seu stand é", player.stand.nome)
elif(dado <= 75):
    player = Player(The_Hand)
    print("Seu stand é", player.stand.nome)
elif(dado <= 85):
    player = Player(Killer_Queen)
    print("Seu stand é", player.stand.nome)
elif(dado <= 140):
    player = Player(Gold_Experience)
    print("Seu stand é", player.stand.nome)
elif(dado <= 150):
    player = Player(King_Crimson)
    print("Seu stand é", player.stand.nome)
elif(dado <= 160):
    player = Player(Stone_Free)
    print("Seu stand é", player.stand.nome)
elif(dado <= 180):
    player = Player(Whitesnake)
    print("Seu stand é", player.stand.nome)
elif(dado <= 185):
    player = Player(Tusk)
    print("Seu stand é", player.stand.nome)
elif(dado <= 200):
    player = Player(Dirty_Deeds_Done_Dirt_Cheap)
    print("Seu stand é", player.stand.nome)
elif(dado <= 210):
    player = Player(Soft_And_Wet)
    print("Seu stand é", player.stand.nome)
elif(dado > 210):
    player = Player(Wonder_Of_U)
    print("Seu stand é", player.stand.nome)

#Funções
def barragem(dano):
    global player
    global inimigo
    totaldamage = 0
    for i in range(5):
        damage = random.randint(1, dano)
        totaldamage += damage
    inimigo.vida -= totaldamage
    
        
    if(player.stand == Star_Platinum or player.stand == Stone_Free or player.stand == Tusk or player.stand == Soft_And_Wet):
        print("ORA "*5)         
    if(player.stand == Za_Warudo or player.stand == Gold_Experience):
        print("MUDA "*5)
    if(player.stand == Crazy_Diamond):
        print("DORARARARARA")
    if(player.stand == Silver_Chariot):
        print("Toma"*5)    
    
    print("\nVocê causou", totaldamage, "de dano")
    print("O inimigo está com", inimigo.vida, "de vida")
    

def TimeStoped():
    global timeStoped
    global player
    #Parar o tempo
    if(player.stand == Star_Platinum):
        if(timeStoped == False):
            print(player.stand.nome + ":Za Warudo")
            timeStoped = True
        elif(timeStoped == True):
            timeStoped = False
            print("E o tempo volta a correr\n")
    elif(player.stand == Za_Warudo):
        if(timeStoped == False):
            print(player.stand.nome, "Paralise o tempo") 
            timeStoped = True
        elif(timeStoped == True):
            timeStoped = False
            print("E o tempo volta a correr\n")

def starfinger():
    global inimigo
    print("STAR FINGER")
    inimigo.vida -= 50
    print("\nVocê atacou o inimigo com o Star Finger e causou 50 de dano")

def facas():
    global inimigo
    inimigo.vida -= 30
    print("\nVocê atacou o inimigo com facas e causou 30 de dano")

def disparar():
    global inimigo
    global blade
    inimigo.vida -= 100
    blade = False
    print("\nVocê disparou sua espada e vai ficar um round sem poder atacar")

def curar():
    global Curar
    if(Curar == False):
        Curar = True
        print("\nVocê ativou o modo de Cura, Use Cura para sair")

    elif(Curar == True):
        Curar = False
        print("\nVocê saiu do modo de cura")

def erase():
    global player
    global inimigo
    player.stand.dano = 999999
    inimigo.vida -= player.stand.dano 
    print("\nVocê apagou o inimigo")

def bomb():
    global inimigo
    inimigo.vida -= 50
    print("\nVocê explodiu o inimigo e causou 50 de dano")

def sha():
    global Sha
    if(Sha == False):
        Sha = True
        print("\nVocê ativou o Sheer Heart Attack por 2 Rounds")
    elif(Sha == True):
        Sha = False
        print("\nVocê desativou o Sheer Heart Attack")


def btd():
    global player
    global inimigo
    print("KIRĀ KUĪN DAISAN NO BAKUDAN, BYTES ZA DUSTO")
    player.vida = 150
    inimigo.vida -= 150
    print("\nVocê ativou o Bites The Dust e recuperou toda sua vida e deu 150 de dano no inimigo")

def mosq():
    global mosquito
    print("\nVocê se cobre de mosquitos")
    mosquito = True

def soco():
    global soco
    inimigo.vida -= 5
    print("\nVocê atacou o inimigo com o soco acelerador e agora seu proximo ataque dará mais dano")
    soco = True

def securar():
    global player
    player.vida += 50
    if(player.vida > 150):
        player.vida = 150

def timeerase():
    global timeerased
    timeerased = True
    print("\nKING CRIMSON")
    print("Você ativou o Time Erase e entrou na dimensão do tempo apagado agora seu proximo ataque dará mais dano")

def epitaph():
    global Epitaph
    Epitaph = True
    print("\nEPITAPH")
    print("Você ativou o Epitaph e desviará dos próximos ataques do inimigo")

def linhas():
    global linha
    if(linha == False):
        linha = True
        print("\nAgora que você está em separado por linhas você pode atacar o inimigo com o triplo do dano e ele te da menos dano")
    elif(linha == True):
        linha = False
        print("\nVocê se juntou denovo")


def securar2():
    global player
    player.vida += 35
    if(player.vida > 150):
        player.vida = 150
        print("\nVocê curou 35 de vida")

def arma():
    global inimigo
    danototal = 0
    for i in range(5):
        dano = random.randint(1, 15)
        danototal += dano
    inimigo.vida -= danototal
    print("\nWhitesnake atirou no inimigo com uma arma e causou", danototal, "de dano")


def disco():
    global inimigo
    inimigo.dano = random.randint(1, 20)
    print("\nVocê usou o Disco e fez ele esquecer um pouco como atacar, assim, o dano do inimigo diminui permanentemente")

def sono():
    global Sono
    Sono = True
    print("\nVocê fez o inimigo dormir")

def unha():
    global inimigo
    Unha = random.randint(15, 35)
    inimigo.vida -= Unha
    print("\nVocê atirou sua unha no inimigo e causou", Unha, "de dano")

def cha():
    global player
    player.vida += 50
    print("\nVocê tomou chá de ervas e curou 50 de vida")
    if(player.vida > 150):
        player.vida = 150

def beatdown():
    global inimigo
    if(inimigo.vida <= 100):
        print("TUSK ACT 4")
        print("Chumimi~in")
        print("ORA "*20)
        print("Arigato Gyro..")
        time.sleep(3)
        inimigo.vida = 0
        print("\nVocê matou o inimigo com o Super Spin")
    else:
        print("\nVocê não pode usar o beatdown enquanto o inimigo estiver com muita vida")

def paradoxo():
    global inimigo
    if(inimigo.vida <= 100):
        print("D4C")
        print("Você trouxe o Inimigo de outra realidade, Os dois se colidiram e o Inimigo morreu")
        inimigo.vida = 0
    else:
        print("\nVocê não pode usar o paradoxo enquanto o inimigo estiver com muita vida")

def troca():
    global player
    player.vida = 150
    print("\nVocê trocou de Corpo com seu Eu de outra realidade e agora Você está com sua vida cheia")

def Lovetrain():
    global lovetrain
    if(lovetrain == False):
        lovetrain = True
        print("\nD4C LOVE TRAIN")
        print("Você ativou o Love Train e agora está Intangível")
    elif(lovetrain == True):
        lovetrain = False
        print("\nD4C LOVE TRAIN")
        print("Você desativou o Love Train")

def bolhacega():
    global bolhac
    bolhac = True
    print("\nVocê atirou a Bolha Cega no Inimigo e cegou ele")

def bolhaexplosiva():
    global inimigo
    inimigo.vida -= 25
    print("\nVocê atirou uma bolha explosiva no inimigo que explodiu e causou 25 de dano")

def gobeyond():
    global inimigo
    inimigo.vida -= 150
    print("\nVocê atirou uma bolha Go Beyond no inimigo que causou 150 de dano")

def calamidade():
    global player
    global Azar
    Azar = True
    print("\nVocê gerou Calamidade e agora o Inimigo tomara mais dano permanentemente")

def fugir():
    fuga = random.randint(1, 1000)
    if(fuga == 666):
        print("\nVocê conseguio fugir")
        exit()
    else:
        print("\nVocê não conseguio fugir")


#Batalha
print("apareceu um inimigo na sua frente, oque voce vai fazer?\n")
while(inimigo.vida > 0):
    if(player.stand == Silver_Chariot):
        if(Armor > 0):    
            print("Você está com", Armor, "de armadura")
        elif(Armor <= 0):
            Armor = 0
            print("\nVocê perdeu toda a sua armadura e por causa disso você é muito rápido")      
    print("Você está com", player.vida, "de vida")
    escolha = input("Bater   Ações   Fugir\n")
    
    #Bater
    if(escolha.lower() == "bater"):
        #Curar
        if(Curar == True):
            inimigo.vida += player.stand.dano
            if(inimigo.vida > 100):
                inimigo.vida = 100
        
        #Sem Espada
        elif(blade == False):
            print("\nVocê não tem espada para bater")

        #Soco Acelerador
        elif(soco == True):
            soco2 = player.stand.dano * 2
            inimigo.vida -= soco2
            print("\nVocê deu", soco2, "de dano")
            soco = False

        #Tempo Apagado
        elif(timeerased == True):
            soco2 = player.stand.dano * 2
            inimigo.vida -= soco2
            print("\nVocê deu", soco2, "de dano")
            timeerased = False   

        #Linhas do Stone Free
        elif(linha == True):
            Linhas = random.randint(1, 30) * 3
            inimigo.vida -= Linhas
            print("\nVocê deu", Linhas, "de dano")

        #Calamidade
        elif(Azar == True):
            azar = random.randint(25, 50)
            inimigo.vida -= azar
            print("\nVocê deu", azar, "de dano")
        else:
            player.bater(inimigo) 

        
        #inimigo sem vida
        if(inimigo.vida <= 0):
           inimigo.vida = 0
           print("O inimigo morreu")
        else:
           print("O inimigo está com", inimigo.vida, "de vida")
    
    #Ações
    if(escolha.lower() in ["acoes", "açoes", "ações", "acões"]):
        

        #Star Platinum
        if(player.stand == Star_Platinum):
            print("\nBarragem")
            print("Parar o tempo\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in ["parar o tempo", "paratempo", "pararotempo", "parar tempo", "timeStoped", "timestop"]):
                TimeStoped()
            elif(escolha2.lower() in ["starfinger"]):
                starfinger()
            elif(escolha2.lower() in ["barragem"]):
                barragem(6)
        
        #Silver Chariot
        if(player.stand == Silver_Chariot):
            print("\nBarragem")
            print("Disparar espada\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in ["disparar espada", "dispararespada", "espada disparar", "espadadisparar", "disparar"]):
                disparar()
            elif(escolha2.lower() in ["barragem"]):
                barragem(4)
        
        #Za Warudo
        if(player.stand == Za_Warudo):
            print("\nBarragem")
            print("Parar o tempo\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in ["parar o tempo", "paratempo", "pararotempo", "parar tempo", "timeStoped", "timestop"]):
                TimeStoped()
            elif(escolha2.lower() in ["facas"]):
                facas()
            elif(escolha2.lower() in ["barragem"]):
                barragem(6)


        #Crazy Diamond
        if(player.stand == Crazy_Diamond):
            print("\nBarragem")
            print("Curar\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in ["curar", "heal"]):
                curar()
            elif(escolha2.lower() in ["barragem"]):
                barragem(5)

        #The Hand
        if(player.stand == The_Hand):
            print("\nBarragem")
            print("Apagar\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in ["apagar", "erase"]):
                erase()
            elif(escolha2.lower() in ["barragem"]):
                barragem(5)

        #Killer Queen
        if(player.stand == Killer_Queen):
            print("\nBarragem")
            print("Bomba Primária")
            print("Sheer Heart Attack")
            print("Bites The Dust\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in ["bomba", "bomb", "bomba primaria", "bombaprimaria", "bombaprimária", "bomba primária"]):
                bomb()
            elif(escolha2.lower() in ["sha", "sheerheartattack", "sheerheart attack", "sheer heart attack", "sheer heartattack"]):
                sha()
            elif(escolha2.lower() in ["btd", "bites the dust", "bitesthedust", "bitesthe dust", "bites thedust"]):
                btd()
            elif(escolha2.lower() in ["barragem"]):
                barragem(4)

        #Gold Experience
        if(player.stand == Gold_Experience):
            print("\nBarragem")
            print("Mosquitos")
            print("Soco Acelerador")
            print("Se Curar\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["mosquito", "mosquitos", "mosq"]):
                mosq()
            elif(escolha2.lower() in  ["soco", "socoacelerador", "soco acelerador", "aceleradorsoco", "acelerador soco"]):
                soco()
            elif(escolha2.lower() in  ["securar", "curar", "se curar"]):
                securar()
            elif(escolha2.lower() in ["barragem"]):
                barragem(3)
        
        #King Crimson
        if(player.stand == King_Crimson):
            print("\nBarragem")
            print("Apagar Tempo")
            print("Epitaph\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["apagar tempo", "apagartempo", "time erase", "timeerase", "tempoapagar", "tempo apagar", "erasetime", "erase time"]):
                timeerase()
            elif(escolha2.lower() in  ["epitaph", "epit"]):
                epitaph()
            elif(escolha2.lower() in ["barragem"]):
                barragem(5)

        #Stone_Free
        if(player.stand == Stone_Free):
            print("\nBarragem")
            print("Linhas")
            print("Se Curar\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["linhas", "linha"]):
                linhas()
            elif(escolha2.lower() in  ["securar", "curar", "se curar"]):
                securar2()
            elif(escolha2.lower() in ["barragem"]):
                barragem(3)
        
        #Whitesnake
        if(player.stand == Whitesnake):
            print("\nBarragem")
            print("Arma")
            print("Disco")
            print("Névoa Do Sono\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["arma", "gun", "tiros", "tiro", "tiros"]):
                arma()
            elif(escolha2.lower() in  ["disco", "disc"]):
                disco()
            elif(escolha2.lower() in ["sono", "névoa do sono", "nevoa do sono", "nevoadosono", "nevoa", "névoa"]):
                sono()
            elif(escolha2.lower() in ["barragem"]):
                barragem(3)

        #Tusk
        if(player.stand == Tusk):
            print("\nBarragem")
            print("Unhas")
            print("Chá")
            print("Beatdown\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["unhas", "unha", "atirar unha", "atirar unhas", "atirarunha", "atirarunhas", "atirar"]):
                unha()
            elif(escolha2.lower() in ["cha", "chá"]):
                cha()
            elif(escolha2.lower() in ["beatdown", "beat down", "finalização", "finalizacão", "finalizaçao", "finalizacao"]):
                beatdown()
            elif(escolha2.lower() in ["barragem"]):
                barragem(5)

        #Dirty Deeds Done Dirt Cheap
        if(player.stand == Dirty_Deeds_Done_Dirt_Cheap):
            print("\nBarragem")
            print("Paradoxo")
            print("Troca De Corpo")
            print("Love Train\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["paradoxo", "paradox", "Paradoxo", "Paradox"]):
                paradoxo()
            elif(escolha2.lower() in ["troca", "Troca", "troca de corpos", "trocade corpos", "troca decorpos"]):
                troca()
            elif(escolha2.lower() in ["lovetrain", "LoveTrain", "Lovetrain", "loveTrain", "love train", "Love Train", "Love train", "love Train", "lt"]):
                Lovetrain()
            elif(escolha2.lower() in ["barragem"]):
                barragem(4)
        
        #Soft & Wet  
        if(player.stand == Soft_And_Wet):
            print("\nBarragem")
            print("Bolha De Cegagem")
            print("Bolha Explosiva")
            print("Go Beyond\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["bolhac", "bc", "bolha cegagem", "bolha de cegagem", "bolhade cegagem", "bolha decegagem"]):
                bolhacega()
            elif(escolha2.lower() in ["bolhaex", "be", "bolha explosiva", "bolhaexplosiva"]):
                bolhaexplosiva()
            elif(escolha2.lower() in ["gobeyond", "go beyond"]):
                gobeyond()
            elif(escolha2.lower() in ["barragem"]):
                barragem(4)

        #Wonder Of U
        if(player.stand == Wonder_Of_U):
            print("\nBarragem")
            print("Calamidade\n")
            escolha2 = input("Qual ação você irá fazer?\n")
            if(escolha2.lower() in  ["calamidade", "calamity"]):
                calamidade()
            elif(escolha2.lower() in ["barragem"]):
                barragem(2)

    #Fugir
    if(escolha.lower() == "fugir"):
        fugir()
    
    #Inimigo te ataca
    if(inimigo.vida > 0):
        if(timeStoped == True):
            print("\nO inimigo esta paralizado")
        elif(timeStoped == False):
            if(player.stand == Silver_Chariot):
                if(Armor > 0):
                    Armor -= inimigo.dano 
                    print("O inimigo deu", inimigo.dano, "de dano na sua armadura\n")
                elif(Armor <= 0):
                    print("O inimigo não consegue te atacar porque você é muito rápido\n")
            elif(mosquito == True):
                inimigo.vida -= inimigo.dano
                print("O inimigo se deu", inimigo.dano, "de dano\n")
                mosquito = False
            elif(soco == True):
                print("O inimigo não consegue te atacar porque você está com a consciência acelerada\n")
            elif(timeerased == True):
                print("O inimigo não consegue te atacar porque você está na dimensão do tempo apagado\n")
            elif(Epitaph == True):
                print("O inimigo não consegue te atacar porque você desvia de seus ataques\n")
            elif(linha == True):
                inimigodano = random.randint(1, 25)
                player.vida -= inimigodano
                print("O inimigo deu", inimigodano, "de dano\n")
            elif(Sono == True):
                print("O inimigo não consegue te atacar porque ele está dormindo\n") 
            elif(lovetrain == True):
                print("O Inimigo não consegue te atacar porque você está Intangível\n")
            elif(bolhac == True):
                print("O Inimigo não consegue te atacar porque ele está cego\n")
            else:
                inimigo.bater(player)
                print("O inimigo está com", inimigo.vida, "de vida\n")

    if(player.vida <= 0):
        print("\nVocê morreu")
        exit()
    
    #Rounds
    if(timeStoped == True):
        rounds += 1
    if(blade == False): 
        rounds += 1
    if(Epitaph == True):
        rounds += 1
    if(Sono == True):
        rounds += 1
    if(lovetrain == True):
        rounds += 1
    if(bolhac == True):
        rounds += 1
    if(Sha == True):
        rounds += 1
        Shadano = random.randint(1, 25)
        inimigo.vida -= Shadano
        print("Sheer Heart Attack deu", Shadano, "de dano\n")
    if(player.stand == Za_Warudo):
        if(rounds == 3):
            timeStoped = False
            print("E o tempo volta a correr\n")
            rounds = 0
    elif(player.stand == Star_Platinum):
        if(rounds == 2):
            timeStoped = False
            print("E o tempo volta a correr\n")
            rounds = 0 
    if(player.stand == Silver_Chariot):
        if(rounds == 2):
            blade = True
            print("A espada esta pronta\n")
            rounds = 0
    if(player.stand == Killer_Queen):
        if(rounds == 3):
            Sha = False
            print("O Sheer Heart Attack acabou\n")
            rounds = 0
    if(player.stand == King_Crimson):
        if(rounds == 2):
            Epitaph = False
            print("O Epitaph acabou\n")
            rounds = 0
    if(player.stand == Whitesnake):
        if(rounds == 2):
            Sono = False
            print("O inimigo acordou do sono\n")
            rounds = 0
    if(player.stand == Dirty_Deeds_Done_Dirt_Cheap):
        if(rounds == 3):
            lovetrain = False
            print("O Love Train acabou, Agora Você é Tangível\n")
            rounds = 0
    if(player.stand == Soft_And_Wet):
        if(rounds == 3):
            bolhac = False
            print("O Inimigo voltou a enxengar\n")
            rounds = 0

    #Inimigo morre
    if(inimigo.vida <= 0):
       inimigo.vida = 0
       print("O inimigo morreu")
    # else:
    #    print("O inimigo está com", inimigo.vida, "de vida\n")