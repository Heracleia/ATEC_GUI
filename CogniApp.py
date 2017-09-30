from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty


class ColourLabel(Label):
    l = Label(text='Hello world')
    ellipse_colour = ListProperty([1, 0, 0, 1])

class ProgressMap(Widget):
    pass
    
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
