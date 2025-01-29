# A order Flet app
---------------------------------
install flet:
(pip install flet)

for upgreade
(pip install flet -upgreade)
--------------------------------


--------------------------------
creat new flet app
(flet create ./)

<./> means current directory,you can set any dirctory you want
--------------------------------


--------------------------------
To run the app:
(flet run [app_directory])

or

(flet run -d --assets main.py)
if you are in app_dirctory
and -d argument is for HotReload
assets argument is for path assets folder to app
like flutter you can see changes lives without rerun the app
if you want to rn as a webapplication:
(flet run --web --port 433 --host 1.1.1.1  main.py)
port argument is for specified port,unlless flet run app as a random port
host argument is an like port argument
-------------------------------------