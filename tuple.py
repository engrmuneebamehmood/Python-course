
# it is represented by ()
'''
weekdays=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(weekdays)
print(type(weekdays))         #checking type
print(weekdays[4])            #displaying weekday at index 4
print(weekdays[1:5])          #slicing
print(len(weekdays))          #checking length of tuple

'''
'''
days=tuple(('monday', 'tuesday'))
print(days)
print(type(days))

days_list=list(days)
days_list.append("friday")
print(days_list)
print(type(days_list))

days=tuple(days_list)
print(days)
print(type(days))

'''
#we can not do changes in tuple
#so we can chnage tuple to list and make chnages

weekdays=("Monday","Monday","Wednesday","Thursday","Friday","Saturday","Sunday")
(day1,day2,day3,day4,day5,day6,day7)=weekdays#unpacking

print(day1)

print(weekdays.count('Monday'))