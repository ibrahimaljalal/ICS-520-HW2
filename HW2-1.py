from aima3 import logic 

#We will use proportional logic
logic_kb = logic.PropKB()

'''
S1= Statement 1
S2= Statement 2
S3= Statement 3
B1= Gold in Box1
B2= Gold in Box2
B3= Gold in Box3
'''

#Define the variables
S1,S2,S3,B1,B2,B3=logic.expr('S1,S2,S3,B1,B2,B3')

#This means that only one of the statements is true
logic_kb.tell((S1&~S2&~S3)|(~S1&S2&~S3)|(~S1&~S2&S3))

#This means that only one box has gold
logic_kb.tell(B1|B2|B3)

#The meaning of the statements in propositional logic
logic_kb.tell(S1|'<=>'|B1)
logic_kb.tell(S2|'<=>'|~B2)
logic_kb.tell(S3|'<=>'|~B1)

#Checking what box has gold
print("Does Box 1 have gold? (True=yes and False=No) "+str(logic_kb.ask_if_true(B1)))
print("Does Box 2 have gold? (True=yes and False=No) "+str(logic_kb.ask_if_true(B2)))
print("Does Box 3 have gold? (True=yes and False=No) "+str(logic_kb.ask_if_true(B3)))