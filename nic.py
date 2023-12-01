import datetime

def validate(nic : str) -> bool:
    nic_length = len(nic)
    if nic_length != 12 :
        return False
    else:
        is_digit = nic.isdigit()
        return is_digit
    
# Fuction for identifying the born year
def identify_born_year(nic : str) -> int:
    year = nic[0:4]
    return int(year)
# check gender
def checker_gender(nic : str) -> str:
    gender = int(nic[4:7])
    if gender > 500:
        return "Female"
    else:
        return "Male"

# Get born Date
def get_born_date(nic : str) -> datetime.date :
    born_day = int(nic[4:7])
    if born_day > 500:
        born_day -= 500
    year = identify_born_year(nic)
    jan_first = datetime.date(year, 1, 1)
    born_date = jan_first + datetime.timedelta(days=born_day -1)
    return born_date

# Get the NIC number as a user input
nic_number = input("Enter your NIC number: ")

# validate input
valid_nic = validate(nic_number)
if not valid_nic:
    print("Invalid NIC number! Plase check your NIC number again.")
    exit(0)

# identift the born year
year = identify_born_year(nic_number)

# gender
gender = checker_gender(nic_number)

# Calculate the exact born date
born_date = get_born_date(nic = nic_number)
day = born_date.strftime("%A")
# print the output
print(f" birthday : {born_date}")
print(f'born day is {day}')
print(f'Gender is {gender}')
