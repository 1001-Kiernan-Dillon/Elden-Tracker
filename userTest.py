import unittest
from unittest.mock import patch, MagicMock
from psycopg2 import sql
from userfunctions import get_user_id, get_password, create_user, delete_user

class TestUserFunctions(unittest.TestCase):
    @patch('userfunctions.db_connect')
    def test_get_user_id(self, mock_db_connect):
        # Arrange
        expected_output = 1
        input = 'test_user'
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [expected_output]
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        output = get_user_id(input)

        # Assert
        self.assertEqual(output, expected_output)
        mock_cursor.execute.assert_called_once_with("SELECT user_id FROM users WHERE username = %s;", (input,))

    @patch('userfunctions.db_connect')
    def test_get_password(self, mock_db_connect):
        # Arrange
        expected_output = 'test_password'
        input = 'test_user'
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [expected_output]
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        output = get_password(input)

        # Assert
        self.assertEqual(output, expected_output)
        mock_cursor.execute.assert_called_once_with("SELECT password FROM users WHERE username = %s;", (input,))

    @patch('userfunctions.db_connect')
    def test_create_user(self, mock_db_connect):
        # Arrange
        expected_output = 1
        input = ('test_user', 'test_email', 'test_password')
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [expected_output]
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        create_user(*input)

        # Assert
        mock_cursor.execute.assert_called_once_with(
            sql.SQL("INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING user_id;"),
            input
        )

    @patch('userfunctions.db_connect')
    def test_delete_user(self, mock_db_connect):
        # Arrange
        input = 1
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        delete_user(input)

        # Assert
        mock_cursor.execute.assert_called_once_with("DELETE FROM users WHERE user_id = %s;", (input,))

if __name__ == '__main__':
    unittest.main()
