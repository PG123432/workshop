# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #will go to the terminal
    return "No hablo queso!"

app.debug = True # when I make an error in the file, such as having an undefined variable
#there now opens a new menu that will outline the error. I think this is the debug menu
app.run()

#also when I save things the server reloads, which is interesting. 
