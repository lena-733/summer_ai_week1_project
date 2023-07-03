#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()


#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()


    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            usernameinput = input("create a username\n")
            #validusername = True
            #while validusername == True:
                #usernameinput = input("create a username\n")
                #if usernameinput in ai_social_network.list_of_usernames:
                    #print("already in use")
                    #validusername = True
                #else:
                    #validusername = False

            ai_social_network.create_account(usernameinput)
            

        elif choice == "2":
            valid = True
            while valid == True:
                mainUsername = input("Hey what's your username?\n")
                if mainUsername in ai_social_network.list_of_usernames:
                        valid = False
                else:
                        print("not valid")
                        valid = True

            CurrentUser = ai_social_network.main_user(mainUsername)
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here

            
            while True:
                if inner_menu_choice == "7":
                    break
                elif inner_menu_choice == "1":

                    ai_social_network.edit_account(CurrentUser)
                    
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == "2":
                    print("You are now looking for friends!!")
                    print("here are all the people: "+ str(ai_social_network.list_of_usernames))
                    validfriend = True
                    while validfriend == True:
                        newFriendUsername = input("Who do you want to befriend?\n")
                        if newFriendUsername in ai_social_network.list_of_usernames:
                            validfriend = False
                        else:
                            print("not valid")
                            validfriend = True
                    friendIndex = ai_social_network.list_of_usernames.index(newFriendUsername)
                    newFriendPerson = ai_social_network.list_of_people[friendIndex]
                    CurrentUser.add_friend(newFriendPerson, newFriendUsername)
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == "3":
                    print("here are your friends: "+ str(CurrentUser.friendlistUsernames))
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                elif inner_menu_choice == "4":
                    validmessage = True
                    while validmessage == True:
                        recipient = input("who do you wanna send the message to?\n")
                        if recipient in ai_social_network.list_of_usernames:
                            validmessage = False
                        else:
                            print("not valid")
                            validmessage = True

                    premessage = input("what is the message?\n")
                    message = premessage+" -"+ CurrentUser.id
                    friendIndex = ai_social_network.list_of_usernames.index(recipient)
                    toFriend = ai_social_network.list_of_people[friendIndex]
                    toFriend.inbox.append(message)
                    print(str(toFriend.inbox))
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == "5":
                    print(str(CurrentUser.friendlistUsernames))
                    validblock = True
                    while validblock == True:
                        block = input("who do you wanna block?\n")
                        if block in ai_social_network.list_of_usernames:
                            
                                validblock = False
                        else:
                                print("not valid")
                                validblock = True
                    
                    blockIndex = CurrentUser.friendlistUsernames.index(block)
                    CurrentUser.friendlist.pop(blockIndex)
                    CurrentUser.friendlistUsernames.pop(blockIndex)
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                    print(str(CurrentUser.friendlistUsernames))
                elif inner_menu_choice == "6":
                    print("here are your messages: " + str(CurrentUser.inbox))
                    inner_menu_choice = social_network_ui.manageAccountMenu()




        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
