
from Grand_Restaurant_V2 import AppWindow

from config_Grand_Restau_menus import MENUS


class MenuWindow(AppWindow):
    def __init__(self):
        super().__init__()
        self.menu = None

    def load_items(self):
        super().load_items()
        self.load_menus()

    def load_menus(self):
        pass

    def setup_links(self):
        super().setup_links()

    def open_menu(self, menu: dict):
        pass

    def close_menu(self):
        pass

