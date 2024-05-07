import unittest
from unittest.mock import patch, MagicMock
from itemfunctions import search_items, add_item_to_user, delete_item_from_user

class TestItemFunctions(unittest.TestCase):
    @patch('itemfunctions.db_connect')
    def test_search_items(self, mock_db_connect):
        expected_output = ["Trina's Lily"]
        input = "Trina's Lily"
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = expected_output
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        output = search_items(input)

        self.assertEqual(output, expected_output)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM items WHERE name ILIKE %s;", (f'%{input}%',))

    @patch('itemfunctions.db_connect')
    def test_add_item_to_user(self, mock_db_connect):
        input = (1, 1)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        add_item_to_user(*input)

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO user_items (user_id, item_id) VALUES (%s, %s);",
            input
        )

    @patch('itemfunctions.db_connect')
    def test_delete_item_from_user(self, mock_db_connect):
        input = (1, 1)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        delete_item_from_user(*input)

        mock_cursor.execute.assert_called_once_with("DELETE FROM user_items WHERE user_id = %s AND item_id = %s;", input)

if __name__ == '__main__':
    unittest.main()
