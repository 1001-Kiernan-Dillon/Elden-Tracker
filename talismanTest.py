import unittest
from unittest.mock import patch, MagicMock
from talismanfunctions import search_talismans, add_talisman_to_user, delete_talisman_from_user

class TestTalismanFunctions(unittest.TestCase):
    @patch('talismanfunctions.db_connect')
    def test_search_talismans(self, mock_db_connect):
        expected_output = ['Blessed Dew Talisman']
        input = 'Blessed Dew Talisman'
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = expected_output
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        output = search_talismans(input)

        self.assertEqual(output, expected_output)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM talismans WHERE name ILIKE %s;", (f'%{input}%',))

    @patch('talismanfunctions.db_connect')
    def test_add_talisman_to_user(self, mock_db_connect):
        input = (1, 1)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        add_talisman_to_user(*input)

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO user_talismans (user_id, talisman_id) VALUES (%s, %s);",
            input
        )

    @patch('talismanfunctions.db_connect')
    def test_delete_talisman_from_user(self, mock_db_connect):
        input = (1, 1)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        delete_talisman_from_user(*input)

        mock_cursor.execute.assert_called_once_with("DELETE FROM user_talismans WHERE user_id = %s AND talisman_id = %s;", input)

if __name__ == '__main__':
    unittest.main()
