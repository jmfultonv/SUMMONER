from random import randint

def DragonPrimeResult ():
	print ("\n")
	print ("You have been Primarily Identified as the Dragon. You are a free and terrible spirit.\n")
	print ("You see everyone as an enemy and are cruel to those different than you.\n")
	print ("You are capable of great things, but soon grow bored and often leave people and places in worse condition than when you found them.")
	print ("Fear is your friend. May others never speak ill of you.")
	print ("\n")
def DjinnPrimeResult ():
	print ("\n")
	print ("You have been Primarily Identified as the Djinn. You are a master of everything except yourself.\n")
	print ("You are cunning, but thoughtless. You have made yourself a slave to world.\n")
	print ("Your mind is filled with power, but your soul is heavy with hate. Even family is your burden to bear.\n")
	print ("Misery is your fate. May you rule over dust and sand forever.")
	print ("\n")
def SpectrePrimeResult ():
	print ("\n")
	print ("You have been Primarily Identified as the Spectre. Your accomplishments are matched only by your self doubt and pride.\n")
	print ("You are creative, but growth comes difficult. Talent is not something that improves.\n")
	print ("You work alone, because competition makes you vulnerable to criticism. Happiness is the assumption of others.\n")
	print ("Deceit is your tool. The world cannot suffer your flaws.\n")
	print ("\n")
def GolemPrimeResult ():
	print ("\n")
	print ("You have been Primarily Identified as the Golem. You are thriving only the here and now.\n")
	print ("You believe that to try is to fail. Conflict is the evil of society brought down upon itself.\n")
	print ("You see nothing wrong with stagnation, in your reality it is change that undoes progress.")
	print ("You are perfect as you are right now. Remember, to try is to fail.\n")
	print ("\n")
def GryphonPrimeResult ():
	print ("\n")
	print ("You have been Primarily Identified as the Gryphon. No one dares disagree with you.\n")
	print ("You consider the world lucky for you to have been born. There are none holier than thou.\n")
	print ("You view yourself a paragon of grace and morality. There are no other fit judges of character.\n")
	print ("Conflict is your weapon. You push everyone to the brink.\n")
	print ("\n")
def DragonSecondaryResult ():
	print ("\n")
	print ("You have been somewhat Identified as the Dragon. You wish for nothing to hold you back.\n")
	print ("People are often obstacles to your ambition.\n")
	print ("You are only happy when surrounded by the new, which means you are rarely happy at all.\n")
	print ("\n")
def DjinnSecondaryResult ():
	print ("\n")
	print ("You have been somewhat Identified as the Djinn. That which you care about weighs you down.")
	print ("You have turned your friends and family into your unwilling jailers.\n")
	print ("You can only be satisfied when everyone is happy except you. Alone in a crowd.\n")
	print ("\n")
def SpectreSecondaryResult ():
	print ("\n")
	print ("You have been somewhat Identified as the Spectre. You only see the past.\n")
	print ("People threaten your security and confidence.\n")
	print ("Your only escape is a closed door, your only relief is an excuse.\n")
	print ("\n")
def GolemSecondaryResult ():
	print ("\n")
	print ("You have been somewhat Identified as the Golem. To you, suffering is karma.\n")
	print ("Your friends create their own mistakes and have to live with their own failures.\n")
	print ("Your sole wish is to grow old exactly where you are.\n")
	print ("\n")
def GryphonSecondaryResult ():
	print ("\n")
	print ("You have been somewhat Identified as the Gryphon. \n")
	print ("You doubt the choices of others and do not trust them to decide for themselves.\n")
	print ("You consider the only path to be one you approve.\n")
	print ("\n")
