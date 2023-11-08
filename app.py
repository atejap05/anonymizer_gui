from nicegui import ui




def handle_btn_show_drawer():
    left_drawer.toggle()
    btn_show_drower.visible = False


def handle_btn_hide_drawer():
    left_drawer.toggle()
    btn_show_drower.visible = True


with ui.header(elevated=True).classes(replace='row items-center h-20') as header:

    ## TODO: Replace the curent url with the Labin01 page link
    with ui.link(target='https://www.gov.br/receitafederal/pt-br', new_tab=True):
        ui.image('src/assets/imgs/logo_labin-removebg.png').classes(' ml-4 h-16 w-16')

    ui.label('Anonimizador de Dados Sigilosos').classes('ml-4 text-2xl font-bold')



with ui.grid().classes("mt-0 p-8 pt-16 w-full h-screen bg-blue-50") as grid:
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



with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    btn_hide_drower = ui.button(
        on_click=handle_btn_hide_drawer,
        icon='arrow_back_ios_new').props('flat').classes('absolute top-4 right-0 rounded-lg mr-2')
    with ui.row():
        pass

    ui.label('Side menu')

# with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
#     ui.button(on_click=footer.toggle, icon='contact_support').props('fab')


ui.run()









