from nicegui import ui

from components.Header.Header import Header
from components.SideBar.ToggleSideBar import ToggleSideBar


def main():
    header = Header()
    toggle_side_bar = ToggleSideBar()

    header.create_header()
    toggle_side_bar.create_toggle()

    ui.run()
