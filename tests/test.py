import mysql.connector
import unittest


class TestMovieDatabase(unittest.TestCase):
    def test_connection(self):
        db = mysql.connector.connect(
            host="mysql", user="root", password="password", database="movies_db"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movie")
        movies = cursor.fetchall()
        self.assertGreater(len(movies), 0, "No movies found")
        cursor.close()
        db.close()


if __name__ == "__main__":
    unittest.main()
