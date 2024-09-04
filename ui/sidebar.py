import flet as ft

def create_sidebar(update_content):
    return ft.Column(
        [
            ft.TextButton("Target", on_click=lambda e: update_content("Target")),
            ft.TextButton("Attack", on_click=lambda e: update_content("Attack")),
            ft.TextButton("Advanced", on_click=lambda e: update_content("Advanced")),
            ft.TextButton("Output", on_click=lambda e: update_content("Output")),
            ft.TextButton("Finalize", on_click=lambda e: update_content("Finalize")),
            ft.TextButton("Tasks", on_click=lambda e: update_content("Tasks")),
        ],
        alignment=ft.MainAxisAlignment.START,
        width=200
    )
