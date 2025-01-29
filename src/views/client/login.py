import flet as ft 
from fletx import Xview

class LoginView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(),
                ft.ElevatedButton("<< Back",on_click=lambda e:self.page.go("/"))
            ]
        )