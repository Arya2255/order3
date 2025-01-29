import flet as ft 
from fletx import Xview

class HomeView(Xview):

    def build(self):
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            appbar=ft.AppBar(
                leading=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icon(ft.Icons.ACCOUNT_CIRCLE),
                            adaptive=True,
                        ),
                        ft.Text("ایجاد حساب")
                    ]
                ),
                leading_width=100,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
                title=ft.Text("با ایجاد حساب از هزینه کارمزد انتقال جلو گیری کنید."),
                adaptive=True,
                center_title=True,
                force_material_transparency=True,
                toolbar_opacity=0.5,
            ),
            controls=[
                ft.Text("Home View"),
                ft.Text(f"Counts = {self.state.txt_number.value}"),
                ft.ElevatedButton("Go Counter View",on_click=lambda e:self.page.go("/login"))
            ]
        )
