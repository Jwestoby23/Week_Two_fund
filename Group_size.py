amount_people = input("How many students do you have to be placed in groups?")
amount_people = int(amount_people)
group_size = input("How many should be in each group")
group_size = int(group_size)

leftover = amount_people % group_size
Groups = amount_people // group_size
print("You will have",Groups, "Lab groups and will have", leftover)