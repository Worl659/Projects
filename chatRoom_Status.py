# done in 7 min
def chatroom_status(users):
    if len(users) == 0:
        return "no one online"
    elif len(users) == 1:
        return users[0] + " online"
    elif len(users) == 2:
        return users[0] + " and " + users[1] + " online"
    else:
        return (
            users[0] + ", " + users[1] + " and " + str(len(users) - 2) + " more online"
        )


print(chatroom_status(["john", "Becky", "stuart", "bill", "Harman", "jackson"]))
