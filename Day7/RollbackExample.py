import sqlite3

def insert_employees(conn, employees):
    """
    Insert multiple employees into the employee table.
    Rollback if any insertion fails.
    """
    sql = '''INSERT INTO employee(id, name, salary, department) VALUES (?, ?, ?, ?)'''
    try:
        cur = conn.cursor()
        for employee in employees:
            cur.execute(sql, employee)
        conn.commit()  # Commit the changes if all insertions are successful
        print("All employees inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback any changes if an error occurs
        print("Changes rolled back due to error.")

def main():
    database = "test.db"
    
    # Connect to SQLite database
    conn = sqlite3.connect(database)
    
    # Employee data (Note: The second insert intentionally contains an error for demonstration)
    employees = [
        (11, 'Bob', 50000, 'HR'),
        # This next line will fail because 'salary' expects an INTEGER, but is given a TEXT
        (12, 'Eve', 'not_a_number', 'Engineering'),
        (13, 'Charlie', 55000, 'Marketing')
    ]
    
    try:
        # Attempt to insert multiple employees
        insert_employees(conn, employees)
    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
