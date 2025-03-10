import sqlite3

# 1. Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('pract.db')  # Replace 'accounts.db' with your database name
cursor = conn.cursor()

# 2. Create the table (if it doesn't exist already)
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    account_number INTEGER PRIMARY KEY,
    name TEXT,
    pin INTEGER,
    balance REAL
)
''')
conn.commit()

# 3. Define the account dictionary
account = {
    100: ["Deepthi", 1234, 0],
    101: ["Eva", 2345, 100000],
    102: ["Raghavendra", 3456, 110000],
    103: ["Sthuthi", 4567, 85000],
    104: ["Sujay", 5678, 50500]
}

# 4. Insert data from the account dictionary into the SQLite database
for acc_num, details in account.items():
    name, pin, balance = details
    query = '''
    INSERT OR REPLACE INTO accounts (account_number, name, pin, balance)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (acc_num, name, pin, balance))

# 5. Commit the changes
conn.commit()

# 6. Query the database to check if the data is inserted
cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()

# Print the data from the table
for row in rows:
    print(row)

# Close the connection
conn.close()