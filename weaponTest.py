import unittest
from unittest.mock import patch, MagicMock
from weaponfunctions import search_weapons, add_weapon_to_user, delete_weapon_from_user

class TestWeaponFunctions(unittest.TestCase):
    @patch('weaponfunctions.db_connect')
    def test_search_weapons(self, mock_db_connect):
        # Arrange
        expected_output = [('Hand Axe', 'Axe')]
        input = 'Hand Axe'
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = expected_output
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        output = search_weapons(input)

        # Assert
        self.assertEqual(output, expected_output)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM weapons WHERE name ILIKE %s;", (f'%{input}%',))

    @patch('weaponfunctions.db_connect')
    def test_add_weapon_to_user(self, mock_db_connect):
        # Arrange
        input = (1, 1)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        add_weapon_to_user(*input)

        # Assert
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO user_weapons (user_id, weapon_id) VALUES (%s, %s);",
            input
        )

    @patch('weaponfunctions.db_connect')
    def test_delete_weapon_from_user(self, mock_db_connect):
        # Arrange
        input = (1, 1)
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value = mock_cursor

        # Act
        delete_weapon_from_user(*input)

        # Assert
        mock_cursor.execute.assert_called_once_with("DELETE FROM user_weapons WHERE user_id = %s AND weapon_id = %s;", input)

if __name__ == '__main__':
    unittest.main()
