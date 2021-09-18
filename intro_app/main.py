import wikipedia
import requests   
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


Builder.load_file('files/frontend.kv')

class FirstScreen(Screen):
    
    def search_image(self):
        image_path = 'here.jpg'
        query = self.manager.current_screen.ids.photo.text
        page = wikipedia.page(query)
        image_link = page.images[0]
        req = requests.get(str(image_link))
        
        with open(image_path, "wb") as f:
            f.write(req.content)
        
        self.manager.current_screen.ids.img.source = image_path

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run() 
