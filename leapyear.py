def isLeapyear(year):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False


# Main Program
year = int(input("Enter a year : "))
if isLeapyear(year):
  print("{} is a Leap Year.".format(year))
else:
  print("{} is not a Leap Year.".format(year))
