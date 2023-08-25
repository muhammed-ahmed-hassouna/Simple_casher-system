import time

import sys

import os

dict = {"meet":15,"milk":5,"fish":10,"pasta":3,"rice":8,"corn":5,"flour":10,"sauce":2,"cheese":5,"beef":14}

Color_blue = ("\033[0;34m")

Color_red = ("\033[0;31m")

Color_black = ("\033[0;30m")

Color_white = ("\033[0;37m")

Color_yellow = ("\033[1;93m")

The_price = Color_red+"The price"

The_price2 = Color_yellow+" $"

total = "total"

qus ="""1.Yes
2.NO"""

m = Color_red+"100%"

App_name = "Casher System"

Lod1 = "█▒▒▒▒▒▒▒▒▒▒" 

Lod2 = "██▒▒▒▒▒▒▒▒▒"

Lod3 = "███▒▒▒▒▒▒▒▒" 

Lod4 = "████▒▒▒▒▒▒▒" 

Lod5 = "█████▒▒▒▒▒▒" 

Lod6 = "██████▒▒▒▒▒" 

Lod7 = "███████▒▒▒▒" 

Lod8 = "████████▒▒▒" 

Lod9 = "█████████▒▒" 

Lod10 = "██████████"

Lod11 = Color_red+"Loding.. "

def Return():
  end2 = input(Color_blue+"Enter(End)to return:").lower()
  if end2 == "end":
    os.system("clear")
    time.sleep(0.3)
    a_n()
    print(Color_red+Offers)
  else:
    os.system("clear")
    return Return()
      

def new_account():
  while True:
    end = input(Color_blue+"Enter(end)to open a new account:").lower()
    if end == "end":
      os.system("clear")
      a_n()
      print(Color_red+Offers)
      return k()
    else:
      os.system("clear")
      return new_account()

def cm():
  print(Color_red+"﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏✎") 

def a_n():
  print(Color_black+"       ╔═══━━━───────── • ──────━━━═══╗""\n") 
 
  print(Color_blue+"                 Casher",Color_red+"  System""\n")

  print(Color_black+"       ╚═══━━━───────── • ──────━━━═══╝")
 
  print(Color_black+"•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*","•*´¨`*•.¸¸.•*´¨`*")

def Lodingg():
  time.sleep(1)
  os.system("clear")
  time.sleep(1)
  print(Lodd)
  print("10%")
  print(Lod1)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd)
  print("20%")
  print(Lod2)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd)
  print("30%")
  print(Lod3)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd)
  print("40%")
  print(Lod4)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd)
  print("50%")
  print(Lod5)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd)
  print("60%")
  print(Lod6)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd)
  print("70%") 
  print(Lod7)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd) 
  print("80%") 
  print(Lod8)
  time.sleep(0.2)
  os.system("clear") 
  print(Lodd) 
  print("90%")
  print(Lod9)
  time.sleep(0.2)
  os.system("clear")
  print(Lodd)
  print("100%")
  print(Lod10)
  time.sleep(0.8)
  
Lodd = Color_red+"Loding.."

The_products = "meet","milk","fish","pasta","rice","corn","flour","sauce","cheese","beef"

Offers ="""
 • ━━━━❪The products❫━━━━ • 
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█.meet = $15  fish = $10  █
█.milk = $5   beef = $14  █
█.pasta = $3  rice = $8   █
█.corn = $5   flour= $10  █
█.sauce  =$2  cheese = $6 █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                            
"""
settings ="""1.Add a product"""

Ss ="""1.Program guide
2.Program experience
3.settings"""

Soon_after ="""1.Delete a product
2.Add a product
3.User settings
4.Entry movements
5.User settings
6.The date of the invoice"""

Comma = "﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏✎" 

