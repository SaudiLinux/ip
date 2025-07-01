# Phone Information Tool

A simple tool for collecting and analyzing phone number information, developed by Saudi Linux.

## Prerequisites

- Python 3.9 or newer
- Required Python libraries (listed in requirements.txt)

## Installation

### Automatic Method (Windows Users)

1. Run the `setup_venv.bat` file by double-clicking it.
2. The file will automatically create a virtual environment and install all requirements.

### Manual Method

1. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```
     source venv/bin/activate
     ```

3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

## How to Use

### Command Line Interface

1. On Windows, run the `run_tool.bat` file by double-clicking it.
2. Or run the tool directly from the command line:
   ```
   python3 phone_info_tool.py +966501234567
   ```

### Graphical User Interface

1. On Windows, run the `run_gui.bat` file by double-clicking it.
2. Or run the GUI directly from the command line:
   ```
   python3 gui_tool.py
   ```

3. Enter the phone number in the designated field.
4. Click on the "Analyze Number" button.
5. Results will appear in the results area.
6. You can export the results in different formats (JSON, CSV, Excel, HTML).

## Features

- Phone number validation
- Basic information retrieval (country code, country name, carrier)
- Geolocation information retrieval
- Timezone information retrieval
- Export results in multiple formats
- Command line and graphical user interfaces

## Documentation

For more information, please refer to the following files:

- `INSTALLATION_GUIDE_EN.md`: Detailed installation guide
- `TECHNICAL_DOCUMENTATION_EN.md`: Technical documentation
- `API_DOCUMENTATION_EN.md`: API documentation
- `GUI_DOCUMENTATION_EN.md`: GUI documentation
- `VISUAL_GUIDE_EN.md`: Visual usage guide
- `FAQ_EN.md`: Frequently asked questions

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Developer

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com

## Disclaimer

This tool was developed for educational and research purposes only. It should be used ethically and legally. The developer is not responsible for any inappropriate or illegal use of the tool.
