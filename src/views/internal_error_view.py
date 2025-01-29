import flet as ft 
from fletx import Xview

class InternalErrorView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                 ft.Text("something went wrong"),
            ]
           
        )