from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

NEW_COLOUR = (1, 0, 0, 1)

class DynamicLabelsApp(App):
    """Kivy application that displays a dynamic list of labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # 1. The list of names (data/model)
        self.name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fiona']

    def build(self):
        """Build the Kivy GUI."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.name_list:
            # Create a new Label widget
            temp_label = Label(text=name, size_hint_y=None, height=60)
            main_layout = self.root.ids.main
            # Add the new label to the main_layout (the vertical BoxLayout)
            main_layout.add_widget(temp_label)



if __name__ == '__main__':
    DynamicLabelsApp().run()