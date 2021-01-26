from graphics import *
from random import*

def main():
   
   print ("Dice roll")

   win = GraphWin("Dice", 700, 400)
   rect1 = Rectangle(Point(280,280), Point(80,80))
   win.setBackground("Grey")
   rect1.setFill("white")
   rect1.draw(win)

   rect2 = Rectangle(Point(400, 280), Point (600  ,80))
   rect2.setFill("white")
   rect2.draw(win)

   #Display message
   text = Text(Point(60,10), ("Click to roll dice: "))
   text.draw(win)
   #Define die faces
   center = Point(180,180) #mid
   side1 = Circle(center, 15)
   side1.setFill("Blue")

   center2 = Point(110,180)  #mid lef
   side2 = Circle(center2, 15)
   side2.setFill("Blue")

   center3 = Point(250,180)  #mid rig
   side3 = Circle(center3, 15)
   side3.setFill("Blue")

   center4 = Point(110,115) # top L
   side4 = Circle(center4, 15)
   side4.setFill("Blue")

   center5 = Point(250,115) # top rig
   side5 = Circle(center5, 15)
   side5.setFill("Blue")

   center6 = Point(110,235)    #bottom left
   side6 = Circle(center6, 15)
   side6.setFill("Blue")

   center7 = Point(250,235) #bottom right 2
   side7 = Circle(center7, 15)
   side7.setFill("Blue")

   # Second dice
   center8 = Point(500,180)     #die 2 mid 2
   side8 = Circle(center8, 15)
   side8.setFill("Red")

   center9 = Point(430,180)
   side9 = Circle(center9, 15)    #mid lef 2
   side9.setFill("Red")

   center10 = Point(570,180)
   side10 = Circle(center10, 15) #mid rig 2
   side10.setFill("Red")

   center11 = Point(430,115)
   side11 = Circle(center11, 15) # top L 2
   side11.setFill("Red")

   center12 = Point(570,115)
   side12 = Circle(center12, 15)  # top rig 2
   side12.setFill("Red")

   center13 = Point(430,235)
   side13 = Circle(center13, 15)  #bottom left 2
   side13.setFill("Red")

   center14 = Point(570,235)
   side14 = Circle(center14, 15)  #bottom right 2
   side14.setFill("Red")

   #Set loops for each die
   
   for i in range(5):
      win.getMouse()
      Roll = randint(1,6)
      Roll2 = randint(7,12)

      if Roll == 1:
        side1.draw(win)
      if Roll == 2:
        side11.draw(win)
        side14 .draw(win)
      if Roll == 3:
        side1.draw(win)
        side4.draw(win)
        side7.draw(win)
      if Roll == 4:
        side4.draw(win)
        side5.draw(win)
        side6.draw(win)
        side7.draw(win)
      if Roll == 5:
        side1.draw(win)
        side4.draw(win)
        side6.draw(win)
        side5.draw(win)
        side7.draw(win)
      if Roll == 6:
        side2.draw(win)
        side4.draw(win)
        side6.draw(win)
        side3.draw(win)
        side5.draw(win)
        side7.draw(win)

      #RN 2
      if Roll2 == 7:
        side8.draw(win)
      if Roll2 == 8:
        side13.draw(win)
        side12.draw(win)
      if Roll2 == 9:
        side11.draw(win)
        side8.draw(win)
        side14.draw(win)
      if Roll2 == 10:
        side11.draw(win)
        side12.draw(win)
        side13.draw(win)
        side14.draw(win)
      if Roll2 == 11:
        side11.draw(win)
        side12.draw(win)
        side13.draw(win)
        side14.draw(win)
        side8.draw(win)
      if Roll2 == 12:
        side9.draw(win)
        side10.draw(win)
        side11.draw(win)
        side12.draw(win)
        side13.draw(win)
        side14.draw(win)

      side1.undraw()
      side2.undraw()
      side3.undraw()
      side4.undraw()
      side5.undraw()
      side6.undraw()
      side7.undraw()
      side8.undraw()
      side9.undraw()
      side10.undraw()
      side11.undraw()
      side12.undraw()
      side13.undraw()
      side14.undraw()
      
      
      text2 = Text(Point(310,180), ("        Again "))
      text2.draw(win)
      if win.getMouse():
         text2.undraw()
      
     
   #Change message
   text.undraw()
   text3 = Text(Point(80,10), ("Click Anywhere to exit: "))
   text3.draw(win)

   win.getMouse()
   win.close()

main()
