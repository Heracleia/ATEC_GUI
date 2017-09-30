from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class ProgressMap(Widget):
    l = Label(text='Hello world')

class GamesA(Screen):
    pass

class MainScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("CogniApp.kv")

class CogniApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    CogniApp().run()
