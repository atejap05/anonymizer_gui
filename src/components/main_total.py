from nicegui import ui


class SideBar:
    def __init__(self, btn_show_drower):
        self.left_drawer = ui.left_drawer().classes('bg-blue-100')
        self.btn_show_drower = btn_show_drower
        self.btn_show_drower.visible = False

    def handle_btn_show_drawer(self):
        self.left_drawer.toggle()
        self.btn_show_drower.visible = False

    def handle_btn_hide_drawer(self):
        self.left_drawer.toggle()
        self.btn_show_drower.visible = True

    def handle_input_allowlist(self, input_allow):
        print(input_allow.value)
        input_allow.set_value(None)

    def handle_input_denylist(self, input_deny):
        print(input_deny.value)
        input_deny.set_value(None)

    def create_side_bar(self):
        with self.left_drawer:
            ui.button(
                on_click=self.handle_btn_hide_drawer,
                icon='arrow_back_ios_new').props('flat').classes('absolute top-4 right-0 rounded-lg mr-2')

            ### Title ###
            with ui.row().classes('text-xl text-gray-700 font-bold ml-4 mt-16'):
                ui.label('Opções de Anonimização')

            ui.separator()

            ### Inputs ###
            # Input Model
            with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):
                with ui.icon('help_outline').classes('absolute right-0 top-0 mr-2 '):
                    ui.tooltip('Selecione qual modelo - Named Entity Recognition (NER) -\
                                será usado para detecção de Personally Identifiable Information (PII).')\
                        .classes('bg-zinc-700 text-bold w-64')
                ui.select(['obi/deid_roberta_i2b2', 'modelo 2', 'modelo 3'],
                          label='Modelo').classes('w-full pl-2 pr-2')

            # Input Method
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
                    .classes('w-full pl-2 pr-2')

            # Input Threshold
            with ui.row().classes(' flex justify-center gap-1 text-lg w-full text-gray-700 font-bold  mt-8'):
                ui.label('Threshold')
                slider = ui.slider(min=0.1, max=1.00, step=0.01,
                                   value=0.35).classes('w-11/12')
                ui.label().bind_text_from(slider, 'value').classes(
                    'text-md ml-2 border rounded-lg border-gray-400 w-1/5 text-center p-1 shadow')

            # Input Allowlist and Denylist
            with ui.row().classes('relative text-lg w-full text-gray-700 font-bold py-4 mt-8'):

                with ui.expansion('Allawlists and denylists').classes('w-full'):
                    # Allowlist
                    input_allow = ui.input(
                        label="Add word to allowlist",
                        placeholder='Enter word and press enter.')\
                        .on('keydown.enter', lambda: self.handle_input_allowlist(input_allow))\
                        .classes('w-full')

                    # Denylist
                    input_deny = ui.input(
                        label="Add word to denylist",
                        placeholder='Enter word and press enter.')\
                        .on('keydown.enter', lambda: self.handle_input_denylist(input_deny))\
                        .classes('w-full')


class MainContent():
    def __init__(self):
        self.grid = ui.grid().classes("mt-0 p-8 pt-16 w-full h-screen bg-blue-50")
        side_bar = SideBar(self.btn_show_drower)
        self.btn_show_drower = ui.button(on_click=side_bar.handle_btn_show_drawer,
                                         icon='arrow_forward_ios').props('flat').classes('rounded-lg')
        self.btn_show_drower.visible = False
        self.labels = [['Label 1', 'Label 2'], ['Label 3', 'Label 4'], [
            'Label 5', 'Label 6'], ['Label 7', 'Label 8']]

    def create_main_content(self):
        with self.grid:

            # Button to show the left drawer
            with ui.page_sticky(position='top-left', x_offset=0, y_offset=20):
                self.btn_show_drower
            with ui.row().classes('w-full h-48 place-content-start bg-sky-100 p-0 m-0 '):
                pass

            for i in range(0, len(self.labels), 2):
                with ui.row() as row:
                    with ui.column() as col:
                        ui.label(self.labels[i][0])
                        ui.label(self.labels[i][1])
                    with ui.column() as col:
                        ui.label(self.labels[i+1][0])
                        ui.label(self.labels[i+1][1])

        self.side_bar.create_side_bar()


# Usage
main_content = MainContent()
main_content.create_main_content()

ui.run()
