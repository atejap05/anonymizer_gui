from nicegui import ui


def side_bar(btn_show_drower):

    def handle_btn_show_drawer():
        left_drawer.toggle()
        btn_show_drower.visible = False

    def handle_btn_hide_drawer():
        left_drawer.toggle()
        btn_show_drower.visible = True

    def handle_input_allowlist():
        print(input_allow.value)
        input_allow.set_value(None)

    def handle_input_denylist():
        print(input_deny.value)
        input_deny.set_value(None)

    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        btn_hide_drower = ui.button(
            on_click=handle_btn_hide_drawer,
            icon='arrow_back_ios_new').props('flat').classes('absolute top-4 right-0 rounded-lg mr-2')
        

        ### Title ###
        with ui.row().classes('text-xl text-gray-700 font-bold ml-4 mt-16'):
            ui.label('Opções de Anonimização')
        
        ui.separator()

        ### Inputs ###
        ## Input Model
        with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):
            with ui.icon('help_outline').classes('absolute right-0 top-0 mr-2 '):
                ui.tooltip('Selecione qual modelo - Named Entity Recognition (NER) -\
                            será usado para detecção de Personally Identifiable Information (PII).')\
                                .classes('bg-zinc-700 text-bold w-64')
            ui.select(['obi/deid_roberta_i2b2', 'modelo 2', 'modelo 3'], label='Modelo').classes('w-full pl-2 pr-2' )
        
        ## Input Method
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
            
        ## Input Threshold
        with ui.row().classes(' flex justify-center gap-1 text-lg w-full text-gray-700 font-bold  mt-8'):
            ui.label('Threshold')
            slider = ui.slider(min=0.1, max=1.00, step=0.01, value=0.35).classes('w-11/12')
            ui.label().bind_text_from(slider, 'value').classes('text-md ml-2 border rounded-lg border-gray-400 w-1/5 text-center p-1 shadow')
        
        ## Input Allowlist and Denylist
        with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):
            
            with ui.expansion('Allawlists and denylists').classes('w-full'):
                ## Allowlist
                input_allow = ui.input(
                    label="Add word to allowlist",
                    placeholder='Enter word and press enter.')\
                    .on('keydown.enter', handle_input_allowlist)\
                        .classes('w-full')
                
                ## Denylist
                input_deny = ui.input(
                    label="Add word to denylist",
                    placeholder='Enter word and press enter.')\
                    .on('keydown.enter', handle_input_denylist)\
                        .classes('w-full')
