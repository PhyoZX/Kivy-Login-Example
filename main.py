from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager

from database import DataBase


class CreateAccountWindow(Screen) :
    user_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

class LoginWindow(Screen) :
    email = ObjectProperty(None)
    password = ObjectProperty(None)

class MainWindow(Screen) :
    name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)

class WindowManager(ScreenManager) :
    pass

kv = Builder.load_file("my.kv")

wm = WindowManager()

db = DataBase("users.txt")



class MyApp(App) :
    def build(self):
        return wm

if __name__  == "__main__" :
    MyApp().run()