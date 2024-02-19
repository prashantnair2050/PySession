import sqlite3

def insert_employee(conn, employee_data):
    """
    Insert a new employee into the employee table using a prepared statement
    """
    sql = '''INSERT INTO employee(id, name, salary, department) VALUES (?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, employee_data)
    conn.commit()

def main():
    database = "test.db"
    
    # Connect to SQLite database
    conn = sqlite3.connect(database)
    
    # New employee data
    new_employee = (10, 'Alice', 75000, 'Engineering')
    
    try:
        # Insert a new employee
        insert_employee(conn, new_employee)
        print("Employee inserted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
