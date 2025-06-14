import pandas as pd
import pyodbc

# 1. Read the CSV
df = pd.read_csv("./Sample - Superstore.csv", encoding="latin1")

# 2. Clean column names
df.columns = [col.strip() for col in df.columns]

# 3. Connect to SQL Server
conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=ATHANG\SQLEXPRESS;"
    r"DATABASE=RetailBI;"
    r"Trusted_Connection=yes;"
)
cursor = conn.cursor()

# 4. Insert each row
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO Orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        int(row["Row ID"]),
        row["Order ID"],
        row["Order Date"],
        row["Ship Date"],
        row["Ship Mode"],
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"],
        row["Country"],
        row["City"],
        row["State"],
        int(row["Postal Code"]) if pd.notna(row["Postal Code"]) else None,
        row["Region"],
        row["Product ID"],
        row["Category"],
        row["Sub-Category"],
        row["Product Name"],
        row["Sales"],
        row["Quantity"],
        row["Discount"],
        row["Profit"],
    )

# 5. Save and close
conn.commit()
conn.close()

print("orders.csv successfully loaded into SQL Server.")
