from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QInputDialog
from weaponfunctions import search_weapons, add_weapon_to_user, delete_weapon_from_user
from itemfunctions import search_items, add_item_to_user, delete_item_from_user
from talismanfunctions import search_talismans, add_talisman_to_user, delete_talisman_from_user
from bossfunctions import search_bosses, add_boss_to_user, delete_boss_from_user
from userfunctions import get_user_id, delete_user


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, username):
        super(Ui_MainWindow, self).__init__()
        self.username = username

    def setupUi(self, MainWindow):  # add MainWindow as an argument
        uic.loadUi(r'C:\Program_Scripts\Programs\EldenTracker\mainmenu.ui', MainWindow)  # use MainWindow here

        # Add a QLabel to show the username
        self.usernameLabel = QtWidgets.QLabel(MainWindow.centralwidget)  # use MainWindow.centralwidget here
        self.usernameLabel.setText("Logged in as: " + self.username)
        MainWindow.verticalLayout.addWidget(self.usernameLabel)  # use MainWindow.verticalLayout here

        # Add a QPushButton for deleting the user
        self.deleteUserButton = QtWidgets.QPushButton(MainWindow.centralwidget)
        self.deleteUserButton.setText("Delete User")
        MainWindow.verticalLayout.addWidget(self.deleteUserButton)
        self.deleteUserButton.clicked.connect(self.delete_user) # connect the button to the delete_user function
        
        # Find the search bar
        self.search = MainWindow.findChild(QtWidgets.QLineEdit, 'search')  # replace 'search' with the actual object name of your search bar

        # Connect the buttons to their respective functions
        MainWindow.searchButton.clicked.connect(self.find)  # use MainWindow.searchButton here
        MainWindow.weapon.clicked.connect(self.add_or_delete_weapon)  # use MainWindow.weapon here
        MainWindow.item.clicked.connect(self.add_or_delete_item)  # use MainWindow.item here
        MainWindow.talisman.clicked.connect(self.add_or_delete_talisman)  # use MainWindow.talisman here
        MainWindow.boss.clicked.connect(self.add_or_delete_boss)  # use MainWindow.boss here

    def find(self):
        # Implement your search function here
        search_text = self.search.text()
        print(f'Searching for {search_text}...')
        results = self.search_all(search_text)

        # Create a QListWidget to display the results
        self.listWidget = QtWidgets.QListWidget()

        # Add the results to the QListWidget
        for result in results:
            item = QtWidgets.QListWidgetItem(str(result))
            self.listWidget.addItem(item)

        # Create a QDialog to display the QListWidget
        self.dialog = QtWidgets.QDialog()
        dialog_layout = QtWidgets.QVBoxLayout(self.dialog)
        dialog_layout.addWidget(self.listWidget)
        self.dialog.show()
    
    def search_all(self, search_text):
        """Search for weapons, items, talismans, and bosses by name."""
        # Call all the search functions with the search text
        weapons = search_weapons(search_text)[:3]  # get the first 3 results
        items = search_items(search_text)[:3]  # get the first 3 results
        talismans = search_talismans(search_text)[:3]  # get the first 3 results
        bosses = search_bosses(search_text)[:3]  # get the first 3 results

        # Combine all the results into one list
        results = weapons + items + talismans + bosses

        return results

    def add_or_delete_weapon(self):
        # Prompt the user for the weapon ID
        weapon_id, okPressed = QInputDialog.getInt(self, "Get integer","Weapon ID:", 0, 0, 100, 1)
        if okPressed:
            # Ask the user if they want to add or delete the weapon
            action, okPressed = QInputDialog.getItem(self, "Get item","Action:", ["Add", "Delete"], 0, False)
            if okPressed:
                user_id = get_user_id(self.username)  # replace with actual function to get user id
                if action == "Add":
                    add_weapon_to_user(user_id, weapon_id)
                elif action == "Delete":
                    delete_weapon_from_user(user_id, weapon_id)

    def add_or_delete_item(self):
        # Prompt the user for the item ID
        item_id, okPressed = QInputDialog.getInt(self, "Get integer","Item ID:", 0, 0, 100, 1)
        if okPressed:
            # Ask the user if they want to add or delete the item
            action, okPressed = QInputDialog.getItem(self, "Get item","Action:", ["Add", "Delete"], 0, False)
            if okPressed:
                user_id = get_user_id(self.username)  # replace with actual function to get user id
                if action == "Add":
                    add_item_to_user(user_id, item_id)
                elif action == "Delete":
                    delete_item_from_user(user_id, item_id)

    def add_or_delete_talisman(self):
        # Prompt the user for the talisman ID
        talisman_id, okPressed = QInputDialog.getInt(self, "Get integer","Talisman ID:", 0, 0, 100, 1)
        if okPressed:
            # Ask the user if they want to add or delete the talisman
            action, okPressed = QInputDialog.getItem(self, "Get talisman","Action:", ["Add", "Delete"], 0, False)
            if okPressed:
                user_id = get_user_id(self.username)  # replace with actual function to get user id
                if action == "Add":
                    add_talisman_to_user(user_id, talisman_id)
                elif action == "Delete":
                    delete_talisman_from_user(user_id, talisman_id)
    
    def add_or_delete_boss(self):
        # Prompt the user for the boss ID
        boss_id, okPressed = QInputDialog.getInt(self, "Get integer","Boss ID:", 0, 0, 100, 1)
        if okPressed:
            # Ask the user if they want to add or delete the boss
            action, okPressed = QInputDialog.getItem(self, "Get boss","Action:", ["Add", "Delete"], 0, False)
            if okPressed:
                user_id = get_user_id(self.username)  # replace with actual function to get user id
                if action == "Add":
                    add_boss_to_user(user_id, boss_id)
                elif action == "Delete":
                    delete_boss_from_user(user_id, boss_id)

    def delete_user(self):
        # Implement your user deletion logic here
        print(f'Deleting user {self.username}...')
        delete_user(get_user_id(self.username))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow('username')  # replace 'username' with the actual username
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
