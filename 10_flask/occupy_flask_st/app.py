from flask import Flask
import csv
import random

app = Flask(__name__)

@app.route("/")
def index():
    job_and_prob = {} 

    with open ("occupations.csv", "r") as f:

            csv_reader = csv.reader(f, delimiter=",") 
            next(csv_reader)
            sum = 0.0


            returnString = '<h2>The Nameless Team: Patrick Ging, Eric Guo, Hebe Huang</h2> </hr>' #bottom part with our job

            jobTable = "<table> <tr> <th> Possible Jobs </th> </tr>" #top part with table

            
            for value in csv_reader:
                            if(value[0] == "Total"):
                                    continue
                            sum = sum + (10 * float(value[1])) #adding the values
                            job_and_prob[sum] = value[0]

                            jobTable += "\n<tr> <td> " + value[0] + " </tr></td>"
        

            randNum = random.randrange(998) #random number
            for percent in job_and_prob.keys():
                if(percent >= randNum):
                    returnString += "<h2> Your job is {} </h2></hr>".format(job_and_prob[percent])
                    break
                    #if it's below the value that means it's in between it and the value before it -
                    #elsewise we know it's above the value so we don't actually need another logic operator

            return returnString + jobTable
                
                        
if __name__ == "__main__":  
    app.debug = True       
    app.run()
