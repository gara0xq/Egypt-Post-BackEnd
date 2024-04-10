import psycopg2
import pandas as pd


conn = psycopg2.connect(
    host="ep-delicate-sunset-a23bbout.eu-central-1.aws.neon.fl0.io",
    dbname="EgyptPostDatabase",
    user="fl0user",
    password="EARdkfSg1I3X",
    port="5432"
)

# goverment
# sector
# sectorID
# office
# type
# num

data = pd.read_excel("null.xlsx")

x = 0

for j in data["sector"]:
    sql = "SELECT * FROM TechnicalSupport_officesmodel;"

    ss = (f'{data["sector"][x]}', f'{data["sectorID"][x]}', f'{data["office"][x]}', f'{data["type"][x]}', f'{data["num"][x]}')
    # print(f'{data["sector"][x]}, {data["sectorID"][x]}, {data["office"][x]}, {data["type"][x]}, {data["num"][x]}')
    x += 1

cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
# cur.execute('''SET search_path TO your_schema_name''')
table_records = cur.fetchall()
table_names = [record[0] for record in table_records]

# Print the table names
for table_name in table_names:
    print(table_name)

cur.close()

conn.close()


# sector, sectorCode, office, officeType, numOfWindows


# # Create a cursor object
# cur = conn.cursor()

# # Execute a SQL query to fetch all table names
# cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

# # Fetch all the rows
# table_records = cur.fetchall()

# # Extract table names from the fetched records
# table_names = [record[0] for record in table_records]

# # Print the table names
# for table_name in table_names:
#     print(table_name)

# # Close the cursor and connection
# cur.close()
# conn.close()