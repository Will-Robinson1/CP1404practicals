
from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ Converts miles to kilometres """
    def build(self):
        """ build the Kivy app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

MilesConverterApp().run()