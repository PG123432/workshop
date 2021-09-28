'''
Group "A Nameless Group": Hebe Huang, Patrick Ging, Eric Guo, Period 2

# SUMMARY OF TRIO DISCUSSION
  We disucssed 2 aspects of design - one being assembling the dictionary from the CSV
  file and making the match given the percentages being floats from 1 - 100.
  After that we simply discussed making our code more readable and helped Eric fix his pip.
# DISCOVERIES
  csv.csv_reader has a next() function that allows us to be handle the headers more easily
# QUESTIONS
  What is the actual efficiency of reading a CSV file? Is it ideal to leave the context manager asap or
  is it cool to stay in there for readability.
# COMMENTS
  Our group has really developed good chemistry and they're a great group 

'''
import csv
import random
#dependencies

job_and_prob = {} #dictionary that will be holding a number derived from its percentage as key and the occupation as output


with open ("occupations.csv", "r") as f:

        csv_reader = csv.reader(f, delimiter=",") #creating instance of reader from the occupations.csv
        next(csv_reader)
        sum = 0.0 #used for multiline comment below to establish the sum of former values


        '''
        How the input works.

        Suppose we had this as our sample input

        Teacher, 50
        Programmer, 25
        Other, 25

        To be able to easily implement the randomness whilst maintaining the percentages we used the sum of the previous probabilities and the current probability for the key value

        so in turn it would look like

        {50: "Teacher", "75": Programmer, "100","Other"}

        And we multiplied the numbers by 10 just so we can use random.randint easily.


        '''

        for value in csv_reader:
                if(value[0] == "Total"):
                        continue
                sum = sum + (10 * float(value[1])) #adding the values
                job_and_prob[sum] = value[0]


        

        randNum = random.randrange(998) #random number
        for percent in job_and_prob.keys():
                if(percent >= randNum): #if it's below the value that means it's in between it and the value before it - elsewise we know it's above the value so we don't actually need another logic operator
                        print(job_and_prob.get(percent))
                        break



