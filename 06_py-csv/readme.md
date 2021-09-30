Team "The Nameless Team" Eric Guo, Hebe Huang, Patrick Ging  
SoftDev
# K06 Random Occupation
## Explaining how Hw_06 Solution operates 
* Firstly we imported the csv and random libraries - it has functions we will use later. 
* Then we opened our occupations.csv file, which has the job name followed by the probability of it appearing.
* We used the csv modules' csv.reader() (which allows us to parse a csv file) to read the contents of occupations.csv. We multiplied all percentages by 10 so that we can work with whole numbers instead of decimals.
* After skipping the first line with next(csv_reader), we set up our dictionary.
**A dictionary, like its real life counterpart, has some input, called a key, that maps to an output, called its value. In real life a word is our key mapping to its definition - the value. It's useful mostly because it allows us to associate various pieces of data with each other in one structure.**

We then went through the values in occupations.csv. In order to set up a dictionary for the purpose of randomly selecting an item according to given percentages, we had the key for each occupation be the upper bound of an interval such that the size of the interval relative to the highest interval (998) was equal to the percentage assigned to it in occupations.csv. We used a variable sum that started out as 0. After each iteration sum was increased by the percentage of the next occupation and set as the key to its corresponding occupation... Our dictionary now contains a number line of all the intervals of each occupation.

**A list is, as the name puts it, a record of values of any type. It is easy to use and we're able to go through it's values in a for loop**

With our new dictionary ready, we used the random libraries' random.randrange(998) to pick a random integer from 0 to 998, inclusive - this is because 998 is the sum of our percentages multiplied by 10 . This random number represents picking a random job.

Using a for loop that iterates through the intervals' keys (using the .keys() function) we checked if the number fit in the interval associated with the occupation by checking if the random number was less than the value of the key we were looking at in the for loop. 

**Because the number is random, there is an equal chance of getting any number from 0 to 998 and the chance of picking an occupation is solely dependent on the numbers acquired in occupations.csv. Therefore the bigger the interval that an occupation has in the dictionary, the more likely our random number will fall into that interval and the occupation will be chosen.**

## Explaining Github-flavored Markdown
**Markdown is a syntax that lets us style and format text. Some examples of Markdown syntax are:**
```
- (* or -) for lists
- (**<text>**) for bold
- (# <text>) for headers 
```
