# GUI Documentation for Phone Information Tool

This document provides technical documentation for the Tkinter-based graphical user interface (GUI) of the Phone Information Tool.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Code Structure](#code-structure)
4. [Data Flow](#data-flow)
5. [Implementation Details](#implementation-details)
6. [Customization](#customization)
7. [Best Practices](#best-practices)
8. [Testing](#testing)

## Overview

The GUI for the Phone Information Tool is built using Tkinter, Python's standard GUI toolkit. It provides a user-friendly interface for analyzing phone numbers, viewing results, and exporting data in various formats.

The GUI includes the following features:
- Input field for entering phone numbers
- Analysis button to process the phone number
- Results display area
- Export functionality with format selection
- Theme selection for customizing the appearance
- Help and About dialogs for user assistance

## Requirements

To run the GUI, the following requirements must be met:

- Python 3.6 or higher
- Tkinter (usually included with Python)
- All dependencies listed in `requirements.txt`
- The `PhoneInfoTool` class from `phone_info_tool.py`

## Code Structure

The GUI is implemented in the `gui_tool.py` file, which contains the `PhoneInfoGUI` class. This class encapsulates all the functionality needed for the graphical interface.

### PhoneInfoGUI Class

#### Properties

- `root`: The main Tkinter window
- `phone_tool`: An instance of the `PhoneInfoTool` class
- `theme_var`: StringVar for storing the selected theme
- `export_format_var`: StringVar for storing the selected export format
- `status_var`: StringVar for displaying status messages
- Various UI elements (frames, labels, buttons, etc.)

#### Methods

##### `__init__(self, root)`

Initializes the GUI with the given Tkinter root window.

```python
def __init__(self, root):
    self.root = root
    self.root.title("Phone Information Tool")
    self.root.geometry("800x600")
    self.root.minsize(800, 600)
    
    # Initialize the PhoneInfoTool
    self.phone_tool = PhoneInfoTool()
    
    # Create StringVars for dynamic content
    self.theme_var = tk.StringVar(value="Default")
    self.export_format_var = tk.StringVar(value="JSON")
    self.status_var = tk.StringVar(value="Ready")
    
    # Set up the UI
    self.create_widgets()
    self.set_theme("Default")
```

##### `set_theme(self, theme_name)`

Sets the color scheme for the GUI based on the selected theme.

```python
def set_theme(self, theme_name):
    # Define color schemes for different themes
    themes = {
        "Default": {
            "bg": "#f0f0f0",
            "fg": "#000000",
            "button_bg": "#e0e0e0",
            "button_fg": "#000000",
            "highlight_bg": "#0078d7",
            "highlight_fg": "#ffffff",
            "text_bg": "#ffffff",
            "text_fg": "#000000"
        },
        "Dark": {
            "bg": "#2d2d2d",
            "fg": "#ffffff",
            "button_bg": "#444444",
            "button_fg": "#ffffff",
            "highlight_bg": "#0078d7",
            "highlight_fg": "#ffffff",
            "text_bg": "#3d3d3d",
            "text_fg": "#ffffff"
        },
        "Blue": {
            "bg": "#e6f0ff",
            "fg": "#000000",
            "button_bg": "#0078d7",
            "button_fg": "#ffffff",
            "highlight_bg": "#005999",
            "highlight_fg": "#ffffff",
            "text_bg": "#ffffff",
            "text_fg": "#000000"
        }
    }
    
    # Get the selected theme or default to "Default"
    theme = themes.get(theme_name, themes["Default"])
    
    # Apply the theme to all widgets
    self.root.configure(bg=theme["bg"])
    # Apply to other widgets...
```

##### `create_widgets(self)`

Creates and arranges all the UI elements in the window.

```python
def create_widgets(self):
    # Create main frames
    self.header_frame = tk.Frame(self.root)
    self.content_frame = tk.Frame(self.root)
    self.status_frame = tk.Frame(self.root)
    
    # Arrange frames
    self.header_frame.pack(fill="x", padx=10, pady=10)
    self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)
    self.status_frame.pack(fill="x", padx=10, pady=5)
    
    # Create header elements
    self.title_label = tk.Label(self.header_frame, text="Phone Information Tool", font=("Arial", 16, "bold"))
    self.title_label.pack(side="left")
    
    # Create theme selection
    self.theme_frame = tk.Frame(self.header_frame)
    self.theme_frame.pack(side="right")
    
    self.theme_label = tk.Label(self.theme_frame, text="Theme:")
    self.theme_label.pack(side="left", padx=5)
    
    self.theme_menu = ttk.Combobox(self.theme_frame, textvariable=self.theme_var, values=["Default", "Dark", "Blue"])
    self.theme_menu.pack(side="left")
    self.theme_menu.bind("<<ComboboxSelected>>", lambda e: self.set_theme(self.theme_var.get()))
    
    # Create input area
    self.input_frame = tk.Frame(self.content_frame)
    self.input_frame.pack(fill="x", pady=10)
    
    self.phone_label = tk.Label(self.input_frame, text="Enter Phone Number:")
    self.phone_label.pack(side="left", padx=5)
    
    self.phone_entry = tk.Entry(self.input_frame, width=30)
    self.phone_entry.pack(side="left", padx=5)
    
    self.analyze_button = tk.Button(self.input_frame, text="Analyze", command=self.analyze_number)
    self.analyze_button.pack(side="left", padx=5)
    
    # Create results area
    self.results_frame = tk.Frame(self.content_frame)
    self.results_frame.pack(fill="both", expand=True, pady=10)
    
    self.results_label = tk.Label(self.results_frame, text="Results:")
    self.results_label.pack(anchor="w")
    
    self.results_text = tk.Text(self.results_frame, wrap="word", height=20)
    self.results_text.pack(fill="both", expand=True, side="left")
    
    self.results_scrollbar = tk.Scrollbar(self.results_frame, command=self.results_text.yview)
    self.results_scrollbar.pack(fill="y", side="right")
    self.results_text.config(yscrollcommand=self.results_scrollbar.set)
    
    # Create export area
    self.export_frame = tk.Frame(self.content_frame)
    self.export_frame.pack(fill="x", pady=10)
    
    self.export_label = tk.Label(self.export_frame, text="Export Format:")
    self.export_label.pack(side="left", padx=5)
    
    self.export_menu = ttk.Combobox(self.export_frame, textvariable=self.export_format_var, values=["JSON", "CSV", "Excel", "HTML"])
    self.export_menu.pack(side="left", padx=5)
    
    self.export_button = tk.Button(self.export_frame, text="Export Results", command=self.export_results)
    self.export_button.pack(side="left", padx=5)
    
    # Create help and about buttons
    self.help_about_frame = tk.Frame(self.content_frame)
    self.help_about_frame.pack(fill="x", pady=10)
    
    self.help_button = tk.Button(self.help_about_frame, text="Help", command=self.show_help)
    self.help_button.pack(side="left", padx=5)
    
    self.about_button = tk.Button(self.help_about_frame, text="About", command=self.show_about)
    self.about_button.pack(side="left", padx=5)
    
    # Create status bar
    self.status_label = tk.Label(self.status_frame, textvariable=self.status_var, anchor="w")
    self.status_label.pack(fill="x")
```

##### `analyze_number(self)`

Analyzes the phone number entered by the user and displays the results.

```python
def analyze_number(self):
    # Get the phone number from the entry field
    phone_number = self.phone_entry.get().strip()
    
    if not phone_number:
        messagebox.showerror("Error", "Please enter a phone number")
        return
    
    # Update status
    self.status_var.set("Analyzing...")
    self.root.update_idletasks()
    
    # Clear previous results
    self.results_text.delete(1.0, tk.END)
    
    # Use threading to prevent GUI freezing during analysis
    def analyze_thread():
        try:
            # Analyze the phone number
            success = self.phone_tool.analyze_number(phone_number)
            
            # Update the GUI with results (must be done in the main thread)
            self.root.after(0, self.update_results, success)
        except Exception as e:
            # Handle any exceptions
            self.root.after(0, lambda: self.handle_error(str(e)))
    
    # Start the analysis in a separate thread
    threading.Thread(target=analyze_thread).start()
```

##### `update_results(self, success)`

Updates the results display with the analysis results.

```python
def update_results(self, success):
    if success:
        # Get the results
        results = self.phone_tool.results
        
        # Display the results in the text widget
        self.results_text.insert(tk.END, f"Phone Number: {results['phone_number']}\n")
        self.results_text.insert(tk.END, f"Valid: {results['is_valid']}\n\n")
        
        # Basic Info
        self.results_text.insert(tk.END, "Basic Information:\n")
        for key, value in results['basic_info'].items():
            self.results_text.insert(tk.END, f"  {key.replace('_', ' ').title()}: {value}\n")
        
        # Geolocation
        self.results_text.insert(tk.END, "\nGeolocation:\n")
        for key, value in results['geolocation'].items():
            self.results_text.insert(tk.END, f"  {key.replace('_', ' ').title()}: {value}\n")
        
        # Timezone
        self.results_text.insert(tk.END, "\nTimezone Information:\n")
        for key, value in results['timezone_info'].items():
            self.results_text.insert(tk.END, f"  {key.replace('_', ' ').title()}: {value}\n")
        
        # Online Info (placeholder)
        self.results_text.insert(tk.END, "\nOnline Information:\n")
        for key, value in results['online_info'].items():
            self.results_text.insert(tk.END, f"  {key.replace('_', ' ').title()}: {value}\n")
        
        # Analysis Time
        self.results_text.insert(tk.END, f"\nAnalysis Time: {results['analysis_time']}\n")
        
        # Update status
        self.status_var.set("Analysis complete")
    else:
        # Display error message
        self.results_text.insert(tk.END, "Error: Invalid phone number or analysis failed.")
        self.status_var.set("Analysis failed")
```

##### `export_results(self)`

Exports the analysis results in the selected format.

```python
def export_results(self):
    # Check if there are results to export
    if not hasattr(self.phone_tool, 'results') or not self.phone_tool.results:
        messagebox.showerror("Error", "No results to export. Please analyze a phone number first.")
        return
    
    # Get the selected export format
    export_format = self.export_format_var.get().lower()
    
    # Update status
    self.status_var.set(f"Exporting to {export_format}...")
    self.root.update_idletasks()
    
    # Use threading to prevent GUI freezing during export
    def export_thread():
        try:
            # Export the results
            success, message = self.phone_tool.export_results(export_format)
            
            # Update the GUI with export result (must be done in the main thread)
            self.root.after(0, self.update_export_status, success, message)
        except Exception as e:
            # Handle any exceptions
            self.root.after(0, lambda: self.handle_error(str(e)))
    
    # Start the export in a separate thread
    threading.Thread(target=export_thread).start()
```

##### `show_help(self)`

Displays a help dialog with information about using the tool.

```python
def show_help(self):
    help_text = """
    Phone Information Tool - Help
    
    This tool allows you to analyze phone numbers and retrieve information about them.
    
    How to use:
    1. Enter a phone number in the input field (include the country code with a plus sign, e.g., +966501234567)
    2. Click the "Analyze" button to process the phone number
    3. View the results in the results area
    4. Select an export format and click "Export Results" to save the results
    
    Supported export formats:
    - JSON: JavaScript Object Notation format
    - CSV: Comma-Separated Values format
    - Excel: Microsoft Excel spreadsheet
    - HTML: Web page format
    
    Themes:
    You can change the appearance of the application by selecting a different theme from the dropdown menu.
    
    For more information, please refer to the documentation or contact the developer.
    """
    
    messagebox.showinfo("Help", help_text)
```

##### `show_about(self)`

Displays an about dialog with information about the developer.

```python
def show_about(self):
    about_text = """
    Phone Information Tool
    
    A tool for gathering and analyzing information about phone numbers.
    
    Features:
    - Phone number validation
    - Basic information retrieval (country, carrier, type)
    - Geolocation information
    - Timezone information
    - Multiple export formats
    
    Developer: Saudi Linux
    Email: SaudiLinuxy7@gmail.com
    
    This tool is provided under the MIT License.
    """
    
    messagebox.showinfo("About", about_text)
```

## Data Flow

The data flow in the GUI follows these steps:

1. **Input**: The user enters a phone number in the input field and clicks the "Analyze" button.
2. **Processing**: The GUI creates a thread to run the analysis using the `PhoneInfoTool` class.
3. **Results Display**: The analysis results are displayed in the results text area.
4. **Export**: If the user selects an export format and clicks "Export Results", the results are exported to a file.

## Implementation Details

### Threading

The GUI uses threading to prevent freezing during time-consuming operations such as phone number analysis and result export. This is implemented in the `analyze_number` and `export_results` methods.

```python
# Example of threading in the analyze_number method
def analyze_thread():
    try:
        # Analyze the phone number (potentially time-consuming)
        success = self.phone_tool.analyze_number(phone_number)
        
        # Update the GUI with results (must be done in the main thread)
        self.root.after(0, self.update_results, success)
    except Exception as e:
        # Handle any exceptions
        self.root.after(0, lambda: self.handle_error(str(e)))

# Start the analysis in a separate thread
threading.Thread(target=analyze_thread).start()
```

### Error Handling

The GUI includes error handling to manage exceptions that may occur during phone number analysis or result export. This is implemented in the `handle_error` method.

```python
def handle_error(self, error_message):
    # Display error message in the results area
    self.results_text.delete(1.0, tk.END)
    self.results_text.insert(tk.END, f"Error: {error_message}")
    
    # Update status
    self.status_var.set("Error occurred")
    
    # Show error dialog
    messagebox.showerror("Error", f"An error occurred: {error_message}")
```

### Export Options

The GUI provides multiple export formats (JSON, CSV, Excel, HTML) through a dropdown menu. The selected format is passed to the `export_results` method of the `PhoneInfoTool` class.

```python
# Get the selected export format
export_format = self.export_format_var.get().lower()

# Export the results
success, message = self.phone_tool.export_results(export_format)
```

## Customization

The GUI can be customized in several ways:

### Themes

The GUI supports multiple themes that can be selected from the dropdown menu. Themes are defined in the `set_theme` method and include color schemes for various UI elements.

```python
# Define color schemes for different themes
themes = {
    "Default": {
        "bg": "#f0f0f0",
        "fg": "#000000",
        # Other color definitions...
    },
    "Dark": {
        "bg": "#2d2d2d",
        "fg": "#ffffff",
        # Other color definitions...
    },
    # Other themes...
}
```

### Adding New Themes

To add a new theme, you can extend the `themes` dictionary in the `set_theme` method:

```python
# Add a new theme
themes["Green"] = {
    "bg": "#e6ffe6",
    "fg": "#000000",
    "button_bg": "#4caf50",
    "button_fg": "#ffffff",
    "highlight_bg": "#388e3c",
    "highlight_fg": "#ffffff",
    "text_bg": "#ffffff",
    "text_fg": "#000000"
}
```

### Layout Customization

The layout of the GUI can be customized by modifying the `create_widgets` method. You can add, remove, or rearrange UI elements as needed.

## Best Practices

When working with the GUI code, follow these best practices:

1. **Use Threading**: Always use threading for time-consuming operations to prevent the GUI from freezing.
2. **Handle Errors**: Implement proper error handling to manage exceptions and provide feedback to the user.
3. **Update Status**: Keep the user informed about the current status of operations through the status bar.
4. **Validate Input**: Validate user input before processing to prevent errors and improve user experience.
5. **Separate Logic**: Keep the GUI code separate from the business logic (implemented in the `PhoneInfoTool` class).

## Testing

To test the GUI, you can use the following approaches:

### Manual Testing

1. Run the GUI and test all features manually
2. Verify that the GUI responds correctly to valid and invalid inputs
3. Test all export formats
4. Test all themes
5. Verify that error handling works correctly

### Automated Testing

For automated testing of the GUI, you can use libraries such as `pytest-tk` or `unittest` with mocking:

```python
import unittest
from unittest.mock import MagicMock
import tkinter as tk
from gui_tool import PhoneInfoGUI

class TestPhoneInfoGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.gui = PhoneInfoGUI(self.root)
        self.gui.phone_tool = MagicMock()
    
    def test_analyze_number_valid(self):
        # Set up mock
        self.gui.phone_tool.analyze_number.return_value = True
        self.gui.phone_tool.results = {
            "phone_number": "+966501234567",
            "is_valid": True,
            "basic_info": {"country": "SA"},
            "geolocation": {"country": "SA"},
            "timezone_info": {"timezone": "Asia/Riyadh"},
            "online_info": {"online_presence": "Not implemented"},
            "analysis_time": "2023-06-01 12:34:56"
        }
        
        # Set input and trigger analysis
        self.gui.phone_entry.insert(0, "+966501234567")
        self.gui.analyze_number()
        
        # Verify that the phone_tool.analyze_number method was called
        self.gui.phone_tool.analyze_number.assert_called_once_with("+966501234567")
        
        # Clean up
        self.root.destroy()
    
    # Add more tests...

if __name__ == "__main__":
    unittest.main()
```

---

This documentation provides a comprehensive overview of the GUI implementation for the Phone Information Tool. For more information about the core functionality, please refer to the Technical Documentation.

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com