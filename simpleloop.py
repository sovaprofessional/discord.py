answerList = []
questionsList = [] 
for every x in range(20):
displayQuestion:
	if(x < 4):
		mode=int(raw_input("T or F?"))
	     	if(mode!="Y" AND mode!="y" AND mode!="N" AND mode!="n"): Print ("Invalid Input")
		else: answerList[x] = mode
    	else:
		mode=int(raw_input("A/B/C/D?"))
	     	if(mode!="A" AND mode!="a" AND mode!="B" AND mode!="b" AND mode!="C" AND mode!="c" AND mode!="D" AND mode!="d"): Print ("Invalid Input")
		else: answerList[x] = mode
