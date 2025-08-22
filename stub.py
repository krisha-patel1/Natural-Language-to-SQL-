import sys
import psycopg2
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Usage: python stub.py \"SELECT * FROM your_table;\"")
        return
    query = sys.argv[1]

    user = sys.stdin.readline().strip()
    password = sys.stdin.readline().strip()

    conn = psycopg2.connect(
        host="postgres.cs.rutgers.edu",
        database="amm926",
        user=user,
        password=password
    )

    df = pd.read_sql_query(query, conn)
    print(df)
    conn.close()

if __name__ == "__main__":
    main()
