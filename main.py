from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from database import DataBase


class CreateAccountWindow(Screen) :
    user_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.user_name.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0 :
            if self.password != "" :
                db.add_user(self.email.text, self.password.text, self.user_name.text)

                self.reset()

                wm.current = "login"

            else :
                invalidForm()

        else :
            invalidForm()

    def login(self):
        self.reset()
        wm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.user_name.text = ""

class LoginWindow(Screen) :
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text) :
            MainWindow.current = self.email.text
            self.reset()
            wm.current = "main"
        else :
            invalidLogin()

    def createBtn(self):
        self.reset()
        wm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen) :
    user_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        wm.current = "login"

    def on_enter(self):
        password, name, created = db.get_user(self.current)
        self.user_name.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

class WindowManager(ScreenManager) :
    pass

def invalidLogin() :
    pop = Popup(title = "Invalid Login",
                    content = Label(text = "Invalid username or password."),
                    size_hint = (None, None), size = (400, 400))

    pop.open()

def invalidForm() :
    pop = Popup(title = "Invalid Form",
                    content = Label(text = "Please fill all inputs with valid information"),
                    size_hint = (None, None), size = (400, 400))

kv = Builder.load_file("my.kv")

wm = WindowManager()

db = DataBase("users.txt")

screens = [LoginWindow(name = "login"), CreateAccountWindow(name = "create"), MainWindow(name = "main")]

for screen in screens :
    wm.add_widget(screen)

wm.current = "login"
class MyApp(App) :
    def build(self):
        return wm

if __name__  == "__main__" :
    MyApp().run()