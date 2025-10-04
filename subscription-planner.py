class Account:
    def __init__(self, name, sub_list):
        self.username = name
        self.sublist = sub_list
        print("Welcome to the Subcription manager application! We allow you to organise, edit and\n enquire your subscriptions in the easiest way possible!")
        print(f"\nAccount '{self.name}' created. Kindly enter your current subscription list")
        num_of_subs = input(f"How many subs would you like to add?, {self.name}\n")
        