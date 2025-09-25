from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class NavBar(BoxLayout):
    def logout(self):
        App.get_running_app().logout()
