par = int
score = int
hola = 1
while hola <= 18:
    par_str = "Par of hole " + str(hola) + ": "
    score_str = "Score on hole " + str(hola) + ": "
    par = int(input(par_str))
    score = int(input(score_str))
    if (score - par)>3:
        print("bad hole")
    elif (score - par)==3:
        print("triple bogey")
    elif (score - par)==2:
        print("double bogey")
    elif (score - par)==1:
        print("bogey")
    elif (score - par)==0:
        print("par")
    elif (score - par)==-1:
        print("birdie")
    elif (score - par)==-2:
        print("eagle")
    elif (score - par)== -3:
        print("albatross")
    elif (score - par)<-3:
        print("invalid score")
    hola += 1