def main ():
	DragonValue=1200
	DjinnValue=1200
	SpectreValue=1200
	GolemValue=1200
	GryphonValue=1200
	DragonPriority=5
	DjinnPriority=5
	SpectrePriority=5
	GolemPriority=5
	GryphonPriority=5
	Prime = 'Nothing'
	Secondary = 'Nothing'
	AnswerInput = 0
	TrollFlag=False
	Question0Pass=True
	Question1Pass=True
	Question2Pass=True
	Question3Pass=True
	Question4Pass=True
	Question5Pass=True
	Question6Pass=True
	Question7Pass=True
	Question8Pass=True
	Question9Pass=True
	Question10Pass=True
	Question11Pass=True
	Question12Pass=True
	Question13Pass=True
	Question14Pass=True
	Question15Pass=True
	Question16Pass=True
	Question17Pass=True
	Question18Pass=True
	Question19Pass=True
	Question0UsedFlag=False
	Question1UsedFlag=False
	Question2UsedFlag=False
	Question3UsedFlag=False
	Question4UsedFlag=False
	Question5UsedFlag=False
	Question6UsedFlag=False
	Question7UsedFlag=False
	Question8UsedFlag=False
	Question9UsedFlag=False
	Question10UsedFlag=False
	Question11UsedFlag=False
	Question12UsedFlag=False
	Question13UsedFlag=False
	Question14UsedFlag=False
	Question15UsedFlag=False
	Question16UsedFlag=False
	Question17UsedFlag=False
	Question18UsedFlag=False
	Question19UsedFlag=False
	MassCollector=0
	while MassCollector < 20:
		RandomQuestion = (randint(0,19))
		if (RandomQuestion == 0 and Question0UsedFlag==False):
			Question0UsedFlag=True
			MassCollector = MassCollector + 1
			print ("What makes better justification for stealing from a Baby?\n") 
			print ("That quality is wasted on them or that they should know how cruel the world is?\n")
			while Question0Pass == True:
				AnswerInput = input ("WASTE\n" + "KNOWLEDGE\n")
				if (AnswerInput !='WASTE' and AnswerInput != 'KNOWLEDGE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'WASTE'): #Materialistic
					DragonValue = DragonValue + 100
					DjinnValue = DjinnValue + 100
					SpectreValue = SpectreValue - 100
					GolemValue = GolemValue - 100
					Question0Pass = False
				if (AnswerInput == 'KNOWLEDGE'): #Inhumane
					SpectreValue = SpectreValue + 100
					GolemValue = GolemValue + 100
					DragonValue = DragonValue - 100
					DjinnValue = DjinnValue - 100
					Question0Pass = False
		if (RandomQuestion == 1 and Question1UsedFlag==False):
			Question1UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Would you Trust a Charity with your money if they did not offer the ability to anonymously donate?\n")
			while Question1Pass == True:
				AnswerInput = input ("TRUST\n" + "WITHOLD\n")
				if (AnswerInput !='TRUST' and AnswerInput !='WITHOLD'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'WITHOLD'): #Materialistic
					DragonValue = DragonValue + 100
					DjinnValue = DjinnValue + 100
					GolemValue = GolemValue - 100
					GryphonValue = GryphonValue - 100
					Question1Pass = False
				if (AnswerInput == 'TRUST'):	#Self-Righteous
					GolemValue = GolemValue + 100
					GryphonValue = GryphonValue + 100
					DragonValue = DragonValue - 100
					DjinnValue = DjinnValue - 100
					Question1Pass = False
		if (RandomQuestion == 2 and Question2UsedFlag==False):
			Question2UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Is a Collection more valuable to you when it is Pristine or Complete?")
			while Question2Pass == True:
				AnswerInput = input ("COMPLETE\n" + "PRISTINE\n")
				if (AnswerInput !='COMPLETE' and AnswerInput !='PRISTINE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'PRISTINE'):		#Materialistic
					DragonValue = DragonValue + 100
					DjinnValue = DjinnValue + 100
					SpectreValue = SpectreValue - 100
					GryphonValue = GryphonValue - 100
					Question2Pass = False
				if (AnswerInput == 'COMPLETE'):		#Impulsive
					SpectreValue = SpectreValue + 100
					GryphonValue = GryphonValue + 100
					DragonValue = DragonValue - 100
					DjinnValue = DjinnValue - 100
					Question2Pass = False
		if (RandomQuestion == 3 and Question3UsedFlag==False):
			Question3UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Your Lover is angry and is not listening to you.\n") 
			print ("Should you Raise your voice or Leave the house?\n")
			while Question3Pass == True:
				AnswerInput = input ("RAISE\n" + "LEAVE\n")
				if (AnswerInput !='RAISE' and AnswerInput !='LEAVE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'RAISE'):			#Controlling
					DragonValue = DragonValue + 100
					SpectreValue = SpectreValue + 100
					DjinnValue = DjinnValue - 100
					GolemValue = GolemValue - 100
					Question3Pass = False
				if (AnswerInput == 'LEAVE'):			#Stubborn
					DjinnValue = DjinnValue + 100
					GolemValue = GolemValue + 100
					DragonValue = DragonValue - 100
					SpectreValue = SpectreValue - 100
					Question3Pass = False
		if (RandomQuestion == 4 and Question4UsedFlag==False):
			Question4UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Is it better to rule through Fear or Indoctrination?")
			while Question4Pass == True:
				AnswerInput = input ("INDOCTRINATION\n" + "FEAR\n")
				if (AnswerInput !='INDOCTRINATION' and AnswerInput !='FEAR'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'INDOCTRINATION'):		#Controlling
					DragonValue = DragonValue + 100
					SpectreValue = SpectreValue + 100
					DjinnValue = DjinnValue - 100
					GryphonValue = GryphonValue - 100
					Question4Pass = False
				if (AnswerInput == 'FEAR'):					#Vengeful
					DjinnValue = DjinnValue + 100
					GryphonValue = GryphonValue + 100
					DragonValue = DragonValue - 100
					SpectreValue = SpectreValue - 100
					Question4Pass = False
		if (RandomQuestion == 5 and Question5UsedFlag==False):
			Question5UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Having just saved an Academic Institution from foreclosure, you are left with two options.\n")
			print ("You may have the campus Renamed after you or be placed in control of its Board.\n")
			while Question5Pass == True:
				AnswerInput = input ("RENAME\n" + "BOARD\n")
				if (AnswerInput !='RENAME' and AnswerInput !='BOARD'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'BOARD'):				#Controlling
					DragonValue = DragonValue + 100
					SpectreValue = SpectreValue + 100
					GolemValue = GolemValue - 100
					GryphonValue = GryphonValue - 100
					Question5Pass = False
				if (AnswerInput == 'RENAME'):				#Self-Righteous
					GolemValue = GolemValue + 100
					GryphonValue = GryphonValue + 100
					DragonValue = DragonValue - 100
					SpectreValue = SpectreValue - 100
					Question5Pass = False
		if (RandomQuestion == 6 and Question6UsedFlag==False):
			Question6UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Your Children are fighting again.\n")
			print ("The smarter child is bullying the dumb one.\n")
			print ("Would you Allow this to continue or Convince the dumb child to hurt the smarter one?\n")
			while Question6Pass == True:
				AnswerInput = input ("ALLOW\n" + "CONVINCE\n")
				if (AnswerInput !='ALLOW' and AnswerInput !='CONVINCE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'ALLOW'):			#Unempathetic
					DragonValue = DragonValue + 100
					GolemValue = GolemValue + 100
					DjinnValue = DjinnValue - 100
					SpectreValue = SpectreValue - 100
					Question6Pass = False
				if (AnswerInput == 'CONVINCE'):			#Petty
					DjinnValue = DjinnValue + 100
					SpectreValue = SpectreValue + 100
					DragonValue = DragonValue - 100
					GolemValue = GolemValue - 100
					Question6Pass = False
		if (RandomQuestion == 7 and Question7UsedFlag==False):
			Question7UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Who should Rule?\n")
			print ("Those who were Born to...\n")
			print ("Or those who Want it the most?\n")
			while Question7Pass == True:
				AnswerInput = input ("BORN\n" + "WANT\n")
				if (AnswerInput !='BORN' and AnswerInput !='WANT'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'BORN'):		#Unempathetic
					DragonValue = DragonValue + 100
					GolemValue = GolemValue + 100
					SpectreValue = SpectreValue - 100
					GryphonValue = GryphonValue - 100
					Question7Pass = False
				if (AnswerInput == 'WANT'):		#Impulsive
					SpectreValue = SpectreValue + 100
					GryphonValue = GryphonValue + 100
					DragonValue = DragonValue - 100
					GolemValue = GolemValue - 100
					Question7Pass = False
		if (RandomQuestion == 8 and Question8UsedFlag==False):
			Question8UsedFlag=True
			MassCollector = MassCollector + 1
			print ("A Vagrant has been caught squatting on your land.\n")
			print ("The judge defers to you for sentencing.\n")
			print ("Do you prefer harsh Labor or a heavy Fine?")
			while Question8Pass == True:
				AnswerInput = input ("LABOR\n" + "FINE\n")
				if (AnswerInput !='LABOR' and AnswerInput !='FINE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'FINE'):			#Unempathetic
					DragonValue = DragonValue + 100
					GolemValue = GolemValue + 100
					DjinnValue = DjinnValue - 100
					GryphonValue = GryphonValue - 100
					Question8Pass = False
				if (AnswerInput == 'LABOR'):			#Vengeful
					DjinnValue = DjinnValue + 100
					GryphonValue = GryphonValue + 100
					DragonValue = DragonValue - 100
					GolemValue = GolemValue - 100
					Question8Pass = False
		if (RandomQuestion == 9 and Question9UsedFlag==False):
			Question9UsedFlag=True
			MassCollector = MassCollector + 1
			print ("You have Conspired to overthrow the current dictator\n")
			print ("Do you plan to have him Beheaded or Tortured and put on display?\n")
			while Question9Pass == True:
				AnswerInput = input ("TORTURE\n" + "BEHEAD\n")
				if (AnswerInput !='BEHEAD' and AnswerInput !='TORTURE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'BEHEAD'):			#REBELLIOUS
					DragonValue = DragonValue + 100
					GryphonValue = GryphonValue + 100
					DjinnValue = DjinnValue - 100
					SpectreValue = SpectreValue - 100
					Question9Pass = False
				if (AnswerInput == 'TORTURE'):			#PETTY
					DjinnValue = DjinnValue + 100
					SpectreValue = SpectreValue + 100
					DragonValue = DragonValue - 100
					GryphonValue = GryphonValue - 100
					Question9Pass = False
		if (RandomQuestion == 10 and Question10UsedFlag==False):
			Question10UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Cruelty should be allowed when...\n")
			print ("...it is used against Criminals.\n")
			print ("...the alternative is to Suffer.\n")
			while Question10Pass == True:
				AnswerInput = input ("CRIMINALS\n" + "SUFFER\n")
				if (AnswerInput !='SUFFER' and AnswerInput !='CRIMINALS'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'SUFFER'):			#REBELLIOUS
					DragonValue = DragonValue + 100
					GryphonValue = GryphonValue + 100
					SpectreValue = SpectreValue - 100
					GolemValue = GolemValue - 100
					Question10Pass = False
				if (AnswerInput == 'CRIMINALS'):			#INHUMANE
					SpectreValue = SpectreValue + 100
					GolemValue = GolemValue + 100
					DragonValue = DragonValue - 100
					GryphonValue = GryphonValue - 100
					Question10Pass = False
		if (RandomQuestion == 11 and Question11UsedFlag==False):
			Question11UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Should Zealotry be expected out of a Leader or the People?")
			while Question11Pass == True:
				AnswerInput = input ("LEADER\n" + "PEOPLE\n")
				if (AnswerInput !='PEOPLE' and AnswerInput !='LEADER'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'PEOPLE'):			#REBELLIOUS
					DragonValue = DragonValue + 100
					GryphonValue = GryphonValue + 100
					DjinnValue = DjinnValue - 100
					GolemValue = GolemValue - 100
					Question11Pass = False
				if (AnswerInput == 'LEADER'):			#STUBBORN
					DjinnValue = DjinnValue + 100
					GolemValue = GolemValue + 100
					DragonValue = DragonValue - 100
					GryphonValue = GryphonValue - 100
					Question11Pass = False
		if (RandomQuestion == 12 and Question12UsedFlag==False):
			Question12UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Is Power of men found through Greatness or Purity?\n")
			while Question12Pass == True:
				AnswerInput = input ("GREATNESS\n" + "PURITY\n")
				if (AnswerInput !='GREATNESS' and AnswerInput !='PURITY'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'GREATNESS'):			#Petty
					DjinnValue = DjinnValue + 100
					SpectreValue = SpectreValue + 100
					GolemValue = GolemValue - 100
					GryphonValue = GryphonValue - 100
					Question12Pass = False
				if (AnswerInput == 'PURITY'):			#Self-Righteous
					GolemValue = GolemValue + 100
					GryphonValue = GryphonValue + 100
					DjinnValue = DjinnValue - 100
					SpectreValue = SpectreValue - 100
					Question12Pass = False
		if (RandomQuestion == 13 and Question13UsedFlag==False):
			Question13UsedFlag=True
			MassCollector = MassCollector + 1
			print ("You create better Results when...\n")
			print ("... no one is able to Hide anything from you.\n")
			print ("... there is no one around to Question you.\n")	
			while Question13Pass == True:
				AnswerInput = input ("HIDE\n" + "QUESTION\n")
				if (AnswerInput !='QUESTION' and AnswerInput !='HIDE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'QUESTION'):			#Stubborn
					DjinnValue = DjinnValue + 100
					GolemValue = GolemValue + 100
					SpectreValue = SpectreValue - 100
					GryphonValue = GryphonValue - 100
					Question13Pass = False
				if (AnswerInput == 'HIDE'):				#Impulsive
					SpectreValue = SpectreValue + 100
					GryphonValue = GryphonValue + 100
					DjinnValue = DjinnValue - 100
					GolemValue = GolemValue - 100
					Question13Pass = False
		if (RandomQuestion == 14 and Question14UsedFlag==False):
			Question14UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Is it Better to defeat Many or destroy One")
			while Question14Pass == True:
				AnswerInput = input ("MANY\n" + "ONE\n")
				if (AnswerInput !='MANY' and AnswerInput !='ONE'):
					print ("Please provide a proper answer.\n")
				if (AnswerInput == 'MANY'):			#VENGEFUL
					DjinnValue = DjinnValue + 100
					GryphonValue = GryphonValue + 100
					SpectreValue = SpectreValue - 100
					GolemValue = GolemValue - 100
					Question14Pass = False
				if (AnswerInput == 'ONE'):			#INHUMANE
					SpectreValue = SpectreValue + 100
					GolemValue = GolemValue + 100
					DjinnValue = DjinnValue - 100
					GryphonValue = GryphonValue - 100
					Question14Pass = False
		if (RandomQuestion == 15 and Question15UsedFlag==False):
			Question15UsedFlag=True
			MassCollector = MassCollector + 1
			print ("What holds you back?")
			while Question15Pass == True:
				AnswerInput = input ("TIME\n" + "MONEY\n" + "PEOPLE\n" + "MYSELF\n" + "GOD\n")
				if (AnswerInput == 'GOD'):  #DRAGON
					DragonPriority=1
					Question15Pass = False
				elif (AnswerInput == 'PEOPLE'):  #Djinn
					DjinnPriority=1
					Question15Pass = False
				elif (AnswerInput == 'TIME'): #Spectre
					SpectrePriority=1
					Question15Pass = False
				elif (AnswerInput == 'MONEY'):   #Golem
					GolemPriority = 1
					Question15Pass = False
				elif (AnswerInput == 'MYSELF'):  #Gryphon
					GryphonPriority = 1
					Question15Pass = False
				else:
					print ("Please provide a proper answer")
		if (RandomQuestion == 16 and Question15UsedFlag==True and Question16UsedFlag==False):
			Question16UsedFlag=True
			MassCollector = MassCollector + 1
			print ("What Inspires you?\n")
			while Question16Pass == True:
				if (DragonPriority == 5):
					print ("NOTHING\n")			#DRAGON
				if (DjinnPriority == 5):
					print ("POWER\n")			#DJINN
				if (SpectrePriority == 5):
					print ("TOMORROW\n")			#SPECTRE
				if (GolemPriority == 5):
					print ("NATURE\n")			#GOLEM
				if (GryphonPriority == 5):
					print ("LOVE\n")			#GRYPHON
				AnswerInput = input ()
				if (AnswerInput =='NOTHING' and DragonPriority == 5):
					DragonPriority = 2
					Question16Pass = False
				elif (AnswerInput =='POWER' and DjinnPriority == 5):
					DjinnPriority = 2
					Question16Pass = False
				elif (AnswerInput =='TOMORROW' and SpectrePriority == 5):
					SpectrePriority = 2
					Question16Pass = False
				elif (AnswerInput =='NATURE' and GolemPriority == 5):
					GolemPriority = 2
					Question16Pass = False
				elif (AnswerInput =='LOVE' and GryphonPriority == 5):
					GryphonPriority = 2
					Question16Pass = False
				else:
					print ("Please provide a proper answer.")
		if (RandomQuestion == 17 and Question16UsedFlag==True and Question17UsedFlag==False):
			Question17UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Where are you going?\n")
			while Question17Pass == True:
				if (DragonPriority == 5):
					print ("UP\n")			#DRAGON
				if (DjinnPriority == 5):
					print ("HOME\n")			#DJINN
				if (SpectrePriority == 5):
					print ("NOWHERE\n")			#SPECTRE
				if (GolemPriority == 5):
					print ("SOMEWHERE\n")			#GOLEM
				if (GryphonPriority == 5):
					print ("ANYWHERE\n")			#GRYPHON
				AnswerInput = input ()
				if (AnswerInput =='UP' and DragonPriority == 5):
					DragonPriority = 3
					Question17Pass = False
				elif (AnswerInput =='HOME' and DjinnPriority == 5):
					DjinnPriority = 3
					Question17Pass = False
				elif (AnswerInput =='NOWHERE' and SpectrePriority == 5):
					SpectrePriority = 3
					Question17Pass = False
				elif (AnswerInput =='SOMEWHERE' and GolemPriority == 5):
					GolemPriority = 3
					Question17Pass = False
				elif (AnswerInput =='ANYWHERE' and GryphonPriority == 5):
					GryphonPriority = 3
					Question17Pass = False
				else:
					print ("Please provide a proper answer.")
		if (RandomQuestion == 18 and Question17UsedFlag==True and Question18UsedFlag==False):
			Question18UsedFlag=True
			MassCollector = MassCollector + 1
			print ("On a Scale of 1 to 5, how much to you trust this test?")
			while Question18Pass == True:
				if (DragonPriority == 5):
					print ("1\n")			#DRAGON
				if (DjinnPriority == 5):
					print ("4\n")			#DJINN
				if (SpectrePriority == 5):
					print ("3\n")			#SPECTRE
				if (GolemPriority == 5):
					print ("5\n")			#GOLEM
				if (GryphonPriority == 5):
					print ("2\n")			#GRYPHON
				AnswerInput = input ()
				if (AnswerInput =='1' and DragonPriority == 5):
					DragonPriority = 4
					Question18Pass = False
				elif (AnswerInput =='4' and DjinnPriority == 5):
					DjinnPriority = 4
					Question18Pass = False
				elif (AnswerInput =='3' and SpectrePriority == 5):
					SpectrePriority = 4
					Question18Pass = False
				elif (AnswerInput =='5' and GolemPriority == 5):
					GolemPriority = 4
					Question18Pass = False
				elif (AnswerInput =='2' and GryphonPriority == 5):
					GryphonPriority = 4
					Question18Pass = False
				else:
					print ("Please provide a proper answer.")
		if (RandomQuestion == 19 and Question19UsedFlag==False):
			Question19UsedFlag=True
			MassCollector = MassCollector + 1
			print ("Which of the following should be Legal?\n")   # CONTROL QUESTION
			while Question19Pass == True:
				AnswerInput = input("MURDER\n" + "THEFT\n" + "LYING\n" + "TORTURE\n")
				if (AnswerInput =='LYING'):
					Question19Pass = False
				elif (AnswerInput =='MURDER' or AnswerInput == 'THEFT' or AnswerInput == 'TORTURE'):
					TrollFlag = True
					Question19Pass = False
				else:
					print ("Please provide a proper answer.")
	DragonValue = DragonValue + DragonPriority
	DjinnValue = DjinnValue + DjinnPriority
	SpectreValue = SpectreValue + SpectrePriority
	GolemValue = GolemValue + GolemPriority
	GryphonValue = GryphonValue + GryphonPriority
	if TrollFlag == True:
		print ("The aether has washed your fate away with the current. There are no answers for you here.\n")
	else:
		if ((DragonValue > DjinnValue) and (DragonValue > SpectreValue) and (DragonValue > GolemValue) and (DragonValue > GryphonValue)):
			Prime = 'Dragon'
			DragonPrimeResult()
			if ((DjinnValue > SpectreValue) and (DjinnValue > GolemValue) and (DjinnValue > GryphonValue)):
				Secondary = 'Djinn'
				DjinnSecondaryResult ()
			elif ((SpectreValue > DjinnValue) and (SpectreValue > GolemValue) and (SpectreValue > GryphonValue)):
				Secondary = 'Spectre'
				SpectreSecondaryResult ()
			elif ((GolemValue > DjinnValue) and (GolemValue > SpectreValue) and (GolemValue > GryphonValue)):
				Secondary = 'Golem'
				GolemSecondaryResult ()
			else:
				Secondary = 'Gryphon'
				GryphonSecondaryResult ()
		elif ((DjinnValue > DragonValue) and (DjinnValue > SpectreValue) and (DjinnValue > GolemValue) and (DjinnValue > GryphonValue)):
			Prime = 'Djinn'
			DjinnPrimeResult ()
			if ((DragonValue > SpectreValue) and (DragonValue > GolemValue) and (DragonValue > GryphonValue)):
				Secondary = 'Dragon'
				DragonSecondaryResult ()
			elif ((SpectreValue > DragonValue) and (SpectreValue > GolemValue) and (SpectreValue > GryphonValue)):
				Secondary = 'Spectre'
				SpectreSecondaryResult ()
			elif ((GolemValue > DragonValue) and (GolemValue > SpectreValue) and (GolemValue > GryphonValue)):
				Secondary = 'Golem'
				GolemSecondaryResult ()
			else:
				Secondary = 'Gryphon'
				GryphonSecondaryResult ()
		elif ((SpectreValue > DragonValue) and (SpectreValue > DjinnValue) and (SpectreValue > GolemValue) and (SpectreValue > GryphonValue)):
			Prime = 'Spectre'
			SpectrePrimeResult ()
			if ((DragonValue > DjinnValue) and (DragonValue > GolemValue) and (DragonValue > GryphonValue)):
				Secondary = 'Dragon'
				DragonSecondaryResult ()
			elif ((DjinnValue > DragonValue) and (DjinnValue > GolemValue) and (DjinnValue > GryphonValue)):
				Secondary = 'Djinn'
				DjinnSecondaryResult ()
			elif ((GolemValue > DragonValue) and (GolemValue > DjinnValue) and (GolemValue > GryphonValue)):
				Secondary = 'Golem'
				GolemSecondaryResult ()
			else:
				Secondary = 'Gryphon'
				GryphonSecondaryResult ()
		elif ((GolemValue > DragonValue) and (GolemValue > DjinnValue) and (GolemValue > SpectreValue) and (GolemValue > GryphonValue)):
			Prime = 'Golem'
			GolemPrimeResult ()
			if ((DragonValue > DjinnValue) and (DragonValue > SpectreValue) and (DragonValue > GryphonValue)):
				Secondary = 'Dragon'
				DragonSecondaryResult ()
			elif ((DjinnValue > DragonValue) and (DjinnValue > SpectreValue) and (DjinnValue > GryphonValue)):
				Secondary = 'Djinn'
				DjinnSecondaryResult ()
			elif ((SpectreValue > DragonValue) and (SpectreValue > DjinnValue) and (SpectreValue > GryphonValue)):
				Secondary = 'Spectre'
				SpectreSecondaryResult ()
			else:
				Secondary = 'Gryphon'
				GryphonSecondaryResult ()
		else:
			Prime = 'Gryphon'
			GryphonPrimeResult ()
			if ((DragonValue > DjinnValue) and (DragonValue > SpectreValue) and (DragonValue > GolemValue)):
				Secondary = 'Dragon'
				DragonSecondaryResult ()
			elif ((DjinnValue > DragonValue) and (DjinnValue > SpectreValue) and (DjinnValue > GolemValue)):
				Secondary = 'Djinn'
				DjinnSecondaryResult ()
			elif ((SpectreValue > DragonValue) and (SpectreValue > DjinnValue) and (SpectreValue > GolemValue)):
				Secondary = 'Spectre'
				SpectreSecondaryResult ()
			else:
				Secondary = 'Golem'
				GolemSecondaryResult ()
		if ((Prime == 'Djinn') and (Secondary == 'Dragon')):
			print ("Additionally, I see a magical fate in your future.\n")
		elif ((Prime == 'Dragon') and (Secondary == 'Spectre')):
			print ("Additionally, I see a great victory in your future.\n")
		elif ((Prime == 'Spectre') and (Secondary == 'Gryphon')):
			print ("Additionally, I see a future where you gain great power.\n")
		elif ((Prime == 'Gryphon') and (Secondary == 'Golem')):
			print ("Additionally, I see a future free of worry and fear for you.\n")
		elif ((Prime == 'Golem') and (Secondary == 'Djinn')):
			print ("Additionally, I see your fate, great responsibility awaits.\n")
		elif (DragonValue >= 2200):
			print ("Further, the soul of the Dragon truly dwells around you. Your spirit is that of an invincible warrior.\n")
		elif (DjinnValue >= 2200):
			print ("Further, the soul of the Djinn truly dwells around you. Your spirit is that of an inspiring leader.\n")
		elif (SpectreValue >= 2200):
			print ("Further, the soul of the Wraith truly dwells around you. Your spirit is that of a brilliant creator.\n")
		elif (GolemValue >= 2200):
			print ("Further, the soul of the Mountain truly dwells around you. Your spirit is blessed with driven foresight.\n")
		elif (GryphonValue >= 2200):
			print ("Further, the soul of the Gryphon truly dwells around you. Your spirit is that of a hungering explorer.\n")
		
Quit = 0
QuitCall = 'N0'
print ("Welcome to Ask The Summoner\n")
print ("This program is a quiz.\n")
print ("You will be asked a series of questions.\n")
print ("At the end of the test, you will be told what sort of beast your sins most resemble\n")
while (Quit==0):
	QuitLoop = 0
	main ()
	while (QuitLoop == 0):
		QuitCall = input ("Would you like to take the test again?\n"+"YES\n"+"NO\n")
		if QuitCall == 'YES':
			QuitLoop=1
		elif QuitCall == 'NO':
			QuitLoop=1
			Quit=1
		else:
			"Please provide a proper answer.\n"






