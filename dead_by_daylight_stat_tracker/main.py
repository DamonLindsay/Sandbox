"""
League of Legends Statistics Tracker
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import json


class HomeScreen(Screen):
    """Home screen with buttons for displaying, adding, and exporting data"""


class InputScreen(Screen):
    """Screen for collecting Dead by Daylight statistics."""

    def __init__(self, data_manager, **kwargs):
        """Initialize the InputScreen."""
        super().__init__(**kwargs)
        # Add widgets for data input here
        self.match_result_input = TextInput(hint_text="Survivor Win / Killer Win", multiline=False)
        self.killer_input = TextInput(hint_text="Killer Name", multiline=False)
        self.survivor_input = TextInput(hint_text="Survivor Names (comma-separated)", multiline=False)
        self.data_manager = data_manager
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface for data input."""
        layout = BoxLayout(orientation="vertical")

        # Add widgets for data input
        label = Label(text="Enter Match Information:")

        # Create a horizontal box layout for buttons
        buttons_layout = BoxLayout(orientation="horizontal")

        save_button = Button(text="Save", on_press=self.save_data)
        clear_button = Button(text="Clear", on_press=self.clear_fields)

        # Bind the tab key to the on_tab method for each input field
        self.survivor_input.bind(on_key_down=self.on_tab)
        self.killer_input.bind(on_key_down=self.on_tab)
        self.match_result_input.bind(on_key_down=self.on_tab)

        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(self.survivor_input)
        layout.add_widget(self.killer_input)
        layout.add_widget(self.match_result_input)

        # Add the Save and Clear buttons to the horizontal layout
        buttons_layout.add_widget(save_button)
        buttons_layout.add_widget(clear_button)

        # Add the horizontal layout with buttons to the main layout
        layout.add_widget(buttons_layout)

        # Set the layout as the screen's root widget
        self.add_widget(layout)

    def on_tab(self, instance, key, *args):
        """Handle the Tab key to move focus to the next input field."""
        if key == 9:  # ASCII code for the Tab Key
            # Get the currently focused widget
            focused_widget = self.get_focus_next()

            # If there's a focused widget, move focus to it
            if focused_widget:
                focused_widget.focus = True
            return True  # Consume the Tab key event

    def save_data(self, instance):
        """Save Dead by Daylight match data to storage when the Save button is pressed."""
        # Get input data
        survivors = self.survivor_input.text.split(",")
        killer = self.killer_input.text
        match_result = self.match_result_input.text

        # Validate input data (add more validation as needed)

        # Create a data dictionary
        match_data = {
            "survivors": survivors,
            "killer": killer,
            "match result": match_result
        }

        # Save the data using the DataManager
        self.data_manager.save_data(match_data)

        # Clear the input fields after saving
        self.clear_fields()

    def clear_fields(self, *args):
        """Clear the input fields."""
        self.survivor_input.text = ""
        self.killer_input.text = ""
        self.match_result_input.text = ""


class FilterScreen(Screen):
    """Screen for filtering and analyzing stored data."""

    def __init__(self, data_manager, **kwargs):
        """Initialize the FilterScreen object."""
        super().__init__(**kwargs)
        self.data_manager = data_manager
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface for data filtering and display."""
        layout = BoxLayout(orientation="vertical")

        # Add widgets for filtering
        label = Label(text="Filter and View Data:")
        filter_button = Button(text="Filter", on_press=self.filter_data)
        data_label = Label(text="Filtered Data Will Appear Here")

        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(filter_button)
        layout.add_widget(data_label)

        # Set te layout as the screen's root widget
        self.add_widget(layout)

    def filter_data(self, instance):
        """Filter Dead by Daylight match data and display the results."""
        # Placeholder for filtering logic
        filtered_data = self.data_manager.filter_data({})

        # Display filtered data (placeholder)
        data_label = self.ids.data_label
        data_label.text = "Filtered Data:\n"
        for data in filtered_data:
            data_label.text += f"{data}\n"


class DataManager:
    """Class responsible for managing data storage and retrieval."""

    def __init__(self, filename="dbd_data.txt"):
        """Initialize data storage."""
        # Initialize data storage here.
        self.filename = filename
        self.data = []
        self.load_data()

    def save_data(self, data):
        """Save game data to storage."""
        # Implement data saving logic
        self.data.append(data)
        self.save_to_file()

    def load_data(self):
        """Load data from file."""
        try:
            with open(self.filename, "r") as output_file:
                self.data = json.load(output_file)
        except FileNotFoundError:
            print("No previous data found.  Starting with an empty dataset.")

    def save_to_file(self):
        """Save data to file."""
        with open(self.filename, "w") as input_file:
            json.dump(self.data, input_file)
            print("Data saved to file.")

    def filter_data(self, filters):
        """Filter stored data based on specific filters."""
        # Placeholder for filtering logic
        return self.data  # For now, return all data


class DbdApp(App):
    """Main application class for the League of Legends app."""

    def build(self):
        """Build the app and set up screens."""
        data_manager = DataManager(filename="dbd_data.txt")

        # Create screens with the DataManager instance
        input_screen = InputScreen(data_manager=data_manager, name="input")
        filter_screen = FilterScreen(data_manager=data_manager, name="filter")  # Placeholder for future filter screen

        # Create screen manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(input_screen)
        screen_manager.add_widget(filter_screen)

        return screen_manager


if __name__ == '__main__':
    DbdApp().run()
