# API Documentation for Phone Information Tool

This document provides detailed information on how to use the Phone Information Tool as a library in your own Python projects.

## Table of Contents

1. [Basic Usage](#basic-usage)
2. [Class and Function Details](#class-and-function-details)
3. [Data Structure](#data-structure)
4. [Advanced Examples](#advanced-examples)
5. [Developer Notes](#developer-notes)

## Basic Usage

To use the Phone Information Tool in your Python project, you need to import the `PhoneInfoTool` class and create an instance of it.

```python
# Import the PhoneInfoTool class
from phone_info_tool import PhoneInfoTool

# Create an instance of the PhoneInfoTool
phone_tool = PhoneInfoTool()

# Analyze a phone number
phone_number = "+966501234567"
if phone_tool.analyze_number(phone_number):
    # Get the results
    results = phone_tool.results
    print(f"Country: {results['basic_info']['country']}")
    print(f"Carrier: {results['basic_info']['carrier']}")
    
    # Export the results to a file
    success, file_path = phone_tool.export_results("json")
    if success:
        print(f"Results exported to {file_path}")
```

## Class and Function Details

### PhoneInfoTool Class

The `PhoneInfoTool` class is the main class that provides all the functionality for analyzing phone numbers.

#### Constructor

```python
def __init__(self)
```

Initializes a new instance of the `PhoneInfoTool` class with default values.

**Parameters**: None

**Returns**: A new `PhoneInfoTool` instance

#### Methods

##### validate_phone_number

```python
def validate_phone_number(self, phone_number)
```

Validates the provided phone number using the phonenumbers library.

**Parameters**:
- `phone_number` (str): The phone number to validate, preferably in international format with a plus sign (e.g., "+966501234567")

**Returns**: `bool` - True if the phone number is valid, False otherwise

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.validate_phone_number("+966501234567"):
    print("Valid phone number")
else:
    print("Invalid phone number")
```

##### get_basic_info

```python
def get_basic_info(self)
```

Retrieves basic information about the phone number, such as country, carrier, and number type.

**Parameters**: None (uses the phone number set by `validate_phone_number`)

**Returns**: `dict` - A dictionary containing basic information about the phone number

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.validate_phone_number("+966501234567"):
    basic_info = phone_tool.get_basic_info()
    print(f"Country: {basic_info['country']}")
    print(f"Carrier: {basic_info['carrier']}")
```

##### get_geolocation

```python
def get_geolocation(self)
```

Retrieves approximate geolocation information based on the phone number's country and area code.

**Parameters**: None (uses the phone number set by `validate_phone_number`)

**Returns**: `dict` - A dictionary containing geolocation information

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.validate_phone_number("+966501234567"):
    geolocation = phone_tool.get_geolocation()
    print(f"Country: {geolocation['country']}")
    print(f"Latitude: {geolocation['latitude']}")
    print(f"Longitude: {geolocation['longitude']}")
```

##### get_timezone_info

```python
def get_timezone_info(self)
```

Retrieves timezone information based on the phone number's country.

**Parameters**: None (uses the phone number set by `validate_phone_number`)

**Returns**: `dict` - A dictionary containing timezone information

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.validate_phone_number("+966501234567"):
    timezone_info = phone_tool.get_timezone_info()
    print(f"Timezone: {timezone_info['timezone']}")
    print(f"Current Time: {timezone_info['current_time']}")
    print(f"UTC Offset: {timezone_info['utc_offset']}")
```

##### search_online_databases

```python
def search_online_databases(self)
```

Placeholder method for searching online databases for additional information.

**Parameters**: None (uses the phone number set by `validate_phone_number`)

**Returns**: `dict` - A dictionary containing placeholder information for online database searches

**Note**: This method is a placeholder in the current version and does not perform actual online searches.

##### analyze_number

```python
def analyze_number(self, phone_number)
```

Main method that orchestrates the analysis of a phone number. This method calls all the other information gathering methods and combines the results.

**Parameters**:
- `phone_number` (str): The phone number to analyze, preferably in international format with a plus sign (e.g., "+966501234567")

**Returns**: `bool` - True if the analysis was successful, False otherwise

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.analyze_number("+966501234567"):
    results = phone_tool.results
    print(f"Analysis completed for {results['phone_number']}")
```

##### display_results

```python
def display_results(self)
```

Displays the analysis results in the terminal with colored output.

**Parameters**: None (uses the results from `analyze_number`)

**Returns**: None

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.analyze_number("+966501234567"):
    phone_tool.display_results()
```

##### export_results

```python
def export_results(self, export_format)
```

Exports the analysis results in the specified format.

**Parameters**:
- `export_format` (str): The format to export the results in. Supported formats: "json", "csv", "excel", "html"

**Returns**: `tuple` - (success, message)
- `success` (bool): True if the export was successful, False otherwise
- `message` (str): The path to the exported file if successful, or an error message if not

**Example**:
```python
phone_tool = PhoneInfoTool()
if phone_tool.analyze_number("+966501234567"):
    success, file_path = phone_tool.export_results("json")
    if success:
        print(f"Results exported to {file_path}")
    else:
        print(f"Export failed: {file_path}")
```

## Data Structure

The `results` property of the `PhoneInfoTool` class contains a dictionary with the following structure:

```python
{
    "phone_number": "+966501234567",
    "is_valid": True,
    "basic_info": {
        "country_code": "+966",
        "national_number": 501234567,
        "country": "SA",
        "carrier": "STC",
        "number_type": "Mobile"
    },
    "geolocation": {
        "country": "SA",
        "latitude": 24.7136,
        "longitude": 46.6753,
        "address": "Saudi Arabia"
    },
    "timezone_info": {
        "timezone": "Asia/Riyadh",
        "current_time": "2023-06-01 12:34:56",
        "utc_offset": "+3:00"
    },
    "online_info": {
        "online_presence": "Not implemented in this version",
        "social_media": "Not implemented in this version",
        "data_breaches": "Not implemented in this version"
    },
    "analysis_time": "2023-06-01 12:34:56"
}
```

## Advanced Examples

### Script Usage

Here's an example of how to use the Phone Information Tool in a script that analyzes multiple phone numbers:

```python
from phone_info_tool import PhoneInfoTool
import json

def analyze_multiple_numbers(phone_numbers, export_format="json"):
    results = []
    phone_tool = PhoneInfoTool()
    
    for phone_number in phone_numbers:
        print(f"Analyzing {phone_number}...")
        if phone_tool.analyze_number(phone_number):
            results.append(phone_tool.results)
            success, file_path = phone_tool.export_results(export_format)
            if success:
                print(f"Results exported to {file_path}")
        else:
            print(f"Failed to analyze {phone_number}")
    
    return results

# List of phone numbers to analyze
phone_numbers = [
    "+966501234567",
    "+12125551234",
    "+447911123456"
]

# Analyze all phone numbers and export results to JSON
all_results = analyze_multiple_numbers(phone_numbers, "json")

# Save combined results to a single file
with open("all_results.json", "w") as f:
    json.dump(all_results, f, indent=4)

print(f"All results saved to all_results.json")
```

### GUI Integration

Here's an example of how to integrate the Phone Information Tool with a simple Tkinter GUI:

```python
import tkinter as tk
from tkinter import ttk, messagebox
from phone_info_tool import PhoneInfoTool

class SimplePhoneInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Information Tool")
        self.root.geometry("600x400")
        
        self.phone_tool = PhoneInfoTool()
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Phone number input
        ttk.Label(self.root, text="Enter Phone Number:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = ttk.Entry(self.root, width=30)
        self.phone_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Analyze button
        ttk.Button(self.root, text="Analyze", command=self.analyze_number).grid(row=0, column=2, padx=10, pady=10)
        
        # Results display
        ttk.Label(self.root, text="Results:").grid(row=1, column=0, padx=10, pady=5, sticky="nw")
        self.results_text = tk.Text(self.root, width=70, height=15)
        self.results_text.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
        
        # Export options
        ttk.Label(self.root, text="Export Format:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.export_format = tk.StringVar()
        export_combo = ttk.Combobox(self.root, textvariable=self.export_format, values=["JSON", "CSV", "Excel", "HTML"])
        export_combo.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        export_combo.current(0)  # Default to JSON
        
        # Export button
        ttk.Button(self.root, text="Export Results", command=self.export_results).grid(row=3, column=2, padx=10, pady=10)
    
    def analyze_number(self):
        phone_number = self.phone_entry.get().strip()
        if not phone_number:
            messagebox.showerror("Error", "Please enter a phone number")
            return
        
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        
        # Analyze the phone number
        if self.phone_tool.analyze_number(phone_number):
            # Display results
            results = self.phone_tool.results
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
            
            # Analysis Time
            self.results_text.insert(tk.END, f"\nAnalysis Time: {results['analysis_time']}\n")
        else:
            self.results_text.insert(tk.END, "Invalid phone number or analysis failed.")
    
    def export_results(self):
        if not hasattr(self.phone_tool, 'results') or not self.phone_tool.results:
            messagebox.showerror("Error", "No results to export. Please analyze a phone number first.")
            return
        
        export_format = self.export_format.get().lower()
        success, message = self.phone_tool.export_results(export_format)
        
        if success:
            messagebox.showinfo("Export Successful", f"Results exported to {message}")
        else:
            messagebox.showerror("Export Failed", message)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePhoneInfoGUI(root)
    root.mainloop()
```

## Developer Notes

### Dependencies

The Phone Information Tool relies on several external libraries. Make sure to include these dependencies in your project:

```
phonenumbers>=8.12.0
pytz>=2021.1
requests>=2.25.1
geopy>=2.2.0
pretty-html-table>=0.9.0
openpyxl>=3.0.7
pandas>=1.3.0
colored>=1.4.3
```

### Error Handling

The Phone Information Tool includes basic error handling for common issues such as invalid phone numbers and network errors. However, you may want to implement additional error handling in your application, especially for production use.

### Performance Considerations

- The geolocation and timezone lookups require internet connectivity and may take some time to complete.
- For batch processing of multiple phone numbers, consider implementing threading or asynchronous processing to improve performance.

### Customization

You can customize the Phone Information Tool by extending the `PhoneInfoTool` class or modifying the existing methods. For example, you could add support for additional export formats or implement actual online database searches.

```python
from phone_info_tool import PhoneInfoTool

class CustomPhoneInfoTool(PhoneInfoTool):
    def __init__(self):
        super().__init__()
    
    # Override the search_online_databases method to implement actual searches
    def search_online_databases(self):
        if not self.is_valid or not self.phone_number:
            return {}
        
        try:
            # Implement your custom online database search here
            # This is just a placeholder
            return {
                "online_presence": "Found on 3 websites",
                "social_media": "Found on 2 social media platforms",
                "data_breaches": "No data breaches found"
            }
        except Exception as e:
            return {}
    
    # Add a new method for additional functionality
    def check_spam_likelihood(self):
        if not self.is_valid or not self.phone_number:
            return {"spam_likelihood": "Unknown"}
        
        # Implement spam detection logic here
        # This is just a placeholder
        return {"spam_likelihood": "Low"}
```

---

This API documentation provides detailed information on how to use the Phone Information Tool as a library in your own Python projects. For more information about the tool's implementation details, please refer to the Technical Documentation.

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com