from kivy.uix.screenmanager import Screen
from kivy.app import App


class LoginScreen(Screen):
    def try_login(self, username: str, password: str):
        ok = App.get_running_app().login(username, password)
        if not ok:
            # Show a friendly error via id defined in KV
            self.ids.error_lbl.text = "Invalid credentials. Try again."
        else:
            self.ids.error_lbl.text = ""