import unittest
from unittest.mock import patch, MagicMock
from bossfunctions import search_bosses, add_boss_to_user, delete_boss_from_user

class TestBossFunctions(unittest.TestCase):
    @patch('bossfunctions.db_connect')
    def test_search_bosses(self, mock_db_connect):
        # Arrange
        expected_output = [('Commander Niall')]  # Change this line
        input = "Commander Niall"
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = expected_output
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        output = search_bosses(input)

        # Assert
        self.assertEqual(output, expected_output)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM bosses WHERE name ILIKE %s;", (f'%{input}%',))

    @patch('bossfunctions.db_connect')
    def test_add_boss_to_user(self, mock_db_connect):
        input = (1, 77)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        add_boss_to_user(*input)

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO user_bosses (user_id, boss_id) VALUES (%s, %s);",
            input
        )

    @patch('bossfunctions.db_connect')
    def test_delete_boss_from_user(self, mock_db_connect):
        input = (1, 77)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        delete_boss_from_user(*input)

        mock_cursor.execute.assert_called_once_with("DELETE FROM user_bosses WHERE user_id = %s AND boss_id = %s;", input)

if __name__ == '__main__':
    unittest.main()
