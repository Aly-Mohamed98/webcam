#from filesharer import FileSharer
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser
from filesharer import FileSharer


Builder.load_file('files/frontend.kv')

class CameraScreen(Screen):
    #Controling the camera with options to start, stop and capture
    def start(self):
        #starts the camera and changes the text of the button
        self.ids.camera_switch.opacity = 1
        self.ids.camera_switch.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera_switch.texture = self.ids.camera_switch._camera.texture

    def stop(self):
        #stops the camera and changes the text of the button
        self.ids.camera_switch.play = False
        self.ids.camera_switch.opacity = 0
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera_switch.texture = None

    def capture(self):
        #Taking a photo and saving the image in the specified file path
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f'images/{current_time}.png'
        self.ids.camera_switch.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):
    link_message = "Create a link first!"
    def get_link(self):
        # Accessing the photo filepath and uploads it to the web and provides the user with the link
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath)
        self.url = filesharer.share()
        self.ids.link.text = self.url
    
    def copy_link(self):
        #Copying the link on to the clipboard
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text= self.link_message
    def open_link(self):
        #opening the link on the default browser
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text= self.link_message

class RootWidget(ScreenManager):
    pass
        

class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run() 


