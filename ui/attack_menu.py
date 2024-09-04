import flet as ft

def AttackMenu():
    # Функция для обновления доступных полей на основе выбранного режима атаки
    def update_attack_mode_fields(selected_mode):
        attack_mode_controls.controls.clear()
        if selected_mode == "Dictionary Attack":
            attack_mode_controls.controls.extend([
                ft.Text("Dictionaries:"),
                ft.TextField(hint_text="Select Dictionaries"),
                ft.Text("Rules (optional):"),
                ft.TextField(hint_text="Select Rules [Max. 4]")
            ])
        elif selected_mode == "Combinator Attack":
            attack_mode_controls.controls.extend([
                ft.Text("Left Dictionary:"),
                ft.TextField(hint_text="Select Left Dictionary"),
                ft.Text("Right Dictionary:"),
                ft.TextField(hint_text="Select Right Dictionary"),
                ft.Text("Left Rule (optional):"),
                ft.TextField(hint_text="Set Left Rule"),
                ft.Text("Right Rule (optional):"),
                ft.TextField(hint_text="Set Right Rule")
            ])
        elif selected_mode == "Mask Attack":
            attack_mode_controls.controls.extend([
                ft.Text("Mask:"),
                ft.TextField(hint_text="Set Mask"),
                ft.Text("Custom charset 1 (optional):"),
                ft.TextField(hint_text="Set Custom charset 1"),
                ft.Text("Custom charset 2 (optional):"),
                ft.TextField(hint_text="Set Custom charset 2"),
                ft.Text("Custom charset 3 (optional):"),
                ft.TextField(hint_text="Set Custom charset 3"),
                ft.Text("Custom charset 4 (optional):"),
                ft.TextField(hint_text="Set Custom charset 4"),
                ft.Checkbox(label="Mask increment mode (optional)"),
                ft.Row([
                    ft.TextField(hint_text="Min", width=50),
                    ft.TextField(hint_text="Max", width=50)
                ])
            ])
        # Добавить остальные режимы атаки аналогично
        attack_mode_controls.update()

    attack_mode_controls = ft.Column()

    attack_mode_selector = ft.Dropdown(
        label="Attack Mode",
        options=[
            ft.dropdown.Option("Dictionary Attack"),
            ft.dropdown.Option("Combinator Attack"),
            ft.dropdown.Option("Mask Attack"),
            ft.dropdown.Option("Hybrid1 (Dictionary + Mask)"),
            ft.dropdown.Option("Hybrid2 (Mask + Dictionary)")
        ],
        on_change=lambda e: update_attack_mode_fields(e.control.value)
    )

    return ft.Column([
        attack_mode_selector,
        attack_mode_controls
    ])
