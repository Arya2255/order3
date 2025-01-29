import flet as ft
def login(page):
     return [
ft.AppBar(title=ft.Text("login")),               
ft.ElevatedButton("visit home", on_click=lambda _: page.go("/home"))               
          ]



