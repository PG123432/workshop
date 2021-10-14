'''
    Team Atom

    Patrick Ging, Qina Liu, Joshua Kleopfar 
    Period 2
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST']) <- Don't need this we only need a get request
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == "POST":
        return render_template("response.html", username=request.form.get("username") )        
        '''
        So if you want to get form data from a POST request you need to do request.form.get("bluh")
        But if it's from a get you need request.args.get("firstname")

        I'm guessing we're using a post here so this is what it does.

        '''
    else:
        return render_template("login.html") # just doing this because refreshing on the /auth was bothering me lmao
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
