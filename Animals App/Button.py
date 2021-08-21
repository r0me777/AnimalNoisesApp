import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.core.audio import SoundLoader


class AppLayout(GridLayout):
    def play_music(self, MusicName):
        music = SoundLoader.load(MusicName)

        if music:
            music.play()


class ButtonApp(App):
    pass


if __name__ == "__main__":
    ButtonApp().run()
