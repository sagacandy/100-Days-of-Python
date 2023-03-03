import datetime
now = datetime.datetime.now()
print("The current date and time is: ", now)

datetimeformat = now.strftime("%H")
check = int(datetimeformat)
if check <= 12:
    print("Good moring")
elif check >= 12:
    print("Print Good afternoon")
else:
    print("Print good evening")
