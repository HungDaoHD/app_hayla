from kivy.properties import BooleanProperty, StringProperty, ColorProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.event import EventDispatcher
from kivy.utils import get_color_from_hex


# 1) Register your fonts once (put TTFs in ./fonts/)
LabelBase.register(
    name="Inter",
    fn_regular="assets/fonts/Inter/static/Inter_18pt-Regular.ttf",
    fn_bold="assets/fonts/Inter/static/Inter_18pt-Bold.ttf",
)


# themes = {
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
# }


class Theme(EventDispatcher):
    
    # fonts 
    font_regular = StringProperty("Inter")
    font_bold    = StringProperty("Inter")
    base_size_sp = NumericProperty(16)

    # colors
    bg         = ColorProperty(get_color_from_hex("#F3F3F3")) # background
    text       = ColorProperty(get_color_from_hex('#1E1E1E')) # primary text
    text_muted = ColorProperty(get_color_from_hex('#BFBFC7')) # secondary text
    primary    = ColorProperty(get_color_from_hex('#008F37')) # brand color
    secondary  = ColorProperty(get_color_from_hex('#F7F5E8')) # cards/panels
    warning    = ColorProperty(get_color_from_hex('#FFC107'))
    danger     = ColorProperty(get_color_from_hex('#F24545'))
    
    
    
    def set_light(self):
        self.bg         = get_color_from_hex("#F3F3F3")
        self.text       = get_color_from_hex("#1E1E1E")
        self.text_muted = get_color_from_hex('#BFBFC7')
        self.primary    = get_color_from_hex('#008F37')
        self.secondary  = get_color_from_hex('#F7F5E8')
        
    
    
    def set_dark(self):
        self.bg         = get_color_from_hex('#1E1E1E')
        self.text       = get_color_from_hex('#F3F3F3')
        self.text_muted = get_color_from_hex('#BFBFC7')
        self.primary    = get_color_from_hex('#008F37')
        self.secondary  = get_color_from_hex('#F7F5E8')
        
        
    
    