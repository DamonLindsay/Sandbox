"""
League of Legends Statistics Tracker
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class InputScreen(Screen):
    """Screen for collecting Dead by Daylight statistics."""

    def __init__(self, data_manager, **kwargs):
        """Initialize the InputScreen."""
        super().__init__(**kwargs)
        # Add widgets for data input here
        self.data_manager = data_manager
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface for data input."""
        layout = BoxLayout(orientation="vertical")

        # Add widgets for data input
        label = Label(text="Enter Match Information:")
        survivor_input = TextInput(hint_text="Survivor Names (comma-separated)")
        killer_input = TextInput(hint_text="Killer Name")
        result_input = TextInput(hint_text="Survivor Win / Killer Win")
        save_button = Button(text="Save", on_press=self.save_data)

        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(survivor_input)
        layout.add_widget(killer_input)
        layout.add_widget(result_input)
        layout.add_widget(save_button)

        # Set the layout as the screen's root widget
        self.add_widget(layout)

    def save_data(self, instance):
        """Save Dead by Daylight match data to storage when the Save button is pressed."""
        # Get input data
        survivors = self.ids.survivor_input.text.split(",")
        killer = self.ids.killer_input.text
        match_result = self.ids.result_input.text

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
        self.ids.survivor_input.text = ""
        self.ids.killer_input.text = ""
        self.ids.match_result.text = ""


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

    def __init__(self):
        """Initialize data storage."""
        # Initialize data storage here.
        self.data = []

    def save_data(self, data):
        """Save game data to storage."""
        # Implement data saving logic
        self.data.append(data)
        print(f"Data saved: {data}")

    def filter_data(self, filters):
        """Filter stored data based on specific filters."""
        # Placeholder for filtering logic
        return self.data  # For now, return all data


class DbdApp(App):
    """Main application class for the League of Legends app."""

    def build(self):
        """Build the app and set up screens."""
        data_manager = DataManager()

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
