import sqlite3
from prettytable import PrettyTable
connection = sqlite3.connect("Employee.db")
tablelist = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='EMPLOYEEDATABASE'").fetchall()
if tablelist != []:
    print("table created already...")
else:
    connection.execute('''CREATE TABLE EMPLOYEEDATABASE(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        EMPCODE INTEGER,
                        NAME TEXT,
                        PHONENO INTEGER,
                        EMAIL TEXT,
                        DESIGNATION TEXT,
                        SALARY INTEGER,
                        COMPANYNAME TEXT
                        );''')
    print("table created successfully")
while True:
    print("select an option from the menu ")
    print("1. Add the employees ")
    print("2. view all employees")
    print("3. search an employee using employee name")
    print("4. update an employee details using employee code")
    print("5. delete an employee using employee code")
    print("6. display all employee whose salary is greater than 50000")
    print("7. diaplay the count of total number of employees in the company")
    print("8. diaplay all the employees i alphabetical order, within the specific salary range is 25000 to 60000")
    print("9. display all employees whose salary is less than the average salary of the employee")
    print("10. EXIT")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        getempcode = input("Enter the empcode: ")
        getname = input("Enter the name: ")
        getphoneno = input("Enter the phoneno: ")
        getemail = input("Enter the email: ")
        getdesignation = input("Enter the designation: ")
        getsalary = input("Enter the salary: ")
        getcompanyname = input("Enter the companyname: ")

        connection.execute("INSERT INTO EMPLOYEEDATABASE(Empcode,Name,Phoneno,Email,Designation,Salary,Companyname)\
                                    VALUES(" + getempcode + ",'" + getname + "'," + getphoneno + ",'" + getemail + "','" + getdesignation + "'," + getsalary + ",'" + getcompanyname + "')")
        connection.commit()
        print("added successfully")

    elif choice == 2:
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE")
        table = PrettyTable(["ID","EMPCODE","NAME","PHONENO","EMAIL","DESIGNATION","SALARY","COMPANYNAME"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
        print(table)
    elif choice == 3:
        getName = input("Enter the employee name to be search: ")
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE WHERE name LIKE '%"+getName+"%'")
        table = PrettyTable(["ID","EMPCODE", "NAME", "PHONENO", "EMAIL", "DESIGNATION", "SALARY", "COMPANYNAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
    elif choice == 4:
        getempcode = input("Enter the empcode: ")

        getname = input("Enter the name: ")
        getphoneno = input("Enter the phoneno: ")
        getemail = input("Enter the email: ")
        getdesignation = input("Enter the designation: ")
        getsalary = input("Enter the salary: ")
        getcompanyname = input("Enter the companyname: ")
        result = connection.execute("UPDATE EMPLOYEEDATABASE SET Name='"+getname+"',Phoneno="+getphoneno+",Email='"+getemail+"',Designation='"+getdesignation+"',Salary="+getsalary+",Companyname='"+getcompanyname+"' WHERE Empcode="+getempcode+"")
        connection.commit()
        print("employee data updated successfully")
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE WHERE Empcode="+getempcode+"")
        print("Data Updated successfully")
        table = PrettyTable(["ID","EMPCODE", "NAME", "PHONENO", "EMAIL", "DESIGNATION", "SALARY", "COMPANYNAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
    elif choice == 5:
        getempcode = input("Enter the empcode: ")
        connection.execute("DELETE FROM EMPLOYEEDATABASE WHERE Empcode=" + getempcode)
        connection.commit()
        print("employee data deleted successfully")
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE")
        print("Employee data updated successfully")

    elif choice == 6:
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE WHERE Salary > 50000")
        table = PrettyTable(["ID","EMPCODE", "NAME", "PHONENO", "EMAIL", "DESIGNATION", "SALARY", "COMPANYNAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
    elif choice == 7:
        result = connection.execute("SELECT COUNT(*) AS NAME FROM EMPLOYEEDATABASE")
        for i in result:
            print("Total Employees count is: ", i[0])
    elif choice == 8:
        lower_salary = input("Enter the lower salary: ")
        higher_salary = input("Enter the higher salary: ")
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE WHERE SALARY BETWEEN "+lower_salary+" AND "+higher_salary+" ORDER BY SALARY ASC")
        table = PrettyTable(["ID","EMPCODE", "NAME", "PHONENO", "EMAIL", "DESIGNATION", "SALARY", "COMPANYNAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
    elif choice == 9:
        result = connection.execute("SELECT * FROM EMPLOYEEDATABASE WHERE SALARY<(SELECT avg(SALARY) as SALARY FROM EMPLOYEEDATABASE)")
        table = PrettyTable(["ID","EMPCODE", "NAME", "PHONENO", "EMAIL", "DESIGNATION", "SALARY", "COMPANYNAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
    elif choice == 10:
        connection.close()
        break
    else:
        print("INVALID CHOICE")

















