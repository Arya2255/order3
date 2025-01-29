import flet as ft
def home(page):
     return [
ft.AppBar(title=ft.Text("home")),               
ft.ElevatedButton("visit login", on_click=lambda _: page.go("/login"))               
          ]



