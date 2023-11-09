from nicegui import ui
from components.SideBar.SideBarClasse import SideBar
from components.MainContent.MainContentClass import MainContent


# TODO: Incluir Header e mudar a classe para Layout

class ToggleSideBar():

    def __init__(self) -> None:
        self.side_bar = SideBar()
        self.main_content = MainContent()

    def handle_btn_show_drawer(self):
        self.side_bar.left_drawer.toggle()
        self.main_content.btn_show_drower.visible = False

    def handle_btn_hide_drawer(self):
        self.side_bar.left_drawer.toggle()
        self.main_content.btn_show_drower.visible = True

    # Button to show the left drawer
    def create_toggle(self):

        self.side_bar.create_side_bar()
        self.main_content.create_main_content()

        with ui.page_sticky(position='top-left', x_offset=0, y_offset=20):
            self.main_content.btn_show_drower = ui.button(
                on_click=self.handle_btn_show_drawer,
                icon='arrow_forward_ios').props('flat').classes('rounded-lg')
            self.main_content.btn_show_drower.visible = False

        with self.side_bar.left_drawer:
            ui.button(
                on_click=self.handle_btn_hide_drawer,
                icon='arrow_back_ios_new').props('flat').classes('absolute top-4 right-0 rounded-lg mr-2')
