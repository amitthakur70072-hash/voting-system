vote1=0
vote2=0
vote3=0
while True:
      print("--Voting Menu--")
      print("1.vote for Rahul")
      print("2.vote for Sahil")
      print("3.vote for Anil")
      print("4.show result")  
      print("5.Exit")
      
      choice=input("Enter your choice: ")
      
      if choice=="1":
            vote1 += 1
            print("You voted for Rahul")
      elif choice=="2":
            vote2 += 1
            print("You voted for Sahil")
      elif choice=="3":
            vote3+= 1
            print("You voted for Anil")
      elif choice=="4":
            print("--Results--")
            print("Rahul",vote1)
            print("Sahil",vote2)
            print("Anil",vote3)

            if vote1>vote2 and vote1>vote3:
                  print("Rahul is the Winner")   
            elif vote2>vote1 and vote2>vote3:
                  print("Sahil is the Winner")
            elif vote3>vote1 and vote3>vote2:
                  print("Anil is the Winner")
            else:
                  print("its a tie")                       

      elif choice=="5":
            print("Exit") 
            break
      else:
            print("invalid entry")