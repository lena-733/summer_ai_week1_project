# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = []
        self.list_of_usernames = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        username = input("Let's make an account!\nWhat is your new username?\n")
        age = input("And what is your age?\n")
        mainAccount = Person(username, age)
        self.list_of_people.append(mainAccount)
        self.list_of_usernames.append(username)
        print(str(self.list_of_usernames))
        #implement function that creates account here
        #create instance of person object
        pass
    
    def edit_account(self, username):
        index = self.list_of_usernames.index(username)
        newName = input("What new username?\n")
        newAge = input("What new age?\n")
        editAccount = Person(newName, newAge)
        self.list_of_people[index] = editAccount
        self.list_of_usernames[index] = newName
        print(str(self.list_of_usernames))
    
    def main_user(self,username):
        return currentuser


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.friendlistUsernames = []
        self.inbox = []

    def add_friend(self, person_object):
        print(str(self.list_of_usernames))
        friendIndex = self.list_of_usernames.index(person_object)
        newFriendPerson = self.list_of_people[friendIndex]
        self.friendlist.append(newFriendPerson)
        self.friendlistUsernames.append(person_object)
        print(str(self.friendlistUsernames))


        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self, friend_name, message):
        #implement sending message to friend here
        #access list of people and then add to their inbox
        pass
