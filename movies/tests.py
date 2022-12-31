from app import initialize_app
import unittest

app = initialize_app()


class MovieTest(unittest.TestCase):

    # Check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status = response.status_code

        self.assertEqual(status, 200)


if __name__ == "__main__":

    unittest.main()