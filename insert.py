import pandas as pd
import sqlite3

df1 = pd.read_excel('123 Updated.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel('123 Updated.xlsx', sheet_name='Sheet2')
df3 = pd.read_excel('123 Updated.xlsx', sheet_name='Sheet3')


# for i in df1:
#     print(i)
# print("=========")
# for i in df2:
#     print(i)
# print("=========")
# for i in df3:
#     print(i)
# print("=========")


# C1
# C2
# C3
# C4
# C5
# C6
# C7
# C8
# C9
# C10
# C11
# C12
# C13
# C14
# C15
# C16
# =========
# C2
# C3
# =========
# C3
# C4
# C5
# C14
# =========


conn = sqlite3.connect('EgyptPost/db.sqlite3')
cursor = conn.cursor()

# ('Authin_user',)
# ('Files_messagemodel',)
# ('TechnicalSupport_devicesmodel',)
# ('TechnicalSupport_devicesmodulemodel',)
# ('TechnicalSupport_officesmodel',)
# ('TechnicalSupport_sectormodel',)

# governorate
# sectorCode
# sector





# model
# date
# status
# ram
# deviceType
# serial

# governorate
# sector
# office
# officeType
# model
# serial
# date
# status
# ram
# deviceType
# sectorCode
# numOfWindows
# ip

# sector
# sectorCode
# office
# officeType
# numOfWindows

x = 0
for i in df1["C13"]:    
    sql_insert1 = "INSERT INTO TechnicalSupport_devicesmodel (governorate, sector, office, officeType, model, serial, date, status, ram, deviceType, sectorCode, numOfWindows, ip) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    data1 = (f'{df1["C2"][x]}', f'{df1["C3"][x]}', f'{df1["C4"][x]}', f'{df1["C5"][x]}', f'{df1["C6"][x]}', f'{df1["C8"][x]}', f'{df1["C9"][x]}', f'{df1["C10"][x]}', f'{df1["C11"][x]}', f'{df1["C12"][x]}', f'{df1["C14"][x]}', 0 ,f'{df1["C16"][x]}')
    cursor.execute(sql_insert1, data1)
    conn.commit()
    x += 1

x = 0

for i in df2["C3"]:
    sql_insert2 = "INSERT INTO TechnicalSupport_sectormodel (governorate, sectorCode, sector) VALUES (?, ?, ?)"
    data2 = (f'{df2["C2"][x]}', f'{df2["C4"][x]}', f'{df2["C3"][x]}')
    cursor.execute(sql_insert2, data2)
    conn.commit()

for i in df3["C14"]:
    sql_insert3 = "INSERT INTO TechnicalSupport_officesmodel (sector, sectorCode, office, officeType, numOfWindows) VALUES (?, ?, ?, ?, ?)"
    data3 = (f'{df3["C3"][x]}', f'{df3["C14"][x]}', f'{df3["C4"][x]}', f'{df3["C5"][x]}', 0)
    cursor.execute(sql_insert3, data3)
    conn.commit()


cursor.close()
conn.close()