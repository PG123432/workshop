from flask import Flask, render_template, request, session
import os
#dependencies....

app = Flask(__name__)


app.secret_key = os.urandom(32)

#some constants because I don't feel like putting in 
# "username" in, also easier to clean up when we need to
USERNAME = "username"
PASSWORD = "password"

#login page
@app.route("/", methods=["GET"])
def index():

    if 'username' in session.keys() and 'password' in session.keys():
        if session['username'] == USERNAME and session['password'] == PASSWORD:
            #only if the code was right will we send them to success.html
            return render_template("success.html", 
                username = session['username'], 
                password = session['password'])
        
    return render_template("login.html")


@app.route("/auth", methods=['GET', 'POST'])
def auth():
    '''
    POST
    Checking if the passwords are matching will render in both username and password

    Validation is done server side and we pass in booleans to tell the rendering what to do 
    Perhaps a bad idea, but time will tell

    Creating a session with the username and password in it.
    All you have to do is session[property] = blah
    '''

    if request.method == "POST":
        #storing the username and password in the session
        session['username'] = request.form['username']
        session['password'] = request.form['password']



        '''
        Stuff being rendered in

        username: username from form
        password: password from form
        username_match: if the username's correct
        passwords_match: if the password is correct
        '''
        if session['username'] == USERNAME and session['password'] == PASSWORD:
            #if the passwords match render in the success portal
            return render_template("success.html",
                username = session['username'],
                password = session['password'])
        else:
            #elsewise render in the failure with bools
            #to describe what went
            return render_template("failure.html", 
                username = session['username'], 
                password = session['password'], 
                username_match= session['username'] == USERNAME,
                password_match= session['password'] == PASSWORD)

    else:
        '''
        GET

        Will check for a session, if there's nothing, then we'll redirect them to the 
        home page with some instructions saying "please log in!"
        '''
        if 'username' in session.keys() and 'password' in session.keys():
            #checking if the properties were logged into the keys
            return render_template("response.html", 
                username = session['username'], 
                password = session['password'], 
                username_match= session['username'] == USERNAME,
                password_match= session['password'] == PASSWORD)
        else:
            #if for some reason the session isn't here we'll just redirect them back
            return render_template("login.html")



@app.route("/logout", methods=["POST"])
def logout():
    #getting rid of the session's details
    session.pop("username")
    session.pop("password")

    #sending them back home
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
