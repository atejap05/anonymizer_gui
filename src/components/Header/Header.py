from nicegui import ui


def header():
    with ui.header(elevated=True).classes(replace='row items-center h-20') as header:
    ## TODO: Replace the curent url with the Labin01 page link
        with ui.link(target='https://www.gov.br/receitafederal/pt-br', new_tab=True):
            ui.image('src/assets/imgs/logo_labin-removebg.png').classes(' ml-4 h-16 w-16')

        ui.label('Anonimização de Dados Sigilosos').classes('ml-4 text-2xl font-bold')