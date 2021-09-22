'''

Eric Guo, Hebe Huang, and Patrick Ging - Period 2

Prints the name of a student in the github group.

Dependencies: pyGitHub

Do $pip install PyGitHub

or if it fails b/c you're on 2.7 as default $pip3 install PyGitHub

'''

from github import Github
import random


#creating a github instance using public access token
gh = Github("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")


#getting the organization and its members

softdev_class = gh.get_organization("stuy-softdev").get_members()
# ^ this returns a weird class called a paginated list
# so I have to use totalCount instead of len()


while True:
    student = softdev_class[random.randint(0, softdev_class.totalCount -1)]


    '''
    Have a while loop here because it seems that some people don't have a
    name listed and it just returns none...so we have to have the loop
    '''
    if student.name is not None:
        print(student.name)
        break
