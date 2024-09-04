import flet as ft

def TargetMenu():
    return ft.Column([
        ft.Text("Target Menu"),
        ft.Row([
            ft.Text("Select Hash"),
            ft.TextField(hint_text="Select Hash File"),
        ]),
        ft.Row([
            ft.Text("Select Algorithm"),
            ft.Dropdown(
                options=[
                    ft.dropdown.Option("MD5"),
                    ft.dropdown.Option("SHA-1"),
                    ft.dropdown.Option("SHA-256")
                ],
                hint_text="Select Algorithm"
            )
        ])
    ])
