import sqlite3 as sql
import unittest
class testing_employeename(unittest.TestCase):
    def setUp(self):
        self.Name1="dhanush"

        self.Code="1"
        self.connection=sql.connect("Employee.db")
    def tearDown(self):
        self.Name1=" "

        self.Code=" "
        self.connection.close()
    def test_verify_employeename(self):
        result=self.connection.execute("select NAME from EMPLOYEEDATABASE where EMPCODE="+self.Code)
        for i in result:
            fetchemployeename=i[0]
        self.assertEqual(self.Name1,fetchemployeename)

if __name__=="__main__":
    unittest.main()
