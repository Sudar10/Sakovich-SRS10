from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Регистрация"))
        self.username = TextInput(hint_text='Имя пользователя')
        self.add_widget(self.username)
        self.password = TextInput(hint_text='Пароль', password=True)
        self.add_widget(self.password)
        self.register_button = Button(text='Зарегистрироваться', on_press=self.register)
        self.add_widget(self.register_button)

    def register(self, instance):
        username = self.username.text
        password = self.password.text
        # Реализуйте здесь логику регистрации пользователя
        with open('users.txt', 'a') as f:
            f.write(f"{username},{password}\n")
        print(f"Регистрация нового пользователя: {username}, {password}")

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Авторизация"))
        self.username = TextInput(hint_text='Имя пользователя')
        self.add_widget(self.username)
        self.password = TextInput(hint_text='Пароль', password=True)
        self.add_widget(self.password)
        self.login_button = Button(text='Войти', on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        username = self.username.text
        password = self.password.text
        # Реализуйте здесь логику авторизации пользователя
        print(f"Вход пользователя: {username}, {password}")

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Главный экран"))

class AuthApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    AuthApp().run()
