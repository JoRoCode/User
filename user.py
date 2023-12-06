class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def Display_info(self):
            print(self.first_name)
            print(self.last_name)
            print(self.email)
            print(self.age)
        
    def Enroll(self):
        if self.is_rewards_member == True:
            print("user already a member.")
            return False
        else:
            self.gold_card_points += 200
            self.is_rewards_member = True
            return self
            
            #Have this method change the user's member status to True and set their gold card points to 200.
        #Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
        
    def Spend_points(self,amount):
        if self.gold_card_points < amount:
            print("We are sorry, but you do not have enough gold points accrued.")
        else:
            self.gold_card_points -= amount
            return self
        
        #have this method decrease the user's points by the amount specified.
        #Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
        
        
Phil = User("Phil", "Stevenson", "philshero@pigsrus.com", 126)
Steven = User("Steven", "Phillips", "stevepvillian@yaycats.com", 31)
Mary = User("Mary Jo Sassafrass", "Johnson-Decker-Ashton", "ohmary@blessyourheart.com", 6)
Jed = User("Jed", "Ham", "ilovesamiches@sandwichmeat.com", 88)
        
        
Phil.gold_card_points = Phil.gold_card_points + 147392
        
        
print(Steven.gold_card_points)
print(Steven.is_rewards_member)
User.Enroll(Steven)
print(Steven.gold_card_points)
print(Steven.is_rewards_member)
User.Spend_points(Steven,80)
print(Steven.gold_card_points)
print(Phil.gold_card_points)
User.Spend_points(Phil,50)
print(Phil.gold_card_points)
User.Display_info(Phil)
User.Display_info(Steven)
User.Display_info(Mary)
User.Display_info(Jed)
User.Enroll(Steven)
User.Spend_points(Mary,40)