dateString = input("Please Enter The Date String In DD/MM/YYYY Format : ")
dateList = dateString.split('/')
for i in range(0, len(dateList)):
    dateList[i] = int(dateList[i])
date = dateList[0]
month = dateList[1]
year = dateList[2]
numberAndRomanNumber = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL')
                        , (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
romanDate = ''
romanMonth = ''
romanYear = ''
while date > 0:
    for i, r in numberAndRomanNumber:
        while date >= i:
            romanDate += r
            date -= i
while month > 0:
    for i, r in numberAndRomanNumber:
        while month >= i:
            romanMonth += r
            month -= i
while year > 0:
    for i, r in numberAndRomanNumber:
        while year >= i:
            romanYear += r
            year -= i
romanDateString = romanDate + "/" + romanMonth + "/" + romanYear
print("The Following Date In Roman Numerals Is:", romanDateString)