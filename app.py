from nicegui import ui

# TODO: Separar o app em arquivos/componentes/modulos diferentes (Modularizacao do frontend)
# TODO: Criar um componente para o header
# TODO: Criar um componente para o sidebar
# TODO: Criar um componente para o main_content 
# TODO: Adicionar util functions em cada aquivo/componente/modulo correspondente
# TODO: Criar heuristica/logica para montar um objeto com os valores dos inputs. Como em um formulario
# TODO: Exibir Allowlist e Denylist em uma tabela no main_content
# TODO: Exibir o resultado da anonimização em uma text area no main_content
# TODO: Pensar uma forma melhor de exibir as Entities que seráo anonimizadas para o usuario as escolher
# TODO: Criar um About page com as informações do projeto
# TODO: Adicionar as resquisições para o backend (POST /api/anonimizar)


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

    ui.label('Anonimização de Dados Sigilosos').classes('ml-4 text-2xl font-bold')

    

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
    
    with ui.row().classes('text-xl text-gray-700 font-bold ml-4 mt-16'):
        ui.label('Opções de Anonimização')
    
    ui.separator()

    with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):
        with ui.icon('help_outline').classes('absolute right-0 top-0 mr-2 '):
            ui.tooltip('Selecione qual modelo - Named Entity Recognition (NER) -\
                          será usado para detecção de Personally Identifiable Information (PII).')\
                            .classes('bg-zinc-700 text-bold w-64')
        ui.select(['obi/deid_roberta_i2b2', 'modelo 2', 'modelo 3'], label='Modelo').classes('w-full pl-2 pr-2' )
    

    with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):
        with ui.icon('help_outline').classes('absolute right-0 top-0 mr-2 '):
            ui.tooltip("""Select which manipulation to the text is requested after PII has been identified.\n
                        Redact: Completely remove the PII text\n
                        Replace: Replace the PII text with a constant, e.g. <PERSON>\n
                        Mask: Replaces a requested number of characters with an asterisk (or other mask character)\n
                        Hash: Replaces with the hash of the PII string\n
                        Encrypt: Replaces with an AES encryption of the PII string, allowing the process to be reversed""")\
                            .classes('bg-zinc-700 text-bold w-64')
        ui.select(['Redact', 'Replace', 'Mask', 'Hash', 'Encrypt', 'Replace'], label='Método de Anonimização')\
            .classes('w-full pl-2 pr-2' )
        
    with ui.row().classes(' flex justify-center gap-1 text-lg w-full text-gray-700 font-bold  mt-8'):
        ui.label('Threshold')
        slider = ui.slider(min=0.1, max=1.00, step=0.01, value=0.35).classes('w-11/12')
        ui.label().bind_text_from(slider, 'value').classes('text-md ml-2 border rounded-lg border-gray-400 w-1/5 text-center p-1 shadow')
    

    # Create a global variable to store the input value
    input_value = ''

    # Define a function to handle the input change event
    def handle_input_allowlist():
        print(input_allow.value)
        input_allow.set_value(None)

    def handle_input_denylist():
        print(input_deny.value)
        input_deny.set_value(None)

    with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):
        with ui.expansion('Allawlists and denylists').classes('w-full'):
            input_allow = ui.input(
                label="Add word to allowlist",
                placeholder='Enter word and press enter.')\
                .on('keydown.enter', handle_input_allowlist)\
                    .classes('w-full')
            

            input_deny = ui.input(
                label="Add word to denylist",
                placeholder='Enter word and press enter.')\
                .on('keydown.enter', handle_input_denylist)\
                    .classes('w-full')




ui.run()









