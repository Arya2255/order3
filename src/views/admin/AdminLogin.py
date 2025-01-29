import flet as ft 
from fletx import Xview

class AdminLoginView(Xview):
    
    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.state.LoginPhoneNumberTextField,
                self.state.LoginButton
            ]
        )