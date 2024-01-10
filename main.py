import kivy

from kivy.app import App
from kivy.uix.button import Button

class NewApp(App):
    def build(self):
        return Button(
            text='Hello World',
            pos=(50,50),
            size_hint=(.5,.5))

if __name__ == '__main__':
    NewApp().run()