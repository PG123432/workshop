# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"



'''
Our group had an experiment where we imported the below code in as a module.
When we ran the function that the code was contained in, we didn't get any results.
We added print(__name__) into that function, and it printed "file" (the name
of the file). I'm assuming that __name__ is __main__ when it's the file we're perhaps
running with python3?
'''
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
