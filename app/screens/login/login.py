from pathlib import Path
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty, StringProperty


KV_PATH = Path(__file__).with_name("login.kv")
Builder.load_file(str(KV_PATH))



class LoginScreen(Screen):
    
    # super-simple auth state (replace with real service later)
    is_authenticated = BooleanProperty(False)
    user = StringProperty("")
    
    
    
    def login(self, username: str, password: str) -> bool:
        
        # TODO: replace with real auth (API call, DB, etc.)
        ok = bool(username.strip()) and bool(password.strip())
        self.is_authenticated = ok
        
        if ok:
            self.user = username.strip()
            self.manager.current = "home"
            
        return ok

    
    
    # def logout(self):
    #     self.is_authenticated = False
    #     self.user = ""
    #     self.root.current = "login"
    
    
    
    def try_login(self, username: str, password: str):
        
        ok = self.login(username, password)
        if not ok:
            # Show a friendly error via id defined in KV
            self.ids.error_lbl.text = "Invalid credentials. Try again."
        else:
            self.ids.error_lbl.text = ""