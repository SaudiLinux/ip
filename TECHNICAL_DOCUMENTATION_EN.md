# Technical Documentation for Phone Information Tool

This document provides a technical overview of the Phone Information Tool, including its architecture, implementation details, and data flow.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Class Structure](#class-structure)
3. [Data Flow](#data-flow)
4. [Implementation Details](#implementation-details)
5. [Future Improvements](#future-improvements)
6. [Data Flow Diagram](#data-flow-diagram)
7. [File Structure](#file-structure)

## Architecture Overview

The Phone Information Tool is built using a modular architecture that separates the core functionality from the user interfaces. This design allows for easy maintenance, testing, and extension of the tool.

### Core Components

1. **PhoneInfoTool Class**: The main class that handles all phone number analysis functionality.
2. **Command-Line Interface (CLI)**: A text-based interface for interacting with the tool.
3. **Graphical User Interface (GUI)**: A Tkinter-based GUI for a more user-friendly experience.
4. **Export Module**: Functionality for exporting results in various formats.

### Dependencies

The tool relies on several external libraries:

- **phonenumbers**: For phone number validation and basic information extraction
- **pytz**: For timezone handling
- **geopy**: For geolocation services
- **pandas**: For data manipulation and export to CSV/Excel
- **pretty-html-table**: For HTML table generation
- **colored**: For colored terminal output
- **tkinter**: For the graphical user interface

## Class Structure

### PhoneInfoTool Class

The `PhoneInfoTool` class is the core of the application, providing all the functionality for analyzing phone numbers.

#### Properties

- `phone_number`: The phone number being analyzed
- `is_valid`: Boolean indicating if the phone number is valid
- `results`: Dictionary containing all analysis results

#### Methods

##### `__init__(self)`

Initializes the PhoneInfoTool instance with default values.

```python
def __init__(self):
    self.phone_number = None
    self.is_valid = False
    self.results = {}
```

##### `banner(self)`

Displays a banner with tool information.

```python
def banner(self):
    # Display ASCII art banner and tool information
```

##### `validate_phone_number(self, phone_number)`

Validates the provided phone number using the phonenumbers library.

```python
def validate_phone_number(self, phone_number):
    try:
        # Parse and validate the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        self.is_valid = phonenumbers.is_valid_number(parsed_number)
        self.phone_number = phone_number if self.is_valid else None
        return self.is_valid
    except Exception as e:
        self.is_valid = False
        self.phone_number = None
        return False
```

##### `get_basic_info(self)`

Retrieves basic information about the phone number, such as country, carrier, and number type.

```python
def get_basic_info(self):
    if not self.is_valid or not self.phone_number:
        return {}
    
    try:
        parsed_number = phonenumbers.parse(self.phone_number, None)
        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        country = phonenumbers.region_code_for_number(parsed_number)
        carrier = phonenumbers.carrier.name_for_number(parsed_number, 'en')
        number_type = phonenumbers.number_type(parsed_number)
        
        # Map number type to a human-readable string
        number_type_str = {
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Toll Free",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumbers.PhoneNumberType.SHARED_COST: "Shared Cost",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
            phonenumbers.PhoneNumberType.PAGER: "Pager",
            phonenumbers.PhoneNumberType.UAN: "UAN",
            phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
        }.get(number_type, "Unknown")
        
        return {
            "country_code": f"+{country_code}",
            "national_number": national_number,
            "country": country,
            "carrier": carrier if carrier else "Unknown",
            "number_type": number_type_str
        }
    except Exception as e:
        return {}
```

##### `get_geolocation(self)`

Retrieves approximate geolocation information based on the phone number's country and area code.

```python
def get_geolocation(self):
    if not self.is_valid or not self.phone_number:
        return {}
    
    try:
        parsed_number = phonenumbers.parse(self.phone_number, None)
        country = phonenumbers.region_code_for_number(parsed_number)
        
        # This is a simplified implementation
        # In a real-world scenario, you would use a more comprehensive database
        # or API to get more accurate geolocation information
        
        # Get country information using geopy
        geolocator = Nominatim(user_agent="phone_info_tool")
        location = geolocator.geocode(country)
        
        if location:
            return {
                "country": country,
                "latitude": location.latitude,
                "longitude": location.longitude,
                "address": location.address
            }
        else:
            return {
                "country": country,
                "latitude": "Unknown",
                "longitude": "Unknown",
                "address": "Unknown"
            }
    except Exception as e:
        return {}
```

##### `get_timezone_info(self)`

Retrieves timezone information based on the phone number's country.

```python
def get_timezone_info(self):
    if not self.is_valid or not self.phone_number:
        return {}
    
    try:
        parsed_number = phonenumbers.parse(self.phone_number, None)
        country = phonenumbers.region_code_for_number(parsed_number)
        
        # Get timezone information using phonenumbers and pytz
        timezone_name = phonenumbers.timezone.time_zones_for_number(parsed_number)
        
        if timezone_name and len(timezone_name) > 0:
            tz = pytz.timezone(timezone_name[0])
            now = datetime.now(tz)
            offset = now.strftime('%z')
            offset_hours = int(offset[0:3])
            offset_minutes = int(offset[3:5])
            
            return {
                "timezone": timezone_name[0],
                "current_time": now.strftime('%Y-%m-%d %H:%M:%S'),
                "utc_offset": f"{offset_hours}:{offset_minutes:02d}"
            }
        else:
            return {
                "timezone": "Unknown",
                "current_time": "Unknown",
                "utc_offset": "Unknown"
            }
    except Exception as e:
        return {}
```

##### `search_online_databases(self)`

Placeholder method for searching online databases for additional information.

```python
def search_online_databases(self):
    # This is a placeholder for future implementation
    # In a real-world scenario, this would connect to various online databases
    # to gather additional information about the phone number
    
    return {
        "online_presence": "Not implemented in this version",
        "social_media": "Not implemented in this version",
        "data_breaches": "Not implemented in this version"
    }
```

##### `analyze_number(self, phone_number)`

Main method that orchestrates the analysis of a phone number.

```python
def analyze_number(self, phone_number):
    if not self.validate_phone_number(phone_number):
        self.results = {"error": "Invalid phone number"}
        return False
    
    # Gather all information
    basic_info = self.get_basic_info()
    geolocation = self.get_geolocation()
    timezone_info = self.get_timezone_info()
    online_info = self.search_online_databases()
    
    # Combine results
    self.results = {
        "phone_number": self.phone_number,
        "is_valid": self.is_valid,
        "basic_info": basic_info,
        "geolocation": geolocation,
        "timezone_info": timezone_info,
        "online_info": online_info,
        "analysis_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return True
```

##### `display_results(self)`

Displays the analysis results in the terminal with colored output.

```python
def display_results(self):
    if not self.results or "error" in self.results:
        print(colored("No results to display or an error occurred.", "red"))
        return
    
    # Display results in a formatted way with colored output
```

##### `export_results(self, export_format)`

Exports the analysis results in the specified format (JSON, CSV, Excel, HTML).

```python
def export_results(self, export_format):
    if not self.results or "error" in self.results:
        return False, "No results to export or an error occurred."
    
    # Create exports directory if it doesn't exist
    export_dir = "exports"
    os.makedirs(export_dir, exist_ok=True)
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    phone_suffix = self.phone_number.replace("+", "")
    
    try:
        if export_format.lower() == "json":
            # Export to JSON
            filename = f"{export_dir}/phone_info_{phone_suffix}_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=4)
            return True, filename
        
        elif export_format.lower() == "csv":
            # Export to CSV
            filename = f"{export_dir}/phone_info_{phone_suffix}_{timestamp}.csv"
            # Flatten the nested dictionary for CSV export
            flat_data = self._flatten_dict(self.results)
            df = pd.DataFrame([flat_data])
            df.to_csv(filename, index=False)
            return True, filename
        
        elif export_format.lower() == "excel":
            # Export to Excel
            filename = f"{export_dir}/phone_info_{phone_suffix}_{timestamp}.xlsx"
            # Flatten the nested dictionary for Excel export
            flat_data = self._flatten_dict(self.results)
            df = pd.DataFrame([flat_data])
            df.to_excel(filename, index=False)
            return True, filename
        
        elif export_format.lower() == "html":
            # Export to HTML
            filename = f"{export_dir}/phone_info_{phone_suffix}_{timestamp}.html"
            # Flatten the nested dictionary for HTML export
            flat_data = self._flatten_dict(self.results)
            df = pd.DataFrame([flat_data])
            html_table = build_table(df, 'blue_light')
            
            # Create a complete HTML document
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Phone Information: {self.phone_number}</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: #2c3e50; }}
                    .timestamp {{ color: #7f8c8d; font-size: 0.8em; }}
                </style>
            </head>
            <body>
                <h1>Phone Information: {self.phone_number}</h1>
                <p class="timestamp">Generated on: {self.results.get('analysis_time', timestamp)}</p>
                {html_table}
                <p>Generated by Phone Information Tool</p>
            </body>
            </html>
            """
            
            with open(filename, 'w') as f:
                f.write(html_content)
            return True, filename
        
        else:
            return False, "Unsupported export format. Supported formats: JSON, CSV, Excel, HTML"
    
    except Exception as e:
        return False, f"Error exporting results: {str(e)}"
```

## Data Flow

1. **Input**: The user provides a phone number through either the CLI or GUI.
2. **Validation**: The phone number is validated using the phonenumbers library.
3. **Analysis**: If valid, the tool gathers information about the phone number:
   - Basic information (country, carrier, type)
   - Geolocation information
   - Timezone information
   - Placeholder for online database search
4. **Results**: All gathered information is combined into a results dictionary.
5. **Display/Export**: The results are displayed to the user and can be exported in various formats.

## Implementation Details

### Phone Number Handling

The tool uses the `phonenumbers` library, which is a Python port of Google's libphonenumber, to handle phone number validation and basic information extraction. This library provides robust parsing, validation, and formatting of phone numbers for all countries/regions of the world.

```python
import phonenumbers

# Parse a phone number
parsed_number = phonenumbers.parse("+966501234567", None)

# Check if it's valid
is_valid = phonenumbers.is_valid_number(parsed_number)

# Get the country
country = phonenumbers.region_code_for_number(parsed_number)

# Get the carrier
carrier = phonenumbers.carrier.name_for_number(parsed_number, 'en')

# Get the number type
number_type = phonenumbers.number_type(parsed_number)
```

### Geolocation

The tool uses the `geopy` library to obtain geolocation information based on the phone number's country. In a real-world implementation, this would be enhanced with more specific location data based on area codes and other factors.

```python
from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="phone_info_tool")

# Get location information for a country
location = geolocator.geocode("US")

# Extract latitude, longitude, and address
latitude = location.latitude
longitude = location.longitude
address = location.address
```

### Timezone

The tool uses the `phonenumbers.timezone` module and `pytz` to determine the timezone associated with a phone number and provide current time information.

```python
import pytz
from datetime import datetime

# Get timezone for a phone number
timezone_name = phonenumbers.timezone.time_zones_for_number(parsed_number)

# Get current time in that timezone
tz = pytz.timezone(timezone_name[0])
now = datetime.now(tz)

# Format the time and offset
current_time = now.strftime('%Y-%m-%d %H:%M:%S')
offset = now.strftime('%z')
```

### Data Export

The tool supports exporting results in multiple formats using various libraries:

- **JSON**: Using the built-in `json` module
- **CSV/Excel**: Using `pandas`
- **HTML**: Using `pretty-html-table` and custom HTML templates

```python
import json
import pandas as pd
from pretty_html_table import build_table

# Export to JSON
with open("results.json", 'w') as f:
    json.dump(results, f, indent=4)

# Export to CSV/Excel
df = pd.DataFrame([flat_data])
df.to_csv("results.csv", index=False)
df.to_excel("results.xlsx", index=False)

# Export to HTML
html_table = build_table(df, 'blue_light')
with open("results.html", 'w') as f:
    f.write(html_content)
```

## Future Improvements

1. **Enhanced Geolocation**: Implement more precise geolocation based on area codes and carrier information.
2. **Real Online Database Search**: Implement actual connections to online databases and social media platforms.
3. **Advanced Analysis**: Add machine learning algorithms to detect potential spam or fraudulent numbers.
4. **Multi-Number Processing**: Add support for analyzing multiple phone numbers in batch mode.
5. **API Integration**: Create a REST API for integrating the tool with other applications.
6. **Improved GUI**: Enhance the GUI with more features, such as maps for geolocation and historical analysis.
7. **Internationalization**: Add support for multiple languages in the user interface.

## Data Flow Diagram

```
+----------------+     +-------------------+     +--------------------+
|                |     |                   |     |                    |
| User Input     +---->+ Phone Validation  +---->+ Information        |
| (Phone Number) |     | (phonenumbers)    |     | Gathering          |
|                |     |                   |     |                    |
+----------------+     +-------------------+     +--------+---+-------+
                                                          |   |
                                                          |   |
                       +-------------------+              |   |
                       |                   |              |   |
                       | Export Results    |<-------------+   |
                       | (JSON/CSV/Excel/  |                  |
                       |  HTML)            |                  |
                       |                   |                  |
                       +-------------------+                  |
                                                             |
                       +-------------------+                  |
                       |                   |                  |
                       | Display Results   |<-----------------+
                       | (CLI/GUI)         |
                       |                   |
                       +-------------------+
```

## File Structure

```
phone-info-tool/
├── phone_info_tool.py       # Main implementation of the PhoneInfoTool class
├── gui_tool.py              # Graphical user interface implementation
├── requirements.txt         # List of dependencies
├── setup_venv.bat           # Script for setting up the virtual environment
├── run_tool.bat             # Script for running the CLI
├── run_gui.bat              # Script for running the GUI
├── exports/                 # Directory for exported results
└── documentation/           # Documentation files
```

---

This technical documentation provides an overview of the Phone Information Tool's architecture, implementation, and data flow. For more detailed information about specific aspects of the tool, please refer to the other documentation files.

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com