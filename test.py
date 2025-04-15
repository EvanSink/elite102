import unittest
from initialize_db import initialize_database


class TestNumbersOperations(unittest.TestCase):
    def test_initialize_database(self):
        # Test if the database is initialized correctly
        try:
            initialize_database()
            self.assertTrue(True)  # If no exception is raised, the test passes
        except Exception as e:
            self.fail(f"initialize_database raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()