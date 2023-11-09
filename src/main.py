from src.components.Header.Header import header
from src.components.SideBar.SideBar import side_bar
from src.components.MainContent.MainContent import main_content


def main():
    header()
    side_bar(btn_show_drower=btn_show_drower)
    main_content(handle_btn_show_drawer=handle_btn_show_drawer)