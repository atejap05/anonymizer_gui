from nicegui import ui

def btn_show_drower():
    pass



def main_content(handle_btn_show_drawer):
    with ui.grid().classes("mt-0 p-8 pt-16 w-full h-screen bg-blue-50") as grid:

        ## Button to show the left drawer
        with ui.page_sticky(position='top-left', x_offset=0, y_offset=20):
            btn_show_drower =  ui.button(
                on_click=handle_btn_show_drawer,
                icon='arrow_forward_ios').props('flat').classes('rounded-lg')
            btn_show_drower.visible = False
        
        with ui.row().classes('w-full h-48 place-content-start bg-sky-100 p-0 m-0 '):
            pass
        
        with ui.row() as row:
            with ui.column() as col:
                ui.label('Label 1')
                ui.label('Label 2')
            with ui.column() as col:
                ui.label('Label 3')
                ui.label('Label 4')
        with ui.row() as row:
            with ui.column() as col:
                ui.label('Label 5')
                ui.label('Label 6')
            with ui.column() as col:
                ui.label('Label 7')
                ui.label('Label 8')

