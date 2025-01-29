import flet as ft 
from fletx import Xview

class AdminHomeView(Xview):

    def build(self):
        
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Home View"),
                ft.ElevatedButton("Go Counter View",on_click=lambda e:self.page.go("/admin/login")),
                ft.FloatingActionButton(icon=ft.Icons.ADD, shape=ft.CircleBorder()),
            ],
            floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
            bottom_appbar=ft.BottomAppBar(
                bgcolor=ft.Colors.BLUE,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE, on_click=lambda e:self.page.open(self.HomeDrawer)),
                        ft.Container(expand=True),
                        ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
                        ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
                    ]
                ),
            )
        )
