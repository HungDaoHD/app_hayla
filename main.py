from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition


# Import your screens & widgets so KV can find the classes
from app.themes.theme import Theme
from app.screens.login.login import LoginScreen
from app.screens.home.home import HomeScreen
# from app.widgets.nav import NavBar



Builder.load_file("app.kv")





class Root(ScreenManager):
    pass



class AppHayla(App):
        
        
    def build(self):
        
        self.theme = Theme()
        self._mode = "light"
        self.theme.set_light()
        
        sm = Root(transition=NoTransition())
        sm.current = "login"
        
        return sm
        
        

if __name__ == "__main__":
    AppHayla().run()



