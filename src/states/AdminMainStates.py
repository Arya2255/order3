import flet as ft
from fletx import Xstate
from assets.cloude import *
from assets.responsive import RatioOfWidth

class AdminMainState(Xstate):
    def __init__(self, page):
        super().__init__(page)
        self.page=page
        self.LoginPhoneNumberTextField = ft.TextField(label="شماره تماس",suffix_icon=ft.Icons.CALL,adaptive=True,autofill_hints="TELEPHONE_NUMBER_DEVICE",autofocus=True,input_filter=ft.NumbersOnlyInputFilter(),keyboard_type=ft.KeyboardType.PHONE,max_length=11,on_change=self.on_text_change,width=RatioOfWidth(page, 1.5))
        self.LoginButton = ft.ElevatedButton("ورود",on_click=self.SendSms,disabled=True)

        self.LoginVerifyButtomSheet = ft.BottomSheet(dismissible=False,maintain_bottom_view_insets_padding=True,show_drag_handle=True,enable_drag=True,content=ft.Container(padding=10,content=ft.Column(tight=True,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
            ft.Row(controls=[
                ft.TextField(adaptive=True,autofill_hints=ft.AutofillHint.ONE_TIME_CODE,autofocus=True,input_filter=ft.NumbersOnlyInputFilter(),keyboard_type=ft.KeyboardType.NUMBER,max_length=1,width=RatioOfWidth(page,15),text_align=ft.TextAlign.CENTER),ft.TextField(adaptive=True,input_filter=ft.NumbersOnlyInputFilter(),keyboard_type=ft.KeyboardType.NUMBER,max_length=1,width=RatioOfWidth(page,15),text_align=ft.TextAlign.CENTER),ft.TextField(adaptive=True,input_filter=ft.NumbersOnlyInputFilter(),keyboard_type=ft.KeyboardType.NUMBER,max_length=1,width=RatioOfWidth(page,15),text_align=ft.TextAlign.CENTER),ft.TextField(adaptive=True,input_filter=ft.NumbersOnlyInputFilter(),keyboard_type=ft.KeyboardType.NUMBER,max_length=1,width=RatioOfWidth(page,15),text_align=ft.TextAlign.CENTER),ft.TextField(adaptive=True,input_filter=ft.NumbersOnlyInputFilter(),keyboard_type=ft.KeyboardType.NUMBER,max_length=1,width=RatioOfWidth(page,15),text_align=ft.TextAlign.CENTER)
            ],tight=True,wrap=True,alignment=ft.MainAxisAlignment.CENTER),
            ft.ElevatedButton("تایید")
            ]
        )))
           
    def SendSms(self,e):
        #این تابع برای ارسال کد تایید به شماره تماس وارد شده توسط کاربر استفاده میشه
        print('called')
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.open(self.LoginVerifyButtomSheet)
        
        


    def on_text_change(self, e):
        # Enable the button if the text field contains exactly 11 digits
        self.LoginButton.disabled = len(self.LoginPhoneNumberTextField.value) != 11
        self.update()





























    # def minus_click(self,e):
    #     self.txt_number.value = str(int(self.txt_number.value) - 1)
    #     self.update()

    # def plus_click(self,e):
    #     self.txt_number.value = str(int(self.txt_number.value) + 1)
    #     self.update()