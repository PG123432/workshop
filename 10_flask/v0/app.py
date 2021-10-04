# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) # Q0: I've seen this syntax in Java with constructors.

@app.route("/") # Q1: I think that "/" signifies the most broad directory - I want to say it means index, but I'm not sure.
def hello_world():
    print(__name__) # Q2: This will print to the terminal? Q3: It will print "__main__"
    return "No hablo queso!"  # Q3: This will appear on the screen.

app.run()  # Q4: I think there's a similar function in tkinter. 
                
