import flet as ft
from ui.sidebar import create_sidebar
from ui.target_menu import TargetMenu
from ui.attack_menu import AttackMenu
from ui.advanced_menu import AdvancedMenu
from ui.output_menu import OutputMenu
from ui.finalize_menu import FinalizeMenu
from ui.tasks_menu import TasksMenu

def main(page: ft.Page):
    page.title = "Hashcat Launcher"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = "auto"

    # Создание контейнера для контента
    content_container = ft.Column(expand=True)

    # Функция для обновления контента в зависимости от выбранного меню
    def update_content(menu_name):
        content_container.controls.clear()
        if menu_name == "Target":
            content_container.controls.append(TargetMenu())
        elif menu_name == "Attack":
            content_container.controls.append(AttackMenu())
        elif menu_name == "Advanced":
            content_container.controls.append(AdvancedMenu())
        elif menu_name == "Output":
            content_container.controls.append(OutputMenu())
        elif menu_name == "Finalize":
            content_container.controls.append(FinalizeMenu())
        elif menu_name == "Tasks":
            content_container.controls.append(TasksMenu())
        page.update()

    # Создание бокового меню
    sidebar = create_sidebar(update_content)

    # Основная разметка страницы
    page.add(
        ft.Row(
            [
                sidebar,
                ft.VerticalDivider(),
                content_container,
            ],
            expand=True
        )
    )

ft.app(target=main)
