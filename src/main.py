import flet as ft
from fletx import Xapp,route
#وضعیت هر قسمت از برنامه رو توی پوشه وضعیت ها میریزیم
from states.ClientMainStates import ClientMainState
from states.AdminMainStates import AdminMainState
#هر صفحه ای که برنامه نیاز داره رو توی پوشه صفحه ها درست میکنیم
#admin pages
from views.admin.AdminHome import AdminHomeView
from views.admin.AdminLogin import AdminLoginView
#client pages
from views.client.home import HomeView
from views.client.login import LoginView
#404 view
from views.PageNotFoundeView import PageNotFoundView
#اگه برنامه به هر دلیلی با مشکلی مواجه بشه این صفحه نمایش داده میشه
from views.internal_error_view import InternalErrorView
# اینا ممکنه مفید باشن
#https://github.com/StanMathers/simple-datatable کار با جدول رو آسون میکنه
#https://github.com/SKbarbon/flet_translator برنامه رو چند زبانه میکنه
#https://github.com/saurabhwadekar/FletX صفحه ها و وضعیتهاشون رو مدیریت میکنه
#https://github.com/xavier53348/Flet-Box یه چیزی مثل بیسیک فور اندرویده با درگ اند دراپ کردن کنترل ها صفحه رو میسازه
#https://github.com/Marysia-Software-Limited/flet-django ترکیب جنگو با فلت



#! کتابخونه فلت پاس داده میشه و فلت کل برنامه رو از اینجا شروع میکنه،همه چیز رو app این تابع به تابع 
# از کتابخونه فلت رو میدیم که صفحه اصلی برنامه هستpageبه تابع یه تابع
#./temp/fletStrctur.png 
def main(page: ft.Page):
    # اگر برنامه در مرورگر اجرا بشه یا این گوشی های تاشو،هروفت طول و عرض برنامه تغیر کنه همه چیز از اول رندر میشه
   page.on_resized = lambda e: page.update()
    
             #درست کردن صفحه های برنامه و جا به جایی بینشون
             #  اول سعی کردم به خودم اینکار رو انجام بدم ولی دیدم یه پکیج واسه این کار درست شده و تصمیم گرفتم از پکیج استفاده کنم چون وضعیت برنامه رو هم خود پکیج هندل میکنه ولی اگه به هر دلیلی نخواستیم از پکیج استفاده کنیم میتونیم از کد هایی که قبلا نوشتم استفاده کنیم،فایل های هوم و لاگین در پوشه پیج ها رو به پوشه تمپ انتقال میدم تا بعدا اگه نیاز شد بدونیم چطوری کار میکردن و اسم پوشه پیجز رو به ویوز تغیر دادم
   #====================================================================================================================================================================================================================================================================================================================================================================================================================
   Xapp(
        page=page,
        #مسیر برنامه در وب اپلیکیشن با چه رشته ای مشخص بشه؟
        init_route="/",
        state=AdminMainState,
        #state=ClientMainState,
        # همه ی صفحه هایی که درست کردیم و ایمپورتشون کردیم رو اینجا مینویسیم و یه آدرس براش انتخاب میکنیم
        routes=[
            #admin routes
            route(route="/admin/",view=AdminHomeView),
            route(route="/admin/login",view=AdminLoginView),
            #client routes
            route(route="/",view=HomeView),
            route(route="/login",view=LoginView),
        ],
        not_found_view=PageNotFoundView,
        internal_error_view=InternalErrorView
        
   )
   #صفحه اول برنامه چی باشه؟
   page.go('/admin/login')
   #====================================================================================================================================================================================================================================================================================================================================================================================================================
             #درست کنیم که لیستی از کنترل ها رو برگردونه pagesواسه این کار کافیه یه فایل پایتون درون پوشه 
             #رو صدا میزنیم و اسم فایلی که درست کردیم رو بهش  میدیم page.go() واسه جابه جای در برنامه،هر کجای برنامه که خاستیم 
   #---------------------------------------------------------------------------------------------------------------------------------------------------
    # اگه کاربر در نسخه وب اپلیکیشن و در نوار آدرس مرورگرش،آدرس رو اشتباهی بزنه این صفحه میاره
    # def PageNotFoundView():
    #     NotFoundView = ft.View(
    #                 page.route,
    #                 [
    #                     ft.AppBar(title=ft.Text('404')),
    #                     ft.ElevatedButton('back to home page', on_click=lambda _: page.go("/home")),
    #                 ],
    #             )
    #     return NotFoundView
    # #pages لیستی از تمام فایل ها در پوشه 
    # ListOfViewFiles = os.listdir(str(os.getcwd())+"/pages")
    # # به ازای هر فایلی که پسوندش پایتون باشه یه ویو به این لیست اضافه میشه
    # ListOfView = []
    # for file in ListOfViewFiles:
    #     name,extension = os.path.splitext(file)
    #     if extension == ".py":
    #         module =importlib.import_module('pages.'+name)
    #         function = getattr(module,name)
    #         ListOfView.append(
    #             ft.View(
    #                 name,
    #                 function(page)
    #             )
    #         )
    # #پایین توضیح دادم چیکار میکنه(بین صفحات جابه جا میکنه)
    # def route_change(route):
    #     page.views.clear()
    #     ListOfViewIndex = 0
    #     for index in ListOfView:
    #         if index.route == page.route or '/'+index.route == page.route:
    #             break
    #         else:
    #             ListOfViewIndex+=1
    #     if ListOfViewIndex < len(ListOfView):
    #         page.views.append(ListOfView[ListOfViewIndex])
    #     else:
    #         page.views.append(PageNotFoundView())
    #     page.update()
    # # پایین توضیح دادم چی کار میکنه(تاریخچه ای از صفحات رو مدیریت میکنه)
    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[1]
    #     page.go(top_view.route)
    # #و چه با تغیر آدرس وب اپلیکیشن از نوار آدرس،صفحه رو عوض میکنه page.go('viewname') چه به صورت برنامه نویسی،یعنی صدا زدن 
    # page.on_route_change = route_change
    # # یه تاریخچه از تمام صفحات توی خودش داره و اینکه آخرین بار توی کدومش بودیم و قبل تر از اون،هر موقع روی دکمه های برگشت در نرم افزار کلیک کنیم،ما رو به یکی مونده به آخرین صفحه میبره
    # page.on_view_pop = view_pop
    # #pages اولین صفحه برنامه چی باشه؟،اسم یه فایل توی پوشه 
    # page.go('home')
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------










#خ ،یه برنامه دیگه رو اجرا میکنه و این برنامه برای زمانی هست که به هر دلیلی خطایی در برنامه اصلی رخ بده main این تابع هم مثل تابع 
# خطایی که نمیتونیم هندلش کنیم یا نمیتونیم پیش بینیش کینم،
def AppFiled(page: ft.Page):
    #tasks:میخوایم که به کاربر بگه مشکلی پیش اومده ui یه 
    #tasks: لاگ ها رو به سرور ارسال کنیم و ذخیره کینم،تا بتونیم بفهمیم مشکل چی بوده
    pass

# اگه برنامه با خطا مواجه شد برنامه دوم رو اجرا کن
try:
    ft.app(main)
except:
    ft.app(AppFiled)

