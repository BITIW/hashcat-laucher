import flet as ft

def OutputMenu():
    return ft.Column([
        ft.Row([
            ft.Text("Output File"),
            ft.Button("Set Output File", on_click=lambda e: print("Open file dialog to select output file"))
        ]),
        ft.TextField(label="Output Format", hint_text="Choose output format"),
        ft.Dropdown(
            options=[
                ft.dropdown.Option("hash[:salt]"),
                ft.dropdown.Option("plain"),
                ft.dropdown.Option("hex_plain"),
                ft.dropdown.Option("crack_pos"),
                ft.dropdown.Option("timestamp absolute"),
                ft.dropdown.Option("timestamp relative")
            ],
            multiple=True,
            label="Select Output Format"
        )
    ])
