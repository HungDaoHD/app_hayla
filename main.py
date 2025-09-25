from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.properties import BooleanProperty, StringProperty

# Import your screens & widgets so KV can find the classes
from app.screens.login import LoginScreen
from app.screens.home import HomeScreen
from app.widgets.nav import NavBar



Builder.load_file("app.kv")


class Root(ScreenManager):
    pass


class AppHayla(App):
    # super-simple auth state (replace with real service later)
    is_authenticated = BooleanProperty(False)
    user = StringProperty("")

    
    def login(self, username: str, password: str) -> bool:
        
        # TODO: replace with real auth (API call, DB, etc.)
        ok = bool(username.strip()) and bool(password.strip())
        self.is_authenticated = ok
        
        if ok:
            self.user = username.strip()
            self.root.current = "home"
            
        return ok # test push

    
    def logout(self):
        self.is_authenticated = False
        self.user = ""
        self.root.current = "login"
    
        
    def build(self):
        sm = Root(transition=NoTransition())
        sm.current = "login"
        return sm


if __name__ == "__main__":
    AppHayla().run()
    