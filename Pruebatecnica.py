from datetime import datetime, date, timedelta
from dateutil.parser import parse
import statistics

Names = ['James', 'Mohammed', 'Sofia', 'George', 'Nicola', 'Lena']
Class = ['4PW', '4A', '4A', '4PW', '4PW', '4G']
DateOfBirth = ['30th november', '5/2/12', '1st december 2011', '3/8/12', '5/4/12', '24-jan-12']
TestResult = [80.5, 83, 67, 76.5, 78, 92]

formatted_dates = []
ages = []
for dob in DateOfBirth:
    try:
        dob_obj = datetime.strptime(dob, '%d %B %Y').date()
    except ValueError:
        try:
            # Handle 1st, 2nd, 3rd, 4th, etc. prefixes
            dob_obj = parse(dob).date()
        except ValueError:
            formatted_dates.append(None)
            continue

    formatted_dates.append(dob_obj.strftime('%Y-%m-%d'))
    age = (date.today() - dob_obj) // timedelta(days=365.2425)
    ages.append(age)

mean_test_result = statistics.mean(TestResult)
median_test_result = statistics.median(TestResult)
mean_age = statistics.mean(ages)
median_age = statistics.median(ages)

print(f"These are the fixed data:")
print(f"================================================")
for name, cls, dob, test_result in zip(Names, Class, formatted_dates, TestResult):
    print(f"{name}:{cls}:{dob}:{test_result}")

print(f"================================================")
print(f"The result after the evaluation is the followin:")
print(f"================================================")
print(f"Mean test result: {mean_test_result}")
print(f"================================================")
print(f"Median test result: {median_test_result}")
print(f"================================================")
print(f"Mean age: {mean_age}")
print(f"================================================")
print(f"Median age: {median_age}")
