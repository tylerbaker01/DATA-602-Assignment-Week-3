# 1) What does the code display? How to debug?
numbers = [1,2,3,4,5]
print(numbers[1:-5])
# Answer: The code displays [].
# Debug
print(numbers[0:5])

# 2) Design a program that asks the user to enter a store's sales for each day of the week.
#    The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display result.
monday_sales = float(input('Enter how much was made on Monday: '))
tuesday_sales = float(input('Enter how much was made on Tuesday: '))
wednesday_sales = float(input('Enter how much was made on Wednesday: '))
thursday_sales = float(input('Enter how much was made on Thursday: '))
friday_sales = float(input('Enter how much was made on Friday: '))
saturday_sales = float(input('Enter how much was made on Saturday: '))
sunday_sales = float(input('Enter how much was made on Sunday: '))

daily_sales = [monday_sales, tuesday_sales, wednesday_sales, thursday_sales, friday_sales, saturday_sales, sunday_sales]
weekly_total = 0
for i in daily_sales:
    weekly_total = weekly_total + i
print(weekly_total)

# 3) Create a list with at least 5 places you'd like to travel to. Make sure the list isn't in alphebetical order.
#    Print your list in original order. Use sort and reverse.
travel_goals = ['japan', 'united kingdom', 'california', 'bolivia', 'thailand']
print(travel_goals)
travel_goals.sort()
print(travel_goals)
travel_goals.sort(reverse=True)
print(travel_goals)


# 4)  Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.
course_info = {'601':201, '602':202, '603':400, '604':100}
course_info_one = {'601':"Bob", "602":"Larry", "603":"Michelle", "604":"Lisa"}
course_info_final = {'601':[201, "Bob", "8PM"], "602":[202, "Larry", "4PM"], "603":[400, "Michelle", "2PM"], "604":[100, "Lisa", "11AM"]}

# 5) Write a program that keeps names and email addresses in a dictionary as
#key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

email_directory = {"Fred":"fredl@mail.com", "Lisa":"lisam@mail.com", "Tom":"tomj@mail.com"}
print(email_directory["Tom"])
email_directory["Jane"]= "janeo@mail.com"
email_directory["Fred"]= "fredh@mail.com"
del(email_directory["Lisa"])
print(email_directory)