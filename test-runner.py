import unittest
import importlib
import sqlite3
import pandas as pd

class TestAssignmentFive(unittest.TestCase):
    def test_01(self):
        presidents_csv = asgmt.import_presidents_csv("presidents.csv")
        self.assertEqual(presidents_csv.shape, (53385, 7))
    def test_02(self):
        presidents_csv = asgmt.import_presidents_csv("presidents.csv")
        self.assertEqual(asgmt.return_presidents_csv_shape(presidents_csv, "rows"), 53385)
        self.assertEqual(asgmt.return_presidents_csv_shape(presidents_csv, "columns"), 7)
    def test_03(self):
        presidents_csv = asgmt.import_presidents_csv("presidents.csv")
        self.assertEqual(asgmt.return_presidents_csv_head_tail(presidents_csv, "head").shape, (5, 7))
        self.assertEqual(asgmt.return_presidents_csv_head_tail(presidents_csv, "tail").shape, (5, 7))
        self.assertEqual(min(asgmt.return_presidents_csv_head_tail(presidents_csv, "head").index), 0)
        self.assertEqual(max(asgmt.return_presidents_csv_head_tail(presidents_csv, "head").index), 4)
        self.assertEqual(min(asgmt.return_presidents_csv_head_tail(presidents_csv, "tail").index), 53380)
        self.assertEqual(max(asgmt.return_presidents_csv_head_tail(presidents_csv, "tail").index), 53384)
    def test_04(self):
        presidents_csv = asgmt.import_presidents_csv("presidents.csv")
        columns = ["id","number","district_id","candidate_id","votes","election_type_id","village_id"]
        for column in columns:
            self.assertTrue(column in asgmt.return_presidents_csv_columns(presidents_csv))
    def test_05(self):
        presidents_csv = asgmt.import_presidents_csv("presidents.csv")
        self.assertEqual(asgmt.summarize_presidents_csv(presidents_csv, "number"), (1, 2, 3))
        self.assertEqual(asgmt.summarize_presidents_csv(presidents_csv, "candidate_id"), (329, 330, 331))
        self.assertEqual(asgmt.summarize_presidents_csv(presidents_csv, "votes")[1], 3690466)
        self.assertEqual(asgmt.summarize_presidents_csv(presidents_csv, "votes")[2], 5586019)
        self.assertEqual(asgmt.summarize_presidents_csv(presidents_csv, "votes")[3], 4671021)
    def test_06(self):
        conn = asgmt.create_sqlite3_connection()
        self.assertIsInstance(conn, sqlite3.Connection)
    def test_07(self):
        conn = asgmt.create_sqlite3_connection()
        presidents = asgmt.import_presidents_from_sqlite_db(conn)
        self.assertEqual(presidents.shape, (53385, 7))
    def test_08(self):
        conn = asgmt.create_sqlite3_connection()
        election_types = asgmt.import_table_from_sqlite_db(conn, "election_types")
        self.assertEqual(election_types.shape, (5, 2))
        parties = asgmt.import_table_from_sqlite_db(conn, "parties")
        self.assertEqual(parties.shape, (35, 2))
        candidates = asgmt.import_table_from_sqlite_db(conn, "candidates")
        self.assertEqual(candidates.shape, (331, 4))
        presidents = asgmt.import_table_from_sqlite_db(conn, "presidents")
        self.assertEqual(presidents.shape, (53385, 7))
    def test_09(self):
        conn = asgmt.create_sqlite3_connection()
        self.assertTrue("id" in asgmt.extract_table_columns_from_sqlite_db(conn, "election_types"))
        self.assertTrue("election_type" in asgmt.extract_table_columns_from_sqlite_db(conn, "election_types"))
        self.assertTrue("id" in asgmt.extract_table_columns_from_sqlite_db(conn, "parties"))
        self.assertTrue("name" in asgmt.extract_table_columns_from_sqlite_db(conn, "parties"))
        self.assertTrue("id" in asgmt.extract_table_columns_from_sqlite_db(conn, "candidates"))
        self.assertTrue("name" in asgmt.extract_table_columns_from_sqlite_db(conn, "candidates"))
        self.assertTrue("party_id" in asgmt.extract_table_columns_from_sqlite_db(conn, "candidates"))
        self.assertTrue("election_type_id" in asgmt.extract_table_columns_from_sqlite_db(conn, "candidates"))
    def test_10(self):
        conn = asgmt.create_sqlite3_connection()
        table_shapes = asgmt.show_table_shapes_from_sqlite_db(conn)
        self.assertEqual(len(table_shapes), 10)
        self.assertTrue("election_types", table_shapes.keys())
        self.assertTrue("parties", table_shapes.keys())
        self.assertTrue("candidates", table_shapes.keys())
        self.assertTrue("presidents", table_shapes.keys())
        self.assertEqual(table_shapes["election_types"], (5, 2))
        self.assertEqual(table_shapes["parties"], (35, 2))
        self.assertEqual(table_shapes["candidates"], (331, 4))
        self.assertEqual(table_shapes["presidents"], (53385, 7))
        
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFive)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")