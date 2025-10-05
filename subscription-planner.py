class Account:
    def __init__(self, name):
        self.username = name
        sub_list = []
        print("Welcome to the Subcription manager application! We allow you to organise, edit and\n enquire your subscriptions in the easiest way possible!")
        print(f"\nAccount '{self.username}' created. Kindly enter your current subscription list")
        try: 
            num_of_subs = int(input(f"How many subs would you like to add?, {self.username}\n"))
            for i, num in enumerate(range(0, num_of_subs)):
                sinput = input(f"Enter Subscription-{i+1} name: ")
                sub_list.append(sinput)
            print(sub_list)
                
        except:
            print("You have entered an invalid. Please try again!")
    def get_username():
        super.__init__()
        
sample_account = Account("Ishaan Lohani")