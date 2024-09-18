print("_"*129)
print("\n\n\t\t\t\t\t\t               WELCOME TO SA ICE GALAXY !!!")
print("\t\t\t\t\t\t1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
print("\t\t\t\t\t\t\t      TIRUNELVELI-627011")
print("")
print("_"*129)

print("\nTO SIGN IN, PLEASE ENTER THE FOLLOWING DETAILS")
name=input("\nPLEASE ENTER YOUR NAME:")
while name.isdigit()==True:
     print("SORRY, YOU'VE ENTERED THE WRONG INPUT")
     print("PLEASE CHECK AGAIN")
     name=input("PLEASE ENTER YOUR NAME:")
     
contact=(input("\nPLEASE ENTER YOUR CONTACT NUMBER:"))
while len(contact)!=10 or contact.isdigit()!=True:
     print("SORRY, YOU'VE ENTERED THE WRONG INPUT")
     print("PLEASE CHECK AGAIN")  
     contact=input("\nPLEASE ENTER YOUR CONTACT NUMBER:")

pd=(input("\nPLEASE ENTER A PASSWORD, IT SHOULD NOT BE LESS THAN 8:"))
while len(pd)<8:
     print("SORRY, YOU'VE ENTERED THE WRONG INPUT")
     print("PLEASE CHECK AGAIN") 
     pd=input("\nPLEASE ENTER A PASSWORD, IT SHOULD NOT BE LESS THAN 8:")
     
import random
x=random.randrange(100,1000)
print("\nYOUR USER ID IS",x)

print("\nTHANKS FOR SIGNING TO SA ICE GALAXY")

print("\nWELCOME",name,", WE HOPE YOU ENJOY YOUR TIME")
print("")
print("_"*129)
          
for i in range(0,500):

     print("\nHERE IS YOUR MENU!!")
     
     print("\n\n\t\t\tITEM \t\t\t\t\tCOST")
     print("\n\t\t1.ICE CREAM (FOR 1 SCOOP)")
     print("\n\t\t\tBASIC FLAVOURS:")
     print("\t\t\t01. VANILLA                          Rs 149")
     print("\t\t\t02. STRAWBERRY                       Rs 149")
     print("\t\t\t03. MANGO                            Rs 149")
     print("\t\t\t04. CHOCOLATE                        Rs 149")
     print("\t\t\t05. PISTA                            Rs 149")
     print("\t\t\t06. BUTTER SCOTCH                    Rs 149")
     print("\t\t\t07. BLACK CURRANT                    Rs 149")
     print("\t\t\t08. BLUE BERRY                       Rs 149")
     print("\t\t\t09. COTTON CANDY                     Rs 149")
     print("\t\t\t10. JACKFRUIT                        Rs 149")

     #SPECIAL FLAVOURS
     print("\n\t\t\tEXOTIC FLAVOURS:")
     print("\t\t\t11. MOCHA                            Rs 179")
     print("\t\t\t12. CHUNKEY MONKEY                   Rs 179")
     print("\t\t\t13. LEMON CUSTARD                    Rs 179")
     print("\t\t\t14. THE TONIGHT DOUGH                Rs 179")
     print("\t\t\t15. PINEAPPLE COCONUT                Rs 179")
     print("\t\t\t16. SALTED CARAMEL                   Rs 179")
     print("\t\t\t17. CHERRY GARCIA                    Rs 179")
     print("\t\t\t18. MATCHA                           Rs 179")
     print("\t\t\t19. ALMOND FUDGE                     Rs 179")
     print("\t\t\t20. QUESO                            Rs 179")

     print("\n\t\t\tTOPPINGS FOR ICE CREAM")
     print("\t\t\t01. CHOCO CHIPS                      Rs 20")
     print("\t\t\t02. CHOCO BUTTONS                    Rs 20")
     print("\t\t\t03. GEMS                             Rs 20")
     print("\t\t\t04. SPRINKLES                        Rs 20")
     print("\t\t\t05. OREOS                            Rs 20")
     print("\t\t\t06. KIT KAT                          Rs 20")
     print("\t\t\t07. TUTTY FRUITY                     Rs 20")
     print("\t\t\t08. NUTS                             Rs 20")
     print("\t\t\t09. CHERRY                           Rs 20")
     print("\t\t\t10. DRY FRUITS                       Rs 20")
     print("\t\t\t11. HOT FUDGE                        Rs 20")
     print("\t\t\t12. CARAMEL SAUCE                    Rs 20")
     print("\t\t\t13. BLUEBERRY SYRUP                  Rs 20")
     print("\t\t\t14. STRAWBERRY SYRUP                 Rs 20")
     print("\t\t\t15. CHOCOLATE SYRUP                  Rs 20")

     print("\n\t\t\tCUP SIZE")
     print("\t\t\t01.SMALL                             Rs 10")
     print("\t\t\t02.MEDIUM                            Rs 20")
     print("\t\t\t03.LARGE                             Rs 30")

     print("\n\t\t2.CAKE (FOR 1 LAYER)")
     print("\t\t\t01. VANILLA                          Rs 450")
     print("\t\t\t02. STRAWBERRY                       Rs 450")
     print("\t\t\t03. CHOCOLATE                        Rs 450")
     print("\t\t\t04. WHITE FOREST                     Rs 450")
     print("\t\t\t05. BLACK FOREST                     Rs 450")
     print("\t\t\t06. RED VELVET                       Rs 450")
     print("\t\t\t07. CHEESE CAKE                      Rs 450")
     print("\t\t\t08. BANANA                           Rs 450")
     print("\t\t\t09. COCONUT                          Rs 450")
     print("\t\t\t10. SPONGE CAKE                      Rs 450")

     print("\n\t\t\tSPECIAL CAKE")
     print("\n\t\t\t11. ICE CREAM CAKE")                             
     print("\t\t\t11.01. VANILLA                       Rs 550")
     print("\t\t\t11.02. STRAWBERRY                    Rs 550")
     print("\t\t\t11.03. CHOCOLATE                     Rs 550")
     print("\t\t\t11.04. MANGO                         Rs 550")
     print("\t\t\t11.05. DARK CHOCOLATE                Rs 550")
     print("\t\t\t11.06. BLACKCURRANT                  Rs 550")
     print("\t\t\t11.07. BUTTERSCOTCH                  Rs 550")
     print("\t\t\t11.08. MINT                          Rs 550")
     print("\t\t\t11.09. JACK FRUIT                    Rs 550")
     print("\t\t\t11.10. BERRY                         Rs 550")

     print("\n\t\t\tOUTER LAYER")
     print("\t\t\t01.FROSTING                          Rs 20")
     print("\t\t\t02.ICING                             Rs 20")
     print("\t\t\t03.CREAM                             Rs 20")
     print("\t\t\t04.BUTTER CREAM                      Rs 20")
     print("\t\t\t05.CREAM CHEESE                      Rs 20")

     print("\n\t\t\tFILLINGS")
     print("\t\t\t1. CLASSIC FRENCH BUTTERCREAM        Rs 30")
     print("\t\t\t2. CHOCOLATE GANACHE                 Rs 30")
     print("\t\t\t3. STRAWBERRY                        Rs 30")
     print("\t\t\t4. COCONUT                           Rs 30")
     print("\t\t\t5. BANANA CREAM                      Rs 30")
     print("\t\t\t6. CHERRY CREAM                      Rs 30")
     print("\t\t\t7. WHIPPED CHOCOLATE                 Rs 30")

     print("\n\t\t3.COOKIE (COST FOR 1 COOKIE)")
     print("\t\t\t01. BUTTER COOKIE                    Rs 10")
     print("\t\t\t02. GIGERBREAD COOKIE                Rs 10")
     print("\t\t\t03. CHOCOLATE CHIP COOKIE            Rs 10")
     print("\t\t\t04. GINGER SNAP COOKIE               Rs 10")
     print("\t\t\t05. MOLASSES COOKIE                  Rs 10")
     print("\t\t\t06. UBE CRINKLES                     Rs 10")  
     print("\t\t\t07. SANDWICH COOKIE                  Rs 10")
     print("\t\t\t08. DROP COOKIE                      Rs 10")
     print("\t\t\t09. SNICKER COOKIE                   Rs 10")
     print("\t\t\t10. WHOOPIE PIES                     Rs 10")

     print("\n\t\t\tTOPPINGS")
     print("\t\t\t01. DRIED CRANBERRIES                Rs 10")
     print("\t\t\t02. SHREDDED COCONUT                 Rs 10")
     print("\t\t\t03. CRYSTALLISED GINGER              Rs 10")
     print("\t\t\t04. SLICED FRUIT                     Rs 10")
     print("\t\t\t05. CHOCOLATE GARNISH                Rs 10")
     print("\t\t\t06. EDIBLE FLOWERS                   Rs 10")
     print("\t\t\t07. NUTS AND SEEDS                   Rs 10")
     print("\t\t\t08. FRIED BREAD                      Rs 10")
     print("\t\t\t09. CRUSHED CANDIES                  Rs 10")
     print("\t\t\t10. RAINBOW SPARKLES                 Rs 10")

     print("\n\t\t4.CHOCOLATE (FOR 1 CHOCOLATE)")
     print("\t\t\t01. PEANUT BUTTER CHOCOLATE          Rs 30")
     print("\t\t\t02. THYME CHOCOLATE                  Rs 30")
     print("\t\t\t03. CHAI CHOOCOLATE                  Rs 30")
     print("\t\t\t04. TAHINI CHOCOLATE                 Rs 30")
     print("\t\t\t05. RUBY CHOCOLATE                   Rs 30")
     print("\t\t\t06. GREEN TEA CHOCOLATE              Rs 30")  
     print("\t\t\t07. WASABI CHOCOLATE                 Rs 30")
     print("\t\t\t08. CHILLI CHOCOLATE                 Rs 30")
     print("\t\t\t09. SEA SALT CHOCOLATE               Rs 30")
     print("\t\t\t10. MILK CHOCOLATE                   Rs 30")

     print("\n\t\t\tTOPPINGS")
     print("\t\t\t01. WHIPPED CREAM                    Rs 10")
     print("\t\t\t02. CRUSHED PEPPERMINT CANDY         Rs 10")
     print("\t\t\t03. POWDERED PEANUT BUTTER           Rs 10")
     print("\t\t\t04. DARK COCO POWDER                 Rs 10")
     print("\t\t\t05. MINI MARSHMELLOWS                Rs 10")
     print("\t\t\t06. CINNAMON STICKS                  Rs 10")
     print("\t\t\t07. MILK CHOCOLATE TRUFFLES          Rs 10")
     print("\t\t\t08. FROZEN YOGURT                    Rs 10")
     print("\t\t\t09. CARAMEL                          Rs 10")
     print("\t\t\t10. COFFEE EXTRACT                   Rs 10")

     des=input("\nCHOOSE YOURS!! : ")

     #ICE CREAM 
     if des=="ICE CREAM" or des=="ice cream" or des=="icecream" or des=="ICECREAM" or des=="Icecream" or des=="Ice cream" or des=="1":
          print("\n\n\nYOU HAVE SELECTED 'ICE CREAM', CHECK WHAT'S ON THE MENU!!")          
          print("\n\n\t\t ITEM")
          
          #BASIC FLAVOURS
          print("\n\n\tBASIC FLAVOURS:")
          print("\n\t01. VANILLA")
          print("\t02. STRAWBERRY")
          print("\t03. MANGO")
          print("\t04. CHOCOLATE")
          print("\t05. PISTA")
          print("\t06. BUTTER SCOTCH")
          print("\t07. BLACK CURRANT")
          print("\t08. BLUE BERRY")
          print("\t09. COTTON CANDY")
          print("\t10. JACKFRUIT")

          #SPECIAL FLAVOURS
          print("\n\n\tEXOTIC FLAVOURS:")
          print("\n\t11. MOCHA")
          print("\t12. CHUNKEY MONKEY")
          print("\t13. LEMON CUSTARD")
          print("\t14. THE TONIGHT DOUGH")
          print("\t15. PINEAPPLE COCONUT")
          print("\t16. SALTED CARAMEL")
          print("\t17. CHERRY GARCIA")
          print("\t18. MATCHA")
          print("\t19. ALMOND FUDGE")
          print("\t20. QUESO")
          
          f=int(input("\nDO YOU WISH TO HAVE A BASIC OR EXOTIC FLAVOUR, ENTER 0 FOR BASIC OR 1 FOR EXOTIC:"))
          if f==0:
               a=int(input("\nYOU'VE CHOSEN THE BASICS, ENTER THE NUMBER OF THE BASIC FLAVOUR YOU WOULD LIKE TO HAVE:"))
               if a==1:
                    print("YOU'VE CHOSEN VANILLA")
               elif a==2:
                    print("YOU'VE CHOSEN STRAWBERRY")
               elif a==3:
                    print("YOU'VE CHOSEN MANGO")
               elif a==4:
                    print("YOU'VE CHOSEN CHOCOLATE")
               elif a==5:
                    print("YOU'VE CHOSEN PISTA")
               elif a==6:
                    print("YOU'VE CHOSEN BUTTERSCOTCH")
               elif a==7:
                    print("YOU'VE CHOSEN BLACK CURRANT")
               elif a==8:
                    print("YOU'VE CHOSE BLUE BERRY")
               elif a==9:
                    print("YOU'VE CHOSEN COTTON CANDY")
               elif a==10:
                    print("YOU'VE CHOSEN JACK FRUIT")
             
               else: 
                    print("IT SEEMS YOU MIGHT ENTERED A NUMBER THAT IS NOT ON THE LIST OF THE BASIC FLAVOURS")
                    e=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                    while e!=0 and e!=1:
                         e=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                    if e==0:
                         print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
                         continue
                    elif e==1:
                         print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                         print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                         break
                    
          elif f==1:
               b=int(input("\nYOU'VE CHOSEN EXOTIC, ENTER THE NUMBER OF THE EXOTIC FLAVOUR YOU WOULD LIKE TO HAVE:"))
               if b==11:
                    print("YOU'VE CHOSEN MOCHA")
               elif b==12:
                    print("YOU'VE CHOSEN CHUNKEY MONKEY")
               elif b==13:
                    print("YOU,VE CHOSEN LEMON CUSTARD")
               elif b==14:
                    print("YOU'VE CHOSEN THE TONIGHT DOUGH")
               elif b==15:
                    print("YOU'VE CHOSEN PINEAPPLE COCONUT")
               elif b==16:
                    print("YOU'VE CHOSEN SALTED CARAMEL")
               elif b==17:
                    print("YOU'VE CHOSEN CHERRY GARCIA")
               elif b==18:
                    print("YOU'VE CHOSEN MATCHA")
               elif b==19:
                    print("YOU'VE CHOSEN ALMOND FUDGE")
               elif b==20:
                    print("YOU'VE CHOSEN QUESO")
               else:
                    print("IT SEEMS YOU MIGHT HAVE ENTERED A NUMBER THAT IS NOT ON THE LIST OF THE EXOTIC FLAVOURS")
                    d=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                    while d!=0 and d!=1:
                         d=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                    if d==0:
                         print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
                         continue
                    elif d==1:
                         print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                         print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                         break
                    
          else:
               print("\nSORRY, IT LOOKS LIKE YOU'VE HAVE GIVEN A WRONG INPUT")
               c=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
               while c!=0 and c!=1:
                    c=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
               if c==0:
                    print("WE WELCOME YOU AGAIN TO SA ICE GALAXY ")
                    continue
               elif c==1:
                    print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                    print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                    break

           #TOPPING    
          topping1=input("\nDO YOU WISH TO HAVE TOPPINGS ON YOUR ICECREAM(YES/NO):")
          for i in range(0,50):
               if topping1=="YES" or topping1=="Yes" or topping1=="yes":
                    print("\nHERE IS THE MENU FOR TOPPING")
                    print("01. CHOCO CHIPS")
                    print("02. CHOCO BUTTONS")
                    print("03. GEMS")
                    print("04. SPRINKLES")
                    print("05. OREOS")
                    print("06. KIT KAT")
                    print("07. TUTTY FRUITY")
                    print("08. NUTS")
                    print("09. CHERRY")
                    print("10. DRY FRUITS")
                    print("11. HOT FUDGE")
                    print("12. CARAMEL SAUCE")
                    print("13. BLUEBERRY SYRUP")
                    print("14. STRAWBERRY SYRUP")
                    print("15. CHOCOLATE SYRUP")
                    
                    top=int(input("\nWHAT TOPPING DO YOU WANT, PLEASE ENTER THE NUMBER:"))
                    if top==1:
                         print("YOU'VE SELECTED CHOCO CHIPS")
                         break
                    elif top==2:
                         print("YOU'VE SELECTED CHOCO BUTTONS")
                         break
                    elif top==3:
                         print("YOU'VE SELECTED GEMS")
                         break
                    elif top==4:
                         print("YOU'VE SELECTED SPRINKLES")
                         break
                    elif top==5:
                         print("YOU'VE SELECTED OREOS")
                         break
                    elif top==6:
                         print("YOU'VE SELECTED KIT KAT")
                         break
                    elif top==7:
                         print("YOU'VE SELECTED TUTTY FRUITY")
                         break
                    elif top==8:
                         print("YOU'VE SELECTED NUTS")
                         break
                    elif top==9:
                         print("YOU'VE SELECTED CHERRY")
                         break
                    elif top==10:
                         print("YOU'VE SELECTED DRY FRUITS")
                         break
                    elif top==11:
                         print("YOU'VE SELECTED HOT FUDGE")
                         break
                    elif top==12:
                         print("YOU'VE SELECTED CARAMEL FUDGE")
                         break
                    elif top==13:
                         print("YOU'VE SELECTED BLUEBERRY SYRUP")
                         break
                    elif top==14:
                         print("YOU'VE SELECTED STRAWBERRY SYRUP")
                         break
                    elif top==15:
                         print("YOU'VE SELECTED CHOCOLATE SYRUP")
                         break
                    else:
                         print("PLEASE ENTER AN AVAILABLE OPTION")
                         
               elif topping1=="NO" or topping1=="No" or topping1=="no":
                    print("NO TOPPINGS ON YOUR ICECREAM AS YOU WISH")
                    break

               else:
                    print("PLEASE ENTER AN AVAILABLE OPTION")
                    topping1=input("\nDO YOU WISH TO HAVE TOPPINGS ON YOUR ICECREAM(YES/NO):")
                    
          #CUP SIZE                
          print("\nTHE AVAILABLE CUP SIZES ARE:")
          print("\n1.SMALL")
          print("2.MEDIUM")
          print("3.LARGE")

          cup=int(input("\nWHAT CUP SIZE DO YOU WANT, PLEASE ENTER THE NUMBER:"))
          for i in range(0,50):
               if cup==1:
                    print("A SMALL CUP FOR YOUR ICE CREAM")
                    break
               elif cup==2:
                    print("A MEDIUM CUP FOR YOUR ICE CREAM")
                    break
               elif cup==3:
                    print("A LARGE CUP FOR YOUR ICE CREAM")
                    break
               else:
                    print("PLEASE ENTER A NUMBER THAT IS WITHIN THE GIVEN MENU")
                    cup=int(input("WHAT CUP SIZE DO YOU WANT, PLEASE ENTER THE NUMBER:"))

          #SCOOPS
          scoops=int(input("\n\nHOW MANY SCOOPS OF ICE CREAM DO YOU WANT:"))

          print("\nYOUR ORDER WILL GET READY SOON, WHILE YOU ARE WAITING, HERE IS YOUR RECIEPT")
     
          print("\n\t\tSA ICE GALAXY")
          print("  1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
          print("\t      TIRUNELVELI-627011")
          print("\t\tPH: 9789000425")
          print("\t     GST: 33AAPFN1783J1ZW")
          billno=random.randrange(1500,10500)
          print('')
          print('             ***INVOICE***')
          print('CUSTOMER NAME: ',name,)
          print('PHONE NUMBER: ',contact)
          print('USER ID: ',x,"            BILL NO:",billno)
          print("USER: SHAREE              COUNTER: BIL2") 
          print('')
          print('-'*50)

          #COST
          if f==0 and (topping1=="YES" or topping1=="Yes" or topping1=="yes"):
               if cup==1:
                   cost=149+20+scoops*10
                   print("\n\tITEM\t\t\t\t COST")
                   print("\nSMALL ICECREAM WITH TOPPINGS\t\tRs ",cost)
               elif cup==2:
                   cost=159+20+scoops*10
                   print("\n\tITEM\t\t\t\t COST")
                   print("\nMEDIUM ICECREAM WITH TOPPINGS\t\tRs  ",cost)
               elif cup==3:
                    cost=169+20+scoops*10
                    print("\n\tITEM\t\t\t\t COST")
                    print("\nLARGE ICECREAM WITH TOPPINGS\t\tRs  ",cost)
          elif f==1 and (topping1=="YES" or topping1=="Yes" or topping1=="yes"):
              if cup==1:
                  cost=179+20+scoops*10
                  print("\n\tITEM\t\t\t COST")
                  print("\nSMALL ICECREAM WITH TOPPINGS\tRs ",cost)
              elif cup==2:
                  cost=189+20+scoops*10
                  print("\n\tITEM\t\t\t COST")
                  print("\nMEDIUM ICECREAM WITH TOPPINGS\tRs ",cost)
              elif cup==3:
                  cost=199+20+scoops*10
                  print("\n\tITEM\t\t\t COST")
                  print("\nLARGE ICECREAM WITH TOPPINGS\tRs ",cost)
          elif f==0 and (topping1=="NO" or topping1=="No" or topping1=="no"):
              if cup==1:
                  cost=149+scoops*10
                  print("\n\tITEM\t\t\t\t  COST")
                  print("\nSMALL ICECREAM WITHOUT TOPPINGS\t\tRs  ",cost)
              elif cup==2:
                  cost=159+20+scoops*10
                  print("\n\tITEM\t\t\t\t COST")
                  print("\nMEDIUM ICECREAM WITHOUT TOPPINGS\tRs ",cost)
              elif cup==3:
                  cost=169+20+scoops*10
                  print("\n\tITEM\t\t\t\t COST")
                  print("\nLARGE ICECREAM WITHOUT TOPPINGS\t\tRs  ",cost)
          elif f==1 and (topping1=="NO" or topping1=="No" or topping1=="no"):
              if cup==1:
                  cost=179+scoops*10
                  print("\n\tITEM\t\t\t  COST")
                  print("\nSMALL ICECREAM WITHOUT TOPPINGS\t  Rs ",  cost)
              elif cup==2:
                  cost=189+scoops*10
                  print("\n\tITEM\t\t\t\t  COST")
                  print("\nMEDIUM ICECREAM WITHOUT TOPPINGS\t  Rs ",cost)
              elif cup==3:
                  cost=199+scoops*10
                  print("\n\tITEM\t\t\t    COST")
                  print("\nLARGE ICECREAM WITHOUT TOPPINGS\t  Rs   ",cost)
          print("-"*50)
          print("")
          cgst=(2.5/100)*cost
          sgst=(2.5/100)*cost
          print("\t\tTOTAL QUANTITY:1")
          print("\t\t    CGST:2%\t",cgst)
          print("\t\t    SGST:2%\t",sgst)
          print("")
          print("-"*50)
          total=cost+cgst+sgst
          print("\t\t  GRAND TOTAL:    Rs",total)
          print("")
          print("-"*50)
          print("       FSSAI LIC NO:12419026000669")
          print("\t         THANKS")

          print("\n\nDO YOU WISH TO CONTINUE OR STOP THE PROCESS")
          print("\nIF YOU WISH TO CONTINUE ENTER 0")
          print("IF YOU WISH TO STOP ENTER 1")
         
          last2=int(input("\nSO, ENTER YOUR CHOICE:"))
          
          if last2==0:
               print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
               
          elif last2==1:
               print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
               print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
               break
                   
     #CAKE
     elif des=="CAKE" or des=="Cake" or des=="cake" or des=="2":
          print("\n\n\nYOU HAVE SELECTED 'CAKES', CHECK WHAT'S ON THE MENU!!")
          
          print("\n\n\t\tITEM\n")

          print("01. VANILLA")
          print("02. STRAWBERRY")
          print("03. CHOCOLATE")
          print("04. WHITE FOREST")
          print("05. BLACK FOREST")
          print("06. RED VELVET")
          print("07. CHEESE CAKE")
          print("08. BANANA")
          print("09. COCONUT")
          print("10. SPONGE CAKE")

          print("\nSPECIAL CAKE")
          print("11. ICE CREAM CAKE")                             
          print("\t11.01. VANILLA")
          print("\t11.02. STRAWBERRY")
          print("\t11.03. CHOCOLATE")
          print("\t11.04. MANGO")
          print("\t11.05. DARK CHOCOLATE")
          print("\t11.06. BLACKCURRANT")
          print("\t11.07. BUTTERSCOTCH")
          print("\t11.08. MINT")
          print("\t11.09. JACK FRUIT")
          print("\t11.10. BERRY")

          ca=int(input("\nWHAT CAKE DO YOU WANT, PLEASE ENTER THE NUMBER:"))
          
          if ca==1:
               print("YOU'VE SELECTED VANILLA CAKE")
          elif ca==2:
               print("YOU'VE SELECTED STRAWBERRY CAKE")
          elif ca==3:
               print("YOU'VE SELECTED CHOCOLATE CAKE")
          elif ca==4:
               print("YOU'VE SELECTED WHITE FOREST CAKE")
          elif ca==5:
               print("YOU'VE SELECTED BLACK FOREST CAKE")
          elif ca==6:
               print("YOU'VE SELECTED RED VELVET CAKE")
          elif ca==7:
               print("YOU'VE SSELECTED CHEESE CAKE")
          elif ca==8:
               print("YOU'VE SELECTED BANANA CAKE")
          elif ca==9:
               print("YOU'VE SELECTED COCONUT CAKE")
          elif ca==10:
               print("YOU'VE SELECTED SPONGE CAKE")

          #SPECIAL CAKE
          elif ca==11:
               print("\nYOU'VE SELECTED ICE CREAM CAKE")
               print("NOW SELECT WHAT FLAVOUR YOU WANT FOR YOUR ICE CREAM CAKE")
               icc=int(input("\nENTER THE NUMBER FOR THE ICE CREAM CAKE FLAVOUR:"))
               if icc==1:
                    print("YOU'VE SELECTED VANILLA ICE CREAM CAKE")
               elif icc==2:
                    print("YOU'VE SELECTED STRAWBERRY ICE CREAM CAKE")
               elif icc==3:
                    print("YOU'VE SELECTED CHOCOLATE ICE CREAM CAKE")
               elif icc==4:
                     print("YOU'VE SELECTED MANGO ICE CREAM CAKE")
               elif icc==5:
                    print("YOU'VE SELECTED DARK CHOCOLATE ICE CREAM CAKE")
               elif icc==6:
                    print("YOU'VE SELECTED BLACKCURRANT ICE CREAM CAKE")
               elif icc==7:
                    print("YOU'VE SELECTED BUTTERSCOTCH ICE CREAM CAKE")
               elif icc==8:
                    print("YOU'VE SELECTED MINT ICE CREAM CAKE")
               elif icc==9:
                    print("YOU'VE SELECTED JACK FRUIT ICE CREAM CAKE")
               elif icc==10:
                    print("YOU'VE SELECTED BERRY ICE CREAM CAKE")
               else:
                    print("PLEASE ENTER A NUMBER THAT IS AVAILABLE")
                    ex=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                    while ex!=0 and ex!=1:
                         ex=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                    if ex==0:
                         print("WE WELCOME YOU AGAIN TO SA ICE GALAXY ")
                         continue
                    elif ex==1:
                         print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                         print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                         break
          else:
                print("IT SEEMS YOU MIGHT ENTERED A NUMBER THAT IS NOT ON THE LIST OF THE BASIC FLAVOURS")
                exi=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                while exi!=0 and exi!=1:
                     exi=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                if exi==0:
                    print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
                    continue
                elif exi==1:
                    print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                    print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                    break
               
          #LAYER
          layer=int(input("\nHOW MANY LAYERS OF CAKE DO YOU WANT:"))
          print("YOUR CAKE HAS",layer,"LAYER/LAYERS")

          #OUTER LAYER
          for i in range(0,50):
               if ca!=10:
                    print("\nFOR YOUR OUTER LAYER WHAT DO YOU PREFER")
                    print("\n\n\tITEM \n")
                    print("1.FROSTING")
                    print("2.ICING")
                    print("3.CREAM")
                    print("4.BUTTER CREAM")
                    print("5.CREAM CHEESE")
                    
                    outlay=int(input("\nWHAT WOULD YOU PREFER, PLEASE ENTER THE NUMBER:"))
                    
                    if outlay==1:
                         print("FROSTING ON YOUR CAKE")
                         col=input("\nPLEASE ENTER WHAT COLOUR YOU WOULD LIKE YOUR FROSTING TO BE:")
                         print("YOUR CAKE'S FROSTING IS IN A",col,"COLOUR")
                         break
                    elif outlay==2:
                         print("ICING ON YOUR CAKE")
                         colo=input("\nPLEASE ENTER WHAT COLOUR YOU WOULD LIKE YOUR ICING TO BE:")
                         print("YOUR CAKE'S ICING IS IN A",colo,"COLOUR")
                         break
                    elif outlay==3:
                         print("CREAM ON YOUR CAKE")
                         colou=input("\nPLEASE ENTER WHAT FLAVOURED CREAM YOU WOULD LIKE:")
                         print("YOUR CAKE'S CREAM HAS A",colou,"FLAVOUR")
                         break
                    elif outlay==4:
                         print("BUTTER CREAM ON YOUR CREAM")
                         colour=input("\nPLEASE ENTER WHAT FLAVOURED BUTTER CREAM YOU WOULD LIKE:")
                         print("YOUR CAKE'S BUTTER CREAM HAS A",colour,"FLAVOUR")
                         break
                    elif outlay==5:
                         print("CREAM CHEESE ON YOUR CAKE")
                         colours=input("\nPLEASE ENTER WHAT FLAVOURED CREAM CHEESE YOU WOULD LIKE:")
                         print("YOUR CAKE'S CREAM CHEESE HAS A",colours,"FLAVOUR")
                         break
                    else:
                         print("\nSORRY YOU HAVE ENTERED A WRONG INPUT")
                         print("\nPLEASE ENTER AN AVAILABLE OPTION")

          #FILLING
          if ca!=10:
               filling=input("\nDO YOU WANT FILLINGS IN YOUR CAKE:")
               for i in range(0,50):
                    if filling=="YES" or filling=="Yes" or filling=="yes":
                         print("\nHERE IS YOUR MENU FOR FILLINGS")
                         print("\n\n\t\tITEM \n")
                         print("1. CLASSIC FRENCH BUTTERCREAM")
                         print("2. CHOCOLATE GANACHE")
                         print("3. STRAWBERRY")
                         print("4. COCONUT")
                         print("5. BANANA CREAM")
                         print("6. CHERRY CREAM")
                         print("7. WHIPPED CHOCOLATE")
                         fill=int(input("\nPLEASE ENTER THE NUMBER OF THE FILLING YOU WOULD LIKE:"))
                         if fill==1:
                              print("YOU'VE SELECTED CLASSIC FRENCH BUTTERCREAM AS YOU FILLING")
                              break
                         elif fill==2:
                              break
                              print("YOU'VE SELECTED CHOCOLATE GANACHE AS YOUR FILLING")
                              break
                         elif fill==3:
                              print("YOU'VE SELECTED STRAWBERRY AS YOUR FILLING")
                              break
                         elif fill==4:
                              print("YOU'VE SELECTED COCONUT AS YOUR FILLING")
                              break
                         elif fill==5:
                              print("YOU'VE SELCTED BANANA CREAM AS YOUR FILLING")
                              break
                         elif fill==6:
                              print("YOU'VE SELECTED CHERRY CREAM AS YOUR FILLING")
                              break
                         elif fill==7:
                              print("YOU'VE SELECTED WHIPPED CHOCOLATE AS YOUR FILLING")
                              break
                         else:
                              print("PLEASE AN AVAILABLE OPTION")
                         
                    elif filling=="NO" or filling=="No" or filling=="no":
                         print("NO FILLINGS IN YOUR CAKE AS YOU WISH")
                         break

                    else:
                         print("PLEASE ENTER AN AVAILABLE OPTION")
                         filling=input("\nDO YOU WISH TO HAVE FILLINGS IN YOUR CAKE(YES/NO):")

          print("\nWE WILL CONTACT YOU WITH THE NUMBER",contact," SO PLEASE COME AND COLLECT YOUR ORDER THEN")

          print("\nHERE IS YOUR RECIEPT")
     
          print("\n\t\tSA ICE GALAXY")
          print("  1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
          print("\t      TIRUNELVELI-627011")
          print("\t\tPH: 9789000425")
          print("\t     GST: 33AAPFN1783J1ZW")
          billno=random.randrange(1500,10500)
          print('')
          print('             ***INVOICE***')
          print('CUSTOMER NAME: ',name,)
          print('PHONE NUMBER: ',contact)
          print('USER ID: ',x,"            BILL NO:",billno)
          print("USER: SHAREE              COUNTER: BIL2") 
          print('')
          print('-'*50)
        
          #COST
          if (ca==1 or ca==2 or ca==3 or ca==4 or ca==5 or ca==6 or ca==7 or ca==8 or ca==9) and (filling=="YES" or filling=="Yes" or filling=="yes"):
               cost=450+30+20+layer*50
               print("\n\tITEM\t\t\t  COST")
               print("-"*50)
               print("\nCAKE WITH FILLINGS\t\tRs ",cost)
               print("")
               print("-"*50)
               
          elif ca==10:
               cost=450+layer*50
               print("\n\tITEM\t\t\t  COST")
               print("-"*50)
               print("\nSPONGE CAKE\t\t\tRs ",cost)
               print("")
               print("-"*50)
          elif (ca==1 or ca==2 or ca==3 or ca==4 or ca==5 or ca==6 or ca==7 or ca==8 or ca==9) and (filling=="NO" or filling=="No" or filling=="no"):
               cost=450+20+layer*50
               print("\n\tITEM\t\t\t  COST")
               print("-"*50)
               print("\nCAKE WITHOUT FILLINGS\t\tRs ",cost)
               print("")
               print("-"*50)
          elif ca==11 and (filling=="YES" or filling=="Yes" or filling=="yes"):
               cost=550+30+20+layer*50
               print("\n\tITEM\t\t\t\t  COST")
               print("-"*50)
               print("\nICE CREAM CAKE WITH FILLINGS\t\tRs ", cost)
               print("-"*50)
          elif ca==11 and (filling=="NO" or filling=="No" or filling=="no"):
               cost=550+20+layer*50
               print("\n\tITEM\t\t\t\t  COST")
               print("-"*50)
               print("\nICE CREAM CAKE WITHOUT FILLINGS\t\tRs ",cost)
               print("-"*50)
          print("")
          cgst=(2.5/100)*cost
          sgst=(2.5/100)*cost
          print("\t\tTOTAL QUANTITY:1")
          print("\t\t    CGST:2.5%\t",cgst)
          print("\t\t    SGST:2.5%\t",sgst)
          print("")
          print("-"*50)
          total=cost+cgst+sgst
          print("\t\t GRAND TOTAL: Rs ",total)
          print("")
          print("-"*50)
          print("       FSSAI LIC NO:12419026000669")
          print("\t         THANKS")        
          
          print("\n\nDO YOU WISH TO CONTINUE OR STOP THE PROCESS")
          print("\nIF YOU WISH TO CONTINUE ENTER 0")
          print("IF YOU WISH TO STOP ENTER 1")
         
          last1=int(input("\nSO, ENTER YOUR CHOICE:"))
          
          if last1==0:
               print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
               
          elif last1==1:
               print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
               print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
               break
          
     elif des=="COOKIE" or des=="Cookie" or des=="cookie" or des=="3":
          print("\n\n\nYOU HAVE SELECTED 'COOKIES', CHECK WHAT'S ON THE MENU!!")
          print("\n\n\t\tITEM \n")
          print("01. BUTTER COOKIE")
          print("02. GIGERBREAD COOKIE")
          print("03. CHOCOLATE CHIP COOKIE")
          print("04. GINGER SNAP COOKIE")
          print("05. MOLASSES COOKIE")
          print("06. UBE CRINKLES")  
          print("07. SANDWICH COOKIE")
          print("08. DROP COOKIE")
          print("09. SNICKER COOKIE")
          print("10. WHOOPIE PIES")

          z=int(input("YOU'VE CHOSEN COOKIE, ENTER THE NUMBER OF THE COOKIE YOU WANT:"))
          if z==1:
               print("YOU'VE SELECTED BUTTER COOKIE")
          elif z==2:
               print("YOU'VE SELECTED GINGERBREAD COOKIE")
          elif z==3:
               print("YOU'VE SELECTED CHOCOLATE CHIP COOKIE")
          elif z==4:
               print("YOU'VE SELECTED GINGER SNAP COOKIE")
          elif z==5:
               print("YOU'VE SELECTED MOLASSES COOKIE")
          elif z==6:
               print("YOU'VE SELECTED UBE CRINKLES")
          elif z==7:
               print("YOU'VE SELECTED SANDWICH COOKIE")
          elif z==8:
               print("YOU'VE SELCTED DROP COOKIE")
          elif z==9:
               print("YOU'VE SELECTED SNICKER COOKIE")
          elif z==10:
               print("YOU'VE SELECTED WHOOPIE PIES")
          else:
               print("IT SEEMS YOU MIGHT ENTERED A NUMBER THAT IS NOT ON THE LIST OF THE BASIC FLAVOURS")
               e=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
               while e!=0 and e!=1:
                    e=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
               if e==0:
                    print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
                    continue
               elif e==1:
                    print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                    print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                    break
          toppi=input("\nDO YOU WISH TO HAVE TOPPINGS ON YOUR COOKIES(YES/NO): ")
          for i in range(50):
               if toppi=="YES" or toppi=="Yes" or toppi=="yes":
                    print("HERE IS THE MENU FOR TOPPINGS")
                    print("\n\t\tITEM\n")
                    print("01. DRIED CRANBERRIES")
                    print("02. SHREDDED COCONUT")
                    print("03. CRYSTALLISED GINGER")
                    print("04. SLICED FRUIT")
                    print("05. CHOCOLATE GARNISH")
                    print("06. EDIBLE FLOWERS")
                    print("07. NUTS AND SEEDS")
                    print("08. FRIED BREAD")
                    print("09. CRUSHED CANDIES")
                    print("10. RAINBOW SPARKLES")

                    y=int(input("\nINPUT THE NUMBER OF THE TOPPING YOU WOULD LIKE:"))
                    if y==1:
                         print("YOU'VE SELECTED DRIED CRANBERRIES")
                         break
                    elif y==2:
                         print("YOU'VE SELECTED SHREDDED COCONUT")
                         break
                    elif y==3:
                         print("YOU'VE SELECTED CRYSTALLISED GINGER")
                         break
                    elif y==4:
                         print("YOU'VE SELECTED SLICED FRUIT")
                         break
                    elif y==5:
                         print("YOU'VE SELECTED CHOCOLATE GARNISH")
                         break
                    elif y==6:
                         print("YOU'VE SELECTED EDIBLE FLOWERS")
                         break
                    elif y==7:
                         print("YOU'VE SELECTED NUTS AND SEEDS")
                         break
                    elif y==8:
                         print("YOU'VE SELECTED FRIED BREAD")
                         break
                    elif y==9:
                         print("YOU'VE SELECTED CRUSHED CANDIES")
                         break
                    elif y==10:
                         print("YOU'VE SELECTED RAINBOW SPARKLES")
                         break
                    else:
                         print("\nSORRY YOU HAVE ENTERED A WRONG INPUT")
                         print("\nPLEASE ENTER AN AVAILABLE OPTION")
               elif toppi=="NO" or toppi=="No" or toppi=="no":
                    print("NO TOPPINGS ON YOUR COOKIE AS YOU WISH")
                    break

               else:
                    print("PLEASE ENTER AN AVAILABLE OPTION")
                    toppi=input("\nDO YOU WISH TO HAVE TOPPINGS ON YOUR COOKIE(YES/NO):")
          quantity=int(input("\nHOW MANY COOKIES DO YOU WANT: "))
          print("YOUR ORDER CONTAINS",quantity,"COOKIES")

          print("\n\t\tSA ICE GALAXY")
          print("  1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
          print("\t      TIRUNELVELI-627011")
          print("\t\tPH: 9789000425")
          print("\t     GST: 33AAPFN1783J1ZW")
          billno=random.randrange(1500,10500)
          print('')
          print('             ***INVOICE***')
          print('CUSTOMER NAME: ',name,)
          print('PHONE NUMBER: ',contact)
          print('USER ID: ',x,"            BILL NO:",billno)
          print("USER: SHAREE              COUNTER: BIL2") 
          print('')
          print('-'*50)

          #COST

          if toppi=="YES" or toppi=="Yes" or toppi=="yes":
               cost=10+10*quantity
               print("\n\tITEM\t\t   QUANTITY\t     COST")
               print("-"*50)
               print("\nCOOKIES WITH TOPPINGS       ",quantity,"\t Rs  ",   cost)
          elif toppi=="NO" or toppi=="No" or toppi=="no":
               cost=10*quantity
               print("\n\tITEM\t\t   QUANTITY\t     COST")
               print("-"*50)
               print("\nCOOKIES WITHOUT TOPPINGS    ",quantity,"\t Rs  ",   cost)
          print("")
          cgst=(2.5/100)*cost
          sgst=(2.5/100)*cost
          print("\t\tTOTAL QUANTITY: ",quantity)
          print("\t\t\t    CGST:2.5%\t",cgst)
          print("\t\t\t    SGST:2.5%\t",sgst)
          print("")
          print("-"*50)
          total=cost+cgst+sgst
          print("\t\t\t  GRAND TOTAL: Rs ",total)
          print("")
          print("-"*50)
          print("       FSSAI LIC NO:12419026000669")
          print("\t         THANKS")        
          
          print("\n\nDO YOU WISH TO CONTINUE OR STOP THE PROCESS")
          print("\nIF YOU WISH TO CONTINUE ENTER 0")
          print("IF YOU WISH TO STOP ENTER 1")
         
          last1=int(input("\nSO, ENTER YOUR CHOICE:"))
          
          if last1==0:
               print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
               
          elif last1==1:
               print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
               print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
               break
               
     elif des=="CHOCOLATE" or des=="Chocolate" or des=="chocolate" or des=="4":
              print("\n\n\nYOU HAVE SELECTED 'CHOCOLATES', CHECK WHAT'S ON THE MENU!!")
              print("\n\n\t\tITEM\n")
              print("01. PEANUT BUTTER CHOCOLATE")
              print("02. THYME CHOCOLATE")
              print("03. CHAI CHOOCOLATE")
              print("04. TAHINI CHOCOLATE")
              print("05. RUBY CHOCOLATE")
              print("06. GREEN TEA CHOCOLATE")  
              print("07. WASABI CHOCOLATE")
              print("08. CHILLI CHOCOLATE")
              print("09. SEA SALT CHOCOLATE")
              print("10. MILK CHOCOLATE")

              m=int(input("\nYOU'VE CHOSEN CHOCOLATE, ENTER THE NUMBER OF THE CHOCOLATE YOU WANT:"))
              
              if m==1:
                   print("YOU'VE SELECTED PEANUT BUTTER CHOCOLATE")
              elif m==2:
                   print("YOU'VE SELECTED THYME CHOCOLATE")
              elif m==3:
                   print("YOU'VE SELECTED CHAI CHOOCOLATE")
              elif m==4:
                   print("YOU'VE SELECTED TAHINI CHOCOLATE")
              elif m==5:
                   print("YOU'VE SELECTED RUBY CHOCOLATE")
              elif m==6:
                   print("YOU'VE SELECTED GREEN TEA CHOCOLATE")
              elif m==7:
                   print("YOU'VE SELECTED WASABI CHOCOLATE")
              elif m==8:
                   print("YOU'VE SELCTED CHILLI CHOCOLATE")
              elif m==9:
                   print("YOU'VE SELECTED SEA SALT CHOCOLATE")
              elif m==10:
                   print("YOU'VE SELECTED MILK CHOCOLATE")
              else:
                   print("IT SEEMS YOU MIGHT ENTERED A NUMBER THAT IS NOT ON THE LIST OF THE BASIC FLAVOURS")
                   e=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                   while e!=0 and e!=1:
                       e=int(input("\nDO YOU WISH TO RESTART OR STOP THE PROCESS OF ORDERING, ENTER 0 FOR RESTARTING OR 1 FOR  STOPPING THE PROCESS:"))
                   if e==0:
                       print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
                       continue
                   elif e==1:
                       print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                       print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                       break
              toppi=input("\nDO YOU WISH TO HAVE TOPPINGS ON YOUR CHOCOLATES(YES/NO): ")
              for i in range(50):
                   if toppi=="YES" or toppi=="Yes" or toppi=="yes":
                        print("HERE IS THE MENU FOR TOPPINGS")
                        print("\n\n\t\tITEM\n")
                        print("01. WHIPPED CREAM")
                        print("02. CRUSHED PEPPERMINT CANDY")
                        print("03. POWDERED PEANUT BUTTER")
                        print("04. DARK COCO POWDER")
                        print("05. MINI MARSHMELLOWS")
                        print("06. CINNAMON STICKS")
                        print("07. MILK CHOCOLATE TRUFFLES")
                        print("08. FROZEN YOGURT")
                        print("09. CARAMEL")
                        print("10. COFFEE EXTRACT")

                        n=int(input("\nINPUT THE NUMBER OF THE TOPPING YOU WOULD LIKE:"))
                        if n==1:
                             print("YOU'VE SELECTED WHIPPED CREAM")
                             break
                        elif n==2:
                             print("YOU'VE SELECTED CRUSHED PEPPERMINT CANDY")
                             break
                        elif n==3:
                             print("YOU'VE SELECTED POWDERED PEANUT BUTTER")
                             break
                        elif n==4:
                             print("YOU'VE SELECTED DARK COCO POWDER")
                             break
                        elif n==5:
                             print("YOU'VE SELECTED MINI MARSHMELLOWS")
                             break
                        elif n==6:
                             print("YOU'VE SELECTED CINNAMON STICKS")
                             break
                        elif n==7:
                             print("YOU'VE SELECTED MILK CHOCOLATE TRUFFLES")
                             break
                        elif n==8:
                             print("YOU'VE SELECTED FROZEN YOGURT")
                             break
                        elif n==9:
                             print("YOU'VE SELECTED CARAMEL")
                             break
                        elif n==10:
                             print("YOU'VE SELECTED COFFEE EXTRACT")
                             break
                        else:
                             print("\nSORRY YOU HAVE ENTERED A WRONG INPUT")
                             print("\nPLEASE ENTER AN AVAILABLE OPTION")
                   elif toppi=="NO" or toppi=="No" or toppi=="no":
                        print("NO TOPPINGS ON YOUR CHOCOLATE AS YOU WISH")
                        break

                   else:
                        print("PLEASE ENTER AN AVAILABLE OPTION")
                        toppi=input("\nDO YOU WISH TO HAVE TOPPINGS ON YOUR CHOCOLATE(YES/NO):")

              quantity=int(input("\nHOW MANY CHOCOLATES DO YOU WANT: "))
              print("YOUR ORDER CONTAINS",quantity,"CHOCOLATES")
              
              print("\n\t\tSA ICE GALAXY")
              print("  1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
              print("\t      TIRUNELVELI-627011")
              print("\t\tPH: 9789000425")
              print("\t     GST: 33AAPFN1783J1ZW")
              billno=random.randrange(1500,10500)
              print('')
              print('             ***INVOICE***')
              print('CUSTOMER NAME: ',name,)
              print('PHONE NUMBER: ',contact)
              print('USER ID: ',x,"            BILL NO:",billno)
              print("USER: SHAREE              COUNTER: BIL2") 
              print('')
              print('-'*50)

              #COST
              if toppi=="YES" or toppi=="Yes" or toppi=="yes":
                   cost=30*quantity+10
                   print("\n\tITEM\t\t    QUANTITY\t     COST")
                   print("-"*50)
                   print("CHOCOLATES WITH TOPPING     ",quantity,"\t Rs  ",cost)
              elif toppi=="NO" or toppi=="No" or toppi=="no":
                   cost=30*quantity
                   print("\n\tITEM\t\t      QUANTITY\t     COST")
                   print("-"*50)
                   print("CHOCOLATES WITHOUT TOPPING    ",quantity,"\t Rs  ",cost)
              print("")
              cgst=(2.5/100)*cost
              sgst=(2.5/100)*cost
              print("\t\tTOTAL QUANTITY: ",quantity)
              print("\t\t    CGST:2.5%\t\t",cgst)
              print("\t\t    SGST:2.5%\t\t",sgst)
              print("")
              print("-"*50)
              total=cost+cgst+sgst
              print("\t\t\t  GRAND TOTAL: Rs ",total)
              print("")
              print("-"*50)
              print("       FSSAI LIC NO:12419026000669")
              print("\t         THANKS")        
               
              print("\n\nDO YOU WISH TO CONTINUE OR STOP THE PROCESS")
              print("\nIF YOU WISH TO CONTINUE ENTER 0")
              print("IF YOU WISH TO STOP ENTER 1")
              
              last1=int(input("\nSO, ENTER YOUR CHOICE:"))
               
              if last1==0:
                   print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
                    
              elif last1==1:
                   print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
                   print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
                   break
         
     #OTHER OPTION
     else:
          print("\nOH NO, IT SEEMS YOU  MIGHT HAVE ENTERED THE WRONG INPUT")
          print("DO YOU WISH TO CONTINUE OR STOP THE PROCESS")
          print("\nIF YOU WISH TO CONTINUE ENTER 0")
          print("IF YOU WISH TO STOP ENTER 1")
         
          last=int(input("\nSO, ENTER YOUR CHOICE:"))
          
          if last==0:
               print("WE WELCOME YOU AGAIN TO SA ICE GALAXY")
               
          elif last==1:
               print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
               print("\n\t\t\t\t\t\t\t\tPLEASE VISIT AGAIN")
               break
             




































































































































































































































             

