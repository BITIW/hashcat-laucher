import flet as ft

def FinalizeMenu():
    return ft.Column([
        ft.Text("Finalize Menu"),
        ft.Checkbox(label="Preserve task config"),
        ft.Row([
            ft.Button("Create Task", on_click=lambda e: print("Create Task")),
            ft.Button("Import Config", on_click=lambda e: print("Import Configuration")),
            ft.Button("Export Config", on_click=lambda e: print("Export Configuration"))
        ])
    ])
