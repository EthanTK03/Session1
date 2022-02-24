pay = 13.50
print("You are paid an hourly wage of $13.50 ") 
# Idea for if else :  
# "Do you know how many hours you worked this week?"
# if yes, ask how many hours and subsequently the week's pay
# skip the rest of the code (keep it in else)
# if no, go through the rest of the code

mon = int(input("How many hours did you work Monday? "))
print("You worked " + str(mon) + str(" hours for a total today of $") + str(mon*pay))

tues = int(input("How many hours did you work Tuesday? "))
print("You worked " + str(tues) + str(" hours for a total today of $") + str(tues*pay))

wed = int(input("How many hours did you work Wednesday? "))
print("You worked " + str(wed) + str(" hours for a total today of $") + str(wed*pay))

thur = int(input("How many hours did you work Thursday? "))
print("You worked " + str(thur) + str(" hours for a total today of $") + str(thur*pay))

fri = int(input("How many hours did you work Friday? "))
print("You worked " + str(fri) + str(" hours for a total today of $") + str(fri*pay))

sat = int(input("How many hours did you work Saturday? "))
print("You worked " + str(sat) + str(" hours for a total today of $") + str(sat*pay))

sun = int(input("How many hours did you work Sunday? "))
print("You worked " + str(sun) + str(" hours for a total today of $") + str(sun*pay))

week = (mon+tues+wed+thur+fri+sat+sun)
print("You worked a total of " + str(week) + str(" hours this week, for $") +str(week*pay))
