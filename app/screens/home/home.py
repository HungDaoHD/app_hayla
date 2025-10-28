from pathlib import Path
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen



KV_PATH = Path(__file__).with_name("home.kv")
Builder.load_file(str(KV_PATH))



class HomeScreen(Screen):
    pass
