import flet as ft
from fletx import Xstate

class ClientMainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
        self.page=page
        
    def GetHeghtWith(self):
        #طول و عرض صفحه نمایش کاربر
        return self.page.width,self.page.height
    
    def minus_click(self,e):
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.update()

    def plus_click(self,e):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.update()