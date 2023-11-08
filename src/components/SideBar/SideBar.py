from nicegui import ui


def toggle_drawer():
    
    ui.button('🍔', on_click=lambda: drawer.toggle())

    with ui.left_drawer(bordered=True).props('width=225') as drawer:
        ui.button('🍔', on_click=lambda: drawer.toggle())
        
        ui.label('Label 1')
        ui.label('Label 2')