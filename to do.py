from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

def add():
    ob=w.wthido.text()
    #ob is the object from line edit "wthido"
    if not(ob!=""):
        QMessageBox.critical(w,"error","Write anything to make it work")
    else:
        #f It is the variable that will pull information from the file "the objects"
        f=open("the objects.txt","a")
        f.write(ob+"\n")
        f.close()
        w.list.clear()
        w.wthido.clear()
        f=open("the objects.txt","r")
        for obj in f:
            w.list.addItem(obj.strip())
        f.close()
def delet():

    item=w.list.currentItem()
    

    if item:
        
        text=item.text()
        w.list.clear()
        #too it is the list Where we will put the information from that file "the objects"
        too=[]
        f=open("the objects.txt","r")
        for obj in f:
            too.append(obj.strip())
        f.close()
        f=open("the objects.txt","w")
        for i in too:
            if text!=i:
                f.write(i+"\n")
        f.close()
        f=open("the objects.txt","r")
        for obj in f:
            w.list.addItem(obj.strip())
        f.close()
    elif test()==0:
        QMessageBox.critical(w,"error","Record anything on the list")
    else:
        QMessageBox.critical(w,"error","Click on any information in the list")



def test():
    f=open("the objects.txt","r")
    s=0
    for obj in f:
        s=s+1
    f.close()
    return s
        




    
    
       



app = QApplication([])
w = loadUi ("widjet.ui")
f=open("the objects.txt","r")
for obj in f:
    w.list.addItem(obj.strip())
f.close()
w.show()
w.buttonAdd.clicked.connect (add)
w.buttonDelet.clicked.connect (delet)

app.exec()
