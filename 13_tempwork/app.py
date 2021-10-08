

from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

@app.route("/occupyflaskst")
def index():
    job_and_prob = {}

    with open ("occupations.csv", "r") as f:

            csv_reader = csv.reader(f, delimiter=",")
            next(csv_reader)
            sum = 0.0



            for value in csv_reader:
                            if(value[0] == "Total"):
                                    continue
                            sum = sum + (10 * float(value[1])) #adding the values
                            job_and_prob[sum] = value[0]




            randNum = random.randrange(998) #random number
            for percent in job_and_prob.keys():
                if(percent >= randNum):
                    returnString += "<h2> Your job is {} </h2></hr>".format(job_and_prob[percent])
                    break
                    #if it's below the value that means it's in between it and the value before it -
                    #elsewise we know it's above the value so we don't actually need another logic operator

            render_template("template.html", )


if __name__ == "__main__":
    app.debug = True
    app.run()
