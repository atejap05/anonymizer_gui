from nicegui import ui


class MainContent:
    def __init__(self):
        self.grid = ui.grid().classes("mt-0 p-8 pt-16 w-full h-screen bg-blue-50")
        self.btn_show_drower = None
        self.labels = [['Label 1', 'Label 2'], ['Label 3', 'Label 4'], [
            'Label 5', 'Label 6'], ['Label 7', 'Label 8']]

    def create_main_content(self):
        with self.grid:

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