def k():
  os.system("clear")
  time.sleep(0.3)
  print(Color_blue+"Welcome to casher System")
  time.sleep(0.2)
  print(Color_red+Ss)
  Introductionn = int(input(Color_blue+"Choose:"))
  if Introductionn == 1:
    time.sleep(0.2)
    os.system("clear")
    time.sleep(0.3)
    print(Color_blue+"The program is incomplete")
    time.sleep(0.6)
    print(Color_blue+"It is being developed every day") 
    time.sleep(0.5)
    print("It is being worked on")
    print(Color_red+"Soon after:") 
    time.sleep(0.5)
    print(Color_red+Soon_after)
    Return()
  elif Introductionn == 2:
    os.system("clear")
    a_n()
    print(Color_red+Offers)
    time.sleep(0.2)
  elif Introductionn ==3:
    os.system("clear")
    time.sleep(0.3)
    print(Color_red+settings)
    c = int(input(Color_blue+"Enter the number:"))
    if c == 1:
      add = input(Color_blue+"Enter the product name:") 
      price = int(input(Color_blue+"Set the price:"))
      time.sleep(0.3)
      print("done..!")
      # Under development not completed
      time.sleep(0.2)
      os.system("clear")
      a_n()
      print(Color_red+"• ━━━━❪The products❫━━━━ •")
      print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄") 
      print("█.meet = $15  fish = $10    █") 
      print("█.milk = $5   beef = $14    █") 
      print("█.pasta = $3  rice = $8     █") 
      print("█.corn = $5   flour= $10    █") 
      print("█.sauce  =$2  cheese = $6   █") 
      print("█."+add,"="+" $",price,"                ") 
      print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█") 
  else:
    print(Color_red+"Enter the number correctly")
    time.sleep(0.8)
    os.system("clear")
    return k()
  while True:
    D = input(Color_blue+"Enter the name of the product you want:").lower()
    Q = int(input("Enter the quantity:"))
    if D in The_products:
      print(Color_red+qus)
      con = int(input(Color_blue+"If you're done,Enter the number:"))
      if con ==1:
        Lodingg()
        os.system("clear")
        time.sleep(0.2)
        print(Color_blue+"The bill:")
        time.sleep(0.2)
        print(The_price,D+" =",The_price2,dict[D])
        time.sleep(0.2)
        print(Color_red+"The quantity"+" =",Q)
        time.sleep(0.5)
        print(total+" =",Color_yellow+" $",dict[D]*Q)
        new_account()
      elif con == 2:
        os.system("clear")
        a_n()
        print(Color_red+Offers)
        time.sleep(0.2)
        print(The_price,D+" =",The_price2,dict[D])
        time.sleep(0.2)
        print(Color_red+Comma)
        time.sleep(0.2)
        Q2 = input(Color_blue+"Enter the name of the product you want:").lower()
        Q = int(input("Enter the quantity:"))
        if Q2 in The_products:
          print(Color_red+qus)
          con2 = int(input(Color_blue+"If you're done,Enter the number:"))
          if con2 ==1:
            Lodingg()
            os.system("clear")
            time.sleep(0.2)
            print(Color_blue+"The bill:")
            time.sleep(0.2)
            print(The_price,D+" =",The_price2,dict[D])
            time.sleep(0.2)
            print(Color_red+"The quantity"+" =",Q)
            cm() 
            time.sleep(0.2)
            print(The_price,Q2+" =",The_price2,dict[Q2])
            time.sleep(0.2)
            print(Color_red+"The quantity"+" =",Q) 
            cm()
            time.sleep(0.5)
            print(total+" =",Color_yellow+" $",dict[Q2]*Q+dict[D]*Q)
            new_account()
          elif con2 == 2:
            os.system("clear")
            a_n()
            print(Color_red+Offers)
            time.sleep(0.2)
            print(The_price,Q2+" =",The_price2,dict[Q2])
            time.sleep(0.2)
            print(Color_red+Comma)
            time.sleep(0.2)
            Q3 = input(Color_blue+"Enter the name of the product you want:").lower() 
            Q = int(input("Enter the quantity:"))
            if Q3 in The_products:
              print(Color_red+qus)
              con3 = int(input(Color_blue+"If you're done,Enter the number:"))
              if con3 ==1:
                Lodingg()
                os.system("clear")
                time.sleep(0.2)
                print(Color_blue+"The bill:")
                time.sleep(0.2)
                print(The_price,D+" =",The_price2,dict[D])
                time.sleep(0.2)
                print(Color_red+"The quantity"+" =",Q) 
                cm()
                time.sleep(0.2)
                print(The_price,Q2+" =",The_price2,dict[Q2])
                time.sleep(0.2)
                print(Color_red+"The quantity"+" =" ,Q)
                cm()
                time.sleep(0.2)
                print(The_price,Q3+" =",The_price2,dict[Q3])
                time.sleep(0.2)
                print(Color_red+"The quantity"+" =",Q)
                cm()
                time.sleep(0.5)
                print(total+" =",Color_yellow+" $", dict[Q3]*Q+dict[Q2]*Q+dict[D]*Q)
                new_account()
              elif con3 == 2:
                os.system("clear")
                a_n()
                print(Color_red+Offers)
                time.sleep(0.2)
                print(The_price,Q3+" =",The_price2,dict[Q3])
                time.sleep(0.2)
                print(Color_red+Comma)
                time.sleep(0.2)
                Q4 = input(Color_blue+"Enter the name of the product you want:").lower() 
                Q = int(input("Enter the quantity:"))
                if Q4 in The_products:
                  print(Color_red+qus)
                  con4 = int(input(Color_blue+"If you're done,Enter the number:"))
                  if con4 ==1:
                    Lodingg()
                    os.system("clear")
                    time.sleep(0.2)
                    print(Color_blue+"The bill:")
                    time.sleep(0.2)
                    print(The_price,D+" =",The_price2,dict[D])
                    time.sleep(0.2)
                    print(Color_red+"The quantity"+" =",Q)
                    cm()
                    time.sleep(0.2)
                    print(The_price,Q2+" =",The_price2,dict[Q2])
                    time.sleep(0.2)
                    print(Color_red+"The quantity"+" =",Q)
                    cm()
                    time.sleep(0.2)
                    print(The_price,Q3+" =",The_price2,dict[Q3])
                    time.sleep(0.2)
                    print(Color_red+"The quantity"+" =",Q)
                    cm()
                    time.sleep(0.2)
                    print(The_price,Q4+" =",The_price2,dict[Q4])
                    time.sleep(0.2)
                    print(Color_red+"The quantity"+" =",Q)
                    cm()
                    time.sleep(0.5) 
                    print(total+" =",Color_yellow+" $",dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q) 
                    new_account()
                  elif con4 == 2:
                    os.system("clear")
                    a_n()
                    print(Color_red+Offers)
                    time.sleep(0.2)
                    print(The_price,Q4+" =",The_price2,dict[Q4])
                    time.sleep(0.2)
                    print(Color_red+Comma)
                    time.sleep(0.2)
                    Q5 = input(Color_blue+"Enter the name of the product you want:").lower() 
                    Q = int(input("Enter the quantity:"))
                    if Q5 in The_products:
                      print(Color_red+qus)
                      con5 = int(input(Color_blue+"If you're done,Enter the number:"))
                      if con5 ==1:
                        Lodingg()
                        os.system("clear")
                        time.sleep(0.2)
                        print(Color_blue+"The bill:")
                        time.sleep(0.2)
                        print(Color_red+"The quantity"+" =",Q)
                        cm()
                        time.sleep(0.2)
                        print(The_price,D+" =",The_price2,dict[D])
                        time.sleep(0.2)
                        print(Color_red+"The quantity"+" =",Q)
                        cm()
                        time.sleep(0.2)
                        print(The_price,Q2+" =",The_price2,dict[Q2])
                        time.sleep(0.2)
                        print(Color_red+"The quantity"+" =",Q)
                        cm()
                        time.sleep(0.2)
                        print(The_price,Q3+" =",The_price2,dict[Q3])
                        time.sleep(0.2)
                        print(Color_red+"The quantity"+" =",Q)
                        cm()
                        time.sleep(0.2)
                        print(The_price,Q4+" =",The_price2,dict[Q4])
                        time.sleep(0.2)
                        print(Color_red+"The quantity"+" =",Q)
                        cm()
                        time.sleep(0.2)
                        print(The_price,Q5+" =",The_price2,dict[Q5])
                        time.sleep(0.2)
                        print(Color_red+"The quantity"+" =",Q)
                        cm()
                        time.sleep(0.5)  
                        print(total+" =",Color_yellow+" $",dict[Q5]*Q+dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q)
                        new_account()
                      elif con5 == 2:
                        os.system("clear")
                        a_n()
                        print(Color_red+Offers)
                        time.sleep(0.2)
                        print(The_price,Q5+" =",The_price2,dict[Q5])
                        time.sleep(0.2)
                        print(Color_red+Comma)
                        time.sleep(0.2)
                        Q6 = input(Color_blue+"Enter the name of the product you want:").lower()
                        Q = int(input("Enter the quantity:"))
                        if Q5 in The_products:
                          print(Color_red+qus)
                          con6 = int(input(Color_blue+"If you're done,Enter the number:"))
                          if con6 ==1:
                            Lodingg()
                            os.system("clear")
                            time.sleep(0.2)
                            print(Color_blue+"The bill:")
                            time.sleep(0.2)
                            print(The_price,D+" =",The_price2,dict[D])
                            time.sleep(0.2)
                            print(Color_red+"The quantity"+" =",Q)
                            cm()
                            time.sleep(0.2)
                            print(The_price,Q2+" =",The_price2,dict[Q2])
                            time.sleep(0.2)
                            print(Color_red+"The quantity"+" =",Q)
                            cm()
                            time.sleep(0.2)
                            print(The_price,Q3+" =",The_price2,dict[Q3])
                            time.sleep(0.2)
                            print(Color_red+"The quantity"+" =",Q)
                            cm()
                            time.sleep(0.2)
                            print(The_price,Q4+" =",The_price2,dict[Q4])
                            time.sleep(0.2)
                            print(Color_red+"The quantity"+" =",Q)
                            cm()
                            time.sleep(0.2)
                            print(The_price,Q5+" =",The_price2,dict[Q5])
                            time.sleep(0.2)
                            print(Color_red+"The quantity"+" =",Q)
                            cm()
                            time.sleep(0.2)
                            print(The_price,Q6+" =",The_price2,dict[Q6])
                            time.sleep(0.2)
                            print(Color_red+"The quantity"+" =",Q)
                            cm()
                            time.sleep(0.5)   
                            print(total+" =",Color_yellow+" $",dict[Q6]*Q+dict[Q5]*Q+dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q)
                            new_account()
                          elif con6 == 2:
                            os.system("clear")
                            a_n()
                            print(Color_red+Offers)
                            time.sleep(0.2)
                            print(The_price,Q6+" =",The_price2,dict[Q5])
                            time.sleep(0.2)
                            print(Color_red+Comma)
                            time.sleep(0.2)
                            Q7 = input(Color_blue+"Enter the name of the product you want:").lower()
                            Q = int(input("Enter the quantity:"))
                            if Q7 in The_products:
                              print(Color_red+qus)
                              con7 = int(input(Color_blue+"If you're done,Enter the number:"))
                              if con7 ==1:
                                Lodingg()
                                os.system("clear")
                                time.sleep(0.2)
                                print(Color_blue+"The bill:")
                                time.sleep(0.2)
                                print(The_price,D+" =",The_price2,dict[D])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.2)
                                print(The_price,Q2+" =",The_price2,dict[Q2])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.2)
                                print(The_price,Q3+" =",The_price2,dict[Q3])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.2)
                                print(The_price,Q4+" =",The_price2,dict[Q4])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.2)
                                print(The_price,Q5+" =",The_price2,dict[Q5])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.2)
                                print(The_price,Q6+" =",The_price2,dict[Q6])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.2)
                                print(The_price,Q7+" =",The_price2,dict[Q7])
                                time.sleep(0.2)
                                print(Color_red+"The quantity"+" =",Q)
                                cm()
                                time.sleep(0.5)   
                                print(total+" =",Color_yellow+" $",dict[Q7]*Q+dict[Q6]*Q+dict[Q5]*Q+dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q)
                                new_account()
                              elif con7 == 2:
                                os.system("clear")
                                a_n()
                                print(Color_red+Offers)
                                time.sleep(0.2)
                                print(The_price,Q7+" =",The_price2,dict[Q7])
                                time.sleep(0.2)
                                print(Color_red+Comma)
                                time.sleep(0.2)
                                Q8 = input(Color_blue+"Enter the name of the product you want:").lower()
                                Q = int(input("Enter the quantity:"))
                                if Q8 in The_products:
                                  print(Color_red+qus)
                                  con8 = int(input(Color_blue+"If you're done,Enter the number:"))
                                  if con8 ==1:
                                    Lodingg()
                                    os.system("clear")
                                    time.sleep(0.2)
                                    print(Color_blue+"The bill:")
                                    time.sleep(0.2)
                                    print(The_price,D+" =",The_price2,dict[D])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q2+" =",The_price2,dict[Q2])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q3+" =",The_price2,dict[Q3])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q4+" =",The_price2,dict[Q4])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q5+" =",The_price2,dict[Q5])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q6+" =",The_price2,dict[Q6])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q7+" =",The_price2,dict[Q7])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.2)
                                    print(The_price,Q8+" =",The_price2,dict[Q8])
                                    time.sleep(0.2)
                                    print(Color_red+"The quantity"+" =",Q)
                                    cm()
                                    time.sleep(0.5)
                                    print(total+" =",Color_yellow+" $",dict[Q8]*Q+dict[Q7]*Q+dict[Q6]*Q+dict[Q5]*Q+dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q)
                                    new_account()
                                  elif con8 == 2:
                                    os.system("clear")
                                    a_n()
                                    print(Color_red+Offers)
                                    time.sleep(0.2)
                                    print(The_price,Q8+" =",The_price2,dict[Q8])
                                    time.sleep(0.2)
                                    print(Color_red+Comma)
                                    time.sleep(0.2)
                                    Q9 = input(Color_blue+"Enter the name of the product you want:").lower()
                                    Q = int(input("Enter the quantity:"))
                                    if Q9 in The_products:
                                      print(Color_red+qus)
                                      con9 = int(input(Color_blue+"If you're done,Enter the number:"))
                                      if con9 ==1:
                                        Lodingg()
                                        os.system("clear")
                                        time.sleep(0.2)
                                        print(Color_blue+"The bill:")
                                        time.sleep(0.2)
                                        print(The_price,D+" =",The_price2,dict[D])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(The_price,Q2+" =",The_price2,dict[Q2])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm() 
                                        time.sleep(0.2)
                                        print(The_price,Q3+" =",The_price2,dict[Q3])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(The_price,Q4+" =",The_price2,dict[Q4])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(The_price,Q5+" =",The_price2,dict[Q5])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(The_price,Q6+" =",The_price2,dict[Q6])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(The_price,Q7+" =",The_price2,dict[Q7])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(The_price,Q8+" =",The_price2,dict[Q8])
                                        time.sleep(0.2)
                                        print(The_price,Q9+" =",The_price2,dict[Q9])
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.2)
                                        print(Color_red+"The quantity"+" =",Q)
                                        cm()
                                        time.sleep(0.5) 
                                        print(total+" =",Color_yellow+" $",dict[Q9]*Q+dict[Q8]*Q+dict[Q7]*Q+dict[Q6]*Q+dict[Q5]*Q+dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q)
                                        new_account()
                                      elif con9 == 2:
                                        os.system("clear")
                                        a_n()
                                        print(Color_red+Offers)
                                        time.sleep(0.2)
                                        print(The_price,Q9+" =",The_price2,dict[Q9])
                                        time.sleep(0.2)
                                        print(Color_red+Comma)
                                        time.sleep(0.2)
                                        Q10 = input(Color_blue+"Enter the name of the product you want:").lower()
                                        Q = int(input("Enter the quantity:"))
                                        if Q10 in The_products:
                                          print(Color_red+qus)
                                          con10 = int(input(Color_blue+"If you're done,Enter the number:"))
                                          if con10 ==1:
                                            Lodingg()
                                            os.system("clear")
                                            time.sleep(0.2)
                                            print(Color_blue+"The bill:")
                                            time.sleep(0.2)
                                            print(The_price,D+" =",The_price2,dict[D])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q2+" =",The_price2,dict[Q2])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q3+" =",The_price2,dict[Q3])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q4+" =",The_price2,dict[Q4])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q5+" =",The_price2,dict[Q5])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q6+" =",The_price2,dict[Q6])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q7+" =",The_price2,dict[Q7])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q8+" =",The_price2,dict[Q8])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q9+" =",The_price2,dict[Q9])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.2)
                                            print(The_price,Q10+" =",The_price2,dict[Q10])
                                            time.sleep(0.2)
                                            print(Color_red+"The quantity"+" =",Q)
                                            cm()
                                            time.sleep(0.5)  
                                            print(total+" =",Color_yellow+" $",dict[Q10]*Q+dict[Q9]*Q+dict[Q8]*Q+dict[Q7]*Q+dict[Q6]*Q+dict[Q5]*Q+dict[Q2]*Q+dict[Q3]*Q+dict[Q4]*Q+dict[D]*Q)
                                            new_account()
                                          elif con10 == 2:
                                            os.system("clear")
                                            a_n()
                                            print(Color_red+Offers)
                                            time.sleep(0.2)
                                            print(The_price,Q10+" =",The_price2,dict[Q10])
                                            time.sleep(0.2)
                                            print(Color_red+Comma)
                                            time.sleep(0.2)
                                            break
                                          else:
                                            print(Color_red+"Enter the number correctly")
                                            time.sleep(0.8)
                                            os.system("clear")
                                            a_n()
                                            print(Color_red+Offers)
                                            continue
                                        else:
                                          print(Color_red+"The entrance number doesn't exist")
                                          time.sleep(1.5)
                                          os.system("clear")
                                          a_n()
                                          print(Color_red+Offers)
                                        continue
                                      else:
                                        print(Color_red+"Enter the number correctly")
                                        time.sleep(0.8)
                                        os.system("clear")
                                        a_n()
                                        print(Color_red+Offers)
                                        continue
                                    else:
                                      print(Color_red+"The entrance number doesn't exist")
                                      time.sleep(1.5)
                                      os.system("clear")
                                      a_n()
                                      print(Color_red+Offers)
                                      continue    
                                  else:
                                    print(Color_red+"Enter the number correctly")
                                    time.sleep(0.8)
                                    os.system("clear")
                                    a_n()
                                    print(Color_red+Offers)
                                    continue
                                else:
                                  print(Color_red+"The entrance number doesn't exist")
                                  time.sleep(1.5)
                                  os.system("clear")
                                  a_n()
                                  print(Color_red+Offers)
                                  continue
                              else:
                                print(Color_red+"Enter the number correctly")
                                time.sleep(0.8)
                                os.system("clear")
                                a_n()
                                print(Color_red+Offers)
                                continue
                            else:
                              print(Color_red+"The entrance number doesn't exist")
                              time.sleep(1.5)
                              os.system("clear")
                              a_n()
                              print(Color_red+Offers)
                              continue
                          else:
                            print(Color_red+"Enter the number correctly")
                            time.sleep(0.8)
                            os.system("clear")
                            a_n()
                            print(Color_red+Offers)
                            continue
                        else:
                          print(Color_red+"The entrance number doesn't exist")
                          time.sleep(1.5)
                          os.system("clear")
                          a_n()
                          print(Color_red+Offers)
                          continue
                      else:
                        print(Color_red+"Enter the number correctly")
                        time.sleep(0.8)
                        os.system("clear")
                        a_n()
                        print(Color_red+Offers)
                        continue
                    else:
                      print(Color_red+"The entrance number doesn't exist")
                      time.sleep(1.5)
                      os.system("clear")
                      a_n()
                      print(Color_red+Offers)
                      continue  
                  else:
                    print(Color_red+"Enter the number correctly")
                    time.sleep(0.8)
                    os.system("clear")
                    a_n()
                    print(Color_red+Offers)
                    continue
                else:
                  print(Color_red+"The entrance number doesn't exist")
                  time.sleep(1.5)
                  os.system("clear")
                  a_n()
                  print(Color_red+Offers)
                  continue
              else:
                print(Color_red+"Enter the number correctly")
                time.sleep(0.8)
                os.system("clear")
                a_n()
                print(Color_red+Offers)
                continue
            else:
              print(Color_red+"The entrance number doesn't exist")
              time.sleep(1.5)
              os.system("clear")
              a_n()
              print(Color_red+Offers)
              continue
          else:
            print(Color_red+"Enter the number correctly")
            time.sleep(0.8)
            os.system("clear")
            a_n()
            print(Color_red+Offers)
            continue
        else:
          print(Color_red+"The entrance number doesn't exist")
          time.sleep(1.5)
          os.system("clear")
          a_n()
          print(Color_red+Offers)
          continue
      else:
        print(Color_red+"Enter the number correctly")
        time.sleep(0.8)
        os.system("clear")
        a_n()
        print(Color_red+Offers)
        continue
    else:
      print(Color_red+"Enter the product correctly")
      time.sleep(1.5)
      os.system("clear")
      a_n()
      print(Color_red+Offers)
      continue
      
  
while True:
  try:
    k()
  except ValueError:
    print(Color_red+"No letters")
    time.sleep(1)
    os.system("clear")
    a_n()
    print(Color_red+Offers)
    continue
  break
