
from PyQt6.QtWidgets import QPushButton, QSizePolicy

from Grand_Restaurant_V2 import AppWindow

from config_Grand_Restau_menus import MENUS

H_BTN_POLICY = QSizePolicy.Policy.Preferred
V_BTN_POLICY = QSizePolicy.Policy.Expanding


class MenuWindow(AppWindow):
    def __init__(self):
        super().__init__()

        self.menu = None
        self.step = -1
        self.items = list()

    def load_items(self):
        super().load_items()
        self.load_menus()
        self.menu_details.hide()

    def load_menus(self):
        for menu in MENUS:
            button = QPushButton()
            text = f'{menu["name"]} ({menu["price"]})'
            button.setText(text)
            button.setSizePolicy(H_BTN_POLICY,V_BTN_POLICY)
            button.clicked.connect(lambda *, m=menu: self.open_menu(m))
            self.menu_container.layout().addWidget(button)

    def setup_links(self):
        super().setup_links()

    def open_menu(self, menu: dict):
        # print(menu['name'])
        self.menu = menu
        self.menu_name_label.setText(menu["name"])
        self.menu_price_label.setText('{:.02f}'.format(menu["price"]))
        self.step = 0
        self.menu_container.hide()
        self.menu_details.show()
        self.show_menu_step()

    def clear_menu_step(self):
        while not self.menu_step_container.isEmpty():
            button = self.menu_step_container.takeAt(0)
            button.widget().setParent(None)

    def show_menu_step(self):
        self.clear_menu_step()
        step = self.menu['steps'][self.step]
        self.menu_step_label.setText(step['name'])
        for item in step['items']:
            button = QPushButton()
            button.setText(item)
            button.setSizePolicy(H_BTN_POLICY, V_BTN_POLICY)
            button.clicked.connect(lambda *, i=item: self.pick_menu_item(i))
            self.menu_step_container.addWidget(button)

    def pick_menu_item(self, item):
        self.step += 1
        self.items.append(item)
        if self.step >= len(self.menu['steps']):
            self.validate_menu()
        else:
            self.show_menu_step()

    def validate_menu(self):
        title = f'{self.menu["name"]} -- ({self.menu["price"]})'
        for item in self.items:
            title += f'\n - (item)'
        self.add_to_order(title, self.menu['price'])
        self.close_menu()

    def close_menu(self):
        self.menu = None
        self.step = -1
        self.items.clear()
        self.menu_container.show()
        self.menu_details.hide()
