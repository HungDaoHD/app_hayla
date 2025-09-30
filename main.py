from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.properties import BooleanProperty, StringProperty, ColorProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.event import EventDispatcher
from kivy.utils import get_color_from_hex


# Import your screens & widgets so KV can find the classes
from app.screens.login import LoginScreen
from app.screens.home import HomeScreen
from app.widgets.nav import NavBar





# 1) Register your fonts once (put TTFs in ./fonts/)
LabelBase.register(
    name="Inter",
    fn_regular="assets/fonts/Inter/static/Inter_18pt-Regular.ttf",
    fn_bold="assets/fonts/Inter/static/Inter_18pt-Bold.ttf",
)


Builder.load_file("app.kv")



# self.themes = {
#     'light': {
#         'bg': get_color_from_hex('#F7F5E8'),
#         'text': get_color_from_hex('#434343'),
#         'button': get_color_from_hex('#008F37'),
#         'weekday_color': {
#             0: get_color_from_hex('#434343'),
#             1: get_color_from_hex('#434343'),
#             2: get_color_from_hex('#434343'),
#             3: get_color_from_hex('#434343'),
#             4: get_color_from_hex('#434343'),
#             5: get_color_from_hex('#02a2e6'),
#             6: get_color_from_hex('#f25238'),
#         }
#     },
#     }


class Theme(EventDispatcher):
    # simple container for colors & fonts
    bg         = ColorProperty(get_color_from_hex('#F7F5E8'))   # background
    surface    = ColorProperty([1, 1, 1, 1])   # cards/panels
    text       = ColorProperty([0.95, 0.95, 0.96, 1])   # primary text
    text_muted = ColorProperty([0.75, 0.75, 0.78, 1])   # secondary text
    accent     = ColorProperty(get_color_from_hex('#008F37'))   # brand color
    danger     = ColorProperty([0.95, 0.27, 0.27, 1])

    font_regular = StringProperty("Inter")
    font_bold    = StringProperty("Inter")
    base_size_sp = NumericProperty(16)

    
        
    def set_light(self):
        self.bg         = get_color_from_hex('#F7F5E8')
        self.surface    = [1, 1, 1, 1]
        self.text       = [0.11, 0.11, 0.13, 1]
        self.text_muted = [0.35, 0.35, 0.40, 1]
        self.accent     = get_color_from_hex('#008F37')


    
    def set_dark(self):
        self.bg         = [0.07, 0.07, 0.09, 1]
        self.surface    = [0.12, 0.12, 0.16, 1]
        self.text       = [0.95, 0.95, 0.96, 1]
        self.text_muted = [0.75, 0.75, 0.78, 1]
        self.accent     = [0.31, 0.53, 0.96, 1]



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
            
        return ok

    
    def logout(self):
        self.is_authenticated = False
        self.user = ""
        self.root.current = "login"
    
        
    def build(self):
        
        self.theme = Theme()
        self._mode = "light"
        self.theme.set_light()
        
        sm = Root(transition=NoTransition())
        sm.current = "login"
        
        return sm
        
        
        

if __name__ == "__main__":
    AppHayla().run()
    