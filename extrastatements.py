start_date="2024-01-01"
end_date="2024-12-31"
if start_date>end_date:
    print("valid period")
elif end_date>start_date:
    print("invalid peroid")
else:
    print("one day period")


str1=(len("Enter string 1"))
str2=(len("Enter string2"))

if str1>str2:
    print(f"{str1} is larger")
elif str2>str1:
    print(f"{str2} is larger")
else:
    print("both are equal")

valid_ids=[101,102,103]
user_id=105

if valid_ids==user_id:
    print("Access granted")
else:
    print("Access denied")

value="mohamed"

if value=="strings":
    print("strings detected")
elif value==int:
    print("integer detected")
else:
    print("unkown type")
