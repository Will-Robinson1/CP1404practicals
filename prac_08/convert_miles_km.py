
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

    def handle_calculate(self):
        """ handle calculation, output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """ handle up/down button press """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()




MilesConverterApp().run()