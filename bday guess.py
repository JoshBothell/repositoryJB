NUM128 = 128
NUM64 = 64
NUM32 = 32
NUM16 = 16
NUM8 = 8
NUM4 = 4
NUM2 = 2
NUM1 = 1

day_set1="set1: "
day_set2="set2: "
day_set4="set3: "
day_set8="set4: "
day_set16="set5: "

birthday = 0
birthmonth = 0
birthyear = 0
 
whats_left = 0

for i in range(1,32):
    bin_num=""
    input_num = i
    whats_left = input_num
    if(input_num >= NUM128):
        whats_left = input_num - NUM128
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if(whats_left >= NUM64):
        whats_left = whats_left - NUM64
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if whats_left >= NUM32:
        whats_left = whats_left - NUM32
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if whats_left >= NUM16:
        whats_left = whats_left - NUM16
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if whats_left >= NUM8:
        whats_left = whats_left - NUM8
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if whats_left >= NUM4:
        whats_left = whats_left - NUM4
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if whats_left >= NUM2:
        whats_left = whats_left - NUM2
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    if whats_left >= NUM1:
        whats_left = whats_left - NUM1
        bin_num = bin_num + "1"
    else:
        bin_num = bin_num + "0"

    xnum7 = bin_num[7]
    xnum6 = bin_num[6]
    xnum5 = bin_num[5]
    xnum4 = bin_num[4]
    xnum3 = bin_num[3]
    xnum2 = bin_num[2]
    xnum1 = bin_num[1]
    xnum0 = bin_num[0]
    x = str(i)
    if xnum3 == "1":
        day_set16 = day_set16 + x + " "
    if xnum4 == "1":
        day_set8 = day_set8 + x + " "
    if xnum5 == "1":
        day_set4 = day_set4 + x + " "
    if xnum6 == "1":
        day_set2 = day_set2 + x + " "
    if xnum7 == "1":
        day_set1 = day_set1 + x + " "

print(day_set1)
set_1 = input("Is your birth 'day' in this list? enter y/n   ")
if set_1 == "y":
    birthday += 1
print(day_set2)
set_2 = input("Is your birth 'day' in this list? enter y/n   ")
if set_2 == "y":
    birthday += 2
print(day_set4)
set_4 = input("Is your birth 'day' in this list? enter y/n   ")
if set_4 == "y":
    birthday += 4
print(day_set8)
set_8 = input("Is your birth 'day' in this list? enter y/n   ")
if set_8 == "y":
    birthday += 8
print(day_set16)
set_16 = input("Is your birth 'day' in this list? enter y/n   ")
if set_16 == "y":
    birthday += 16
print(day_set1)
month1 = input("Is your birth 'month' in this list? enter y/n   ")
if month1 == "y":
    birthmonth += 1
print(day_set2)
month2 = input("Is your birth 'month' in this list? enter y/n   ")
if month2 == "y":
    birthmonth += 2
print(day_set4)
month4 = input("Is your birth 'month' in this list? enter y/n   ")
if month4 == "y":
    birthmonth += 4
print(day_set8)
month8 = input("Is your birth 'month' in this list? enter y/n   ")
if month8 == "y":
    birthmonth += 8


print("Your birthday is: ",birthmonth, "/", birthday)
