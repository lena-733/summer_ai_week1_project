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
            ai_social_network.create_account()
            

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            CurrentUser = ai_social_network.main_user()
            #EDDDIITTTT HERERERER

            while True:
                if inner_menu_choice == "5":
                    break
                elif inner_menu_choice == "1":
                    username =input("\nYou are now editing an account\nWhat is your username\n")
                    ai_social_network.edit_account(username)
                    
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == "2":
                    print("You are now looking for friends!!")
                    newFriendUsername = input("Who do you want to befriend?\n")
                    CurrentUser.add_friend(newFriendUsername)


        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
