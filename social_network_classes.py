# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
import json
import os
class SocialNetwork:
    def __init__(self):
        self.list_of_people = []
        self.list_of_usernames = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        for i in self.list_of_people:
            i.serialize()
            data = json.dumps(i) # Convert the response to JSON
            with open("savedinfo.json", "w") as file:
                json.dump(data, file)
        
        for e in self.list_of_usernames:
            datausernames = json.dumps(e)
            with open("savedusernames.json", "w") as file2:
                json.dump(datausernames, file2)

        #f = open(savedinformation.txt)
        #for i in self.list_of_people:
            #json.dumps(i.__dic__)
        

        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        with open("savedinfo.json", "r") as file:
            data = json.load(file)

# Access and process the retrieved JSON data
        self.list_of_people = data["data"]["list_of_people"]
        with open("savedusernames.json", "r") as file2:
            data2 = json.load(file)
        self.list_of_usernames = data2["data2"]["list_of_usernames"]
        pass

    def  create_account(self, username):
        age = input("And what is your age?\n")
        mainAccount = Person(username, age)
        self.list_of_people.append(mainAccount)
        self.list_of_usernames.append(username)
        print(str(self.list_of_usernames))
        #implement function that creates account here
        #create instance of person object
        pass
    
    def edit_account(self, person):
        index = self.list_of_people.index(person)
        newName = input("What new username?\n")
        newAge = input("What new age?\n")
        editAccount = Person(newName, newAge)
        self.list_of_people[index] = editAccount
        self.list_of_usernames[index] = newName
        print(str(self.list_of_usernames))
    
    def main_user(self, username):
        index = self.list_of_usernames.index(username)
        currentuser = self.list_of_people[index]
        return currentuser


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.friendlistUsernames = []
        self.inbox = []

    def add_friend(self, newFriendPerson, newFriendUsername):
        self.friendlist.append(newFriendPerson)
        self.friendlistUsernames.append(newFriendUsername)
        print(str(self.friendlistUsernames))


        #implement adding friend. Hint add to self.friendlist
        pass