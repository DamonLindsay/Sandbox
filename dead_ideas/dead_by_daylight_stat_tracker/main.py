"""
League of Legends Statistics Tracker
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import json


class HomeScreen(Screen):
    """Home screen with buttons for displaying, adding, and exporting data"""

    def __init__(self, data_manager, **kwargs):
        """Initialize the HomeScreen."""
        super().__init__(**kwargs)
        self.data_manager = data_manager
        self.setup_ui()

        # Create a label for displaying data
        self.data_label = Label(text="")
        self.add_widget(self.data_label)

    def setup_ui(self):
        """Set up the user interface for the home screen."""
        layout = BoxLayout(orientation="vertical")

        # Add widgets for home screen
        label = Label(text="Dead by Daylight Statistics Tracker")

        # Create buttons for actions
        display_button = Button(text="Display Data", on_press=self.display_data)
        add_button = Button(text="Add Data", on_press=self.go_to_input_screen)
        export_button = Button(text="Export Data", on_press=self.export_data)

        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(display_button)
        layout.add_widget(add_button)
        layout.add_widget(export_button)

        # Set the layout as the screen's root widget
        self.add_widget(layout)

    def display_data(self, instance):
        """Display the current data."""
        # Update the text of the existing label
        self.data_label.text = str(self.data_manager.data)

    def go_to_input_screen(self, instance):
        """Switch to the input screen for adding data."""
        self.manager.current = "input"

    def export_data(self, instance):
        """Export the current data to a .txt file."""
        # Placeholder for the export logic
        self.data_manager.export_data_to_txt()
        print("Data exported to .txt file.")


class InputScreen(Screen):
    """Screen for collecting Dead by Daylight statistics."""

    def __init__(self, data_manager, home_screen, **kwargs):
        """Initialize the InputScreen."""
        super().__init__(**kwargs)
        # Add widgets for data input here
        self.match_data = {}
        self.data_manager = data_manager
        self.home_screen = home_screen
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface for data input."""
        layout = BoxLayout(orientation="vertical")

        # Add widgets for data input
        label = Label(text="Enter Match Information:")

        # Create a ScrollView to allow scrolling if the content is too long
        scroll_view = ScrollView()

        # Create a Grid Layout to arrange the input fields in a grid
        grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, row_default_height=40)
        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        layout.add_widget(label)

        # Add input fields for Survivor Information
        self.add_survivor_input_fields(grid_layout)

        # Add input fields for Killer Information
        self.add_killer_input_fields(grid_layout)

        # Add input fields for Map Information
        self.add_map_input_field(grid_layout)

        # Create a horizontal BoxLayout for buttons
        buttons_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=40)

        # Create buttons for actions
        save_button = Button(text="Save", on_press=self.save_data)
        clear_button = Button(text="Clear", on_press=self.clear_fields)
        back_button = Button(text="Back to Home", on_press=self.go_to_home_screen)

        # Add the Save, Clear and Back buttons to the horizontal layout
        buttons_layout.add_widget(save_button)
        buttons_layout.add_widget(clear_button)
        buttons_layout.add_widget(back_button)

        # Add the ScrollView with the GridLayout to the layout
        scroll_view.add_widget(grid_layout)
        layout.add_widget(scroll_view)

        # Add widgets to the layout
        layout.add_widget(buttons_layout)

        # Set the layout as the screen's root widget
        self.add_widget(layout)

    def add_survivor_input_fields(self, grid_layout):
        """Add input fields for Survivor Information."""
        survivor_label = Label(text="Survivor Information:")
        grid_layout.add_widget(survivor_label)

        # Add input fields for each survivor
        for i in range(1, 5):
            survivor_name_input = TextInput(hint_text=f"Survivor {i} Name")
            survivor_perk_input = TextInput(hint_text="Perks (comma-separated)")
            item_input = TextInput(hint_text="Item name")
            survivor_addons_input = TextInput(hint_text="Item Addon Names (comma-separated)")
            survivor_outcome_input = TextInput(hint_text="Killed or Survived")
            survivor_offering_input = TextInput(hint_text="Offering Name")

            grid_layout.add_widget(survivor_name_input)
            grid_layout.add_widget(survivor_perk_input)
            grid_layout.add_widget(item_input)
            grid_layout.add_widget(survivor_addons_input)
            grid_layout.add_widget(survivor_outcome_input)
            grid_layout.add_widget(survivor_offering_input)

    def add_killer_input_fields(self, grid_layout):
        """Add input fields for Killer Information."""
        killer_label = Label(text="Killer Information")
        grid_layout.add_widget(killer_label)

        # Add input fields for the killer
        killer_name_input = TextInput(hint_text="Killer Name")
        killer_addons_input = TextInput(hint_text="Addons Used (comma-separated)")
        killer_offering_input = TextInput(hint_text="Offering Name")

        grid_layout.add_widget(killer_name_input)
        grid_layout.add_widget(killer_addons_input)
        grid_layout.add_widget(killer_offering_input)

    def add_map_input_field(self, grid_layout):
        """Add input field for Map Information."""
        map_label = Label(text="Map Information")
        map_input = TextInput(hint_text="Map Name")
        grid_layout.add_widget(map_label)
        grid_layout.add_widget(map_input)

    def go_to_home_screen(self, instance):
        """Switch to the home screen."""
        self.manager.current = "home"

    def save_data(self, instance):
        """Save Dead by Daylight match data to storage when the Save button is pressed."""
        self.match_data = {
            "survivor_information": {"name": self.survivor_name_input.text,
                                     "perks": self.survivor_perk_input.text,
                                     "item": self.item_input.text,
                                     "item addons": self.survivor_addons_input.text,
                                     "outcome": self.survivor_outcome_input.text,
                                     "offering": self.survivor_offering_input.text},
            "killer_information": {"name": self.killer_name_input.text,
                                   "addons": self.killer_addons_input.text,
                                   "offering": self.killer_offering_input.text},
            "map_information": {"name": self.map_input.text}
        }

        # Save the data using the DataManager
        self.data_manager.save_data(self.match_data)

        # Clear the input fields after saving
        self.clear_fields()

    def clear_fields(self, *args):
        """Clear the input fields."""
        input_fields = [self.survivor_name_input, self.survivor_perk_input,
                        self.item_input, self.survivor_addons_input,
                        self.survivor_outcome_input, self.survivor_offering_input,
                        self.killer_name_input, self.killer_addons_input,
                        self.killer_offering_input, self.map_input]

        for field in input_fields:
            field.text = ""


class FilterScreen(Screen):
    """Screen for filtering and analyzing stored data."""

    def __init__(self, data_manager, home_screen, **kwargs):
        """Initialize the FilterScreen object."""
        self.home_screen = home_screen  # Store home screen as an instance variable
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

    def export_data_to_txt(self, file_path="exported_data.txt"):
        """Export data to a .txt file."""
        try:
            with open(file_path, "w") as txt_file:
                for entry in self.data:
                    txt_file.write(str(entry) + "\n")
                print(f"Data exported to {file_path}.")
        except Exception as e:
            print(f"Error exporting data: {e}")

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
        home_screen = HomeScreen(data_manager=data_manager, name="home")
        input_screen = InputScreen(data_manager=data_manager, home_screen=home_screen, name="input")
        filter_screen = FilterScreen(data_manager=data_manager, home_screen=home_screen,
                                     name="filter")  # Placeholder for future filter screen

        # Create screen manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(input_screen)
        screen_manager.add_widget(filter_screen)

        return screen_manager


if __name__ == '__main__':
    DbdApp().run()
