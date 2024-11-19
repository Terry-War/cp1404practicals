"""CP1404 programming 2 - prac 08 - Dynamic Labels
Estimated: 60 minutes
Start: 15:40
Finish: 16:15
Total: 35 minutes
Not to sure about this code and how it creates dynamic labels. Just pinched alot of it from the demos.
I may not be understanding what it means for dynamic labels.
As I tried resizing the GUI after running it the names remain the same.
The only thing I wanted to add to this is a background colour for the text box rather than the default black box.
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

COLOUR = (1, 0, 0, 1)  # Red text color (RGBA)

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        self.list_of_names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')  # Load the KV file
        self.create_widgets()  # Create widgets (Labels) dynamically
        return self.root

    def create_widgets(self):
        """Create labels from list and add them to the GUI."""
        for name in self.list_of_names:
            label = Label(text=name, color=COLOUR)  # Set text color
            self.root.ids.entries_box.add_widget(label)


DynamicLabelsApp().run()