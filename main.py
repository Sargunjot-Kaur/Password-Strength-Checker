password = input("Enter your password:")

from checker import check_length
from checker import check_complexity
print(check_length(password))
print(check_complexity(password))
