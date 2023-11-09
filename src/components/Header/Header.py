from nicegui import ui


class Header:
    def __init__(self):
        self.header = ui.header(elevated=True).classes(
            replace='row items-center h-20')
        self.link_target = 'https://www.gov.br/receitafederal/pt-br'
        self.image_path = 'src/assets/imgs/logo_labin-removebg.png'
        self.label_text = 'Anonimização de Dados Sigilosos'

    def create_header(self):
        with self.header:
            with ui.link(target=self.link_target, new_tab=True):
                ui.image(self.image_path).classes(' ml-4 h-16 w-16')

            ui.label(self.label_text).classes('ml-4 text-2xl font-bold')

        ui.run()


# Usage
header = Header()
header.create_header()
