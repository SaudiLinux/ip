# Phone Information Tool

A comprehensive tool for gathering and analyzing phone number information, including country data, carrier information, geolocation, timezone, and more.

## Developer Information

- **Developer**: Saudi Linux
- **Email**: SaudiLinuxy7@gmail.com

## Features

- **Phone Number Validation**: Verify if a phone number is valid and properly formatted
- **Basic Information**: Retrieve country code, country name, carrier, and number type
- **Geolocation**: Get approximate location information based on the phone number
- **Timezone Information**: Determine the timezone associated with the phone number
- **Online Database Search**: Placeholder for searching phone numbers in online databases
- **Multiple Export Formats**: Export results in JSON, CSV, Excel, or HTML formats
- **Command Line Interface**: Easy-to-use CLI for quick analysis
- **Graphical User Interface**: User-friendly GUI for interactive usage

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Automatic Installation (Recommended)

1. Clone or download this repository
2. Run `setup_venv.bat` by double-clicking it
3. Wait for the installation to complete

### Manual Installation

1. Clone or download this repository
2. Open a command prompt or terminal
3. Navigate to the project directory
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
6. Install the requirements: `pip install -r requirements.txt`

## Usage

### Command Line Interface

1. Run `run_tool.bat` or execute `python phone_info_tool.py` with the virtual environment activated
2. Enter a phone number with country code (e.g., +966501234567)
3. View the analysis results
4. Choose to export the results if desired

### Graphical User Interface

1. Run `run_gui.bat` or execute `python gui_tool.py` with the virtual environment activated
2. Enter a phone number with country code in the input field
3. Click "Analyze Number" to process the number
4. View the results in the results area
5. Export the results in your preferred format if desired

## Export Formats

The tool supports exporting results in the following formats:

- **JSON**: Structured data format
- **CSV**: Comma-separated values for spreadsheet applications
- **Excel**: Microsoft Excel spreadsheet
- **HTML**: Formatted web page for viewing in browsers

## Project Structure

```
ip/
├── phone_info_tool.py     # Main tool file
├── gui_tool.py            # Graphical user interface
├── test_tool.py           # Tool tests
├── requirements.txt       # Project dependencies
├── README.md              # Arabic readme file
├── README_EN.md           # English readme file
├── API_DOCUMENTATION.md   # API documentation
├── TECHNICAL_DOCUMENTATION.md # Technical documentation
├── GUI_DOCUMENTATION.md   # GUI documentation
├── TESTING_DOCUMENTATION.md # Testing documentation
├── SECURITY_PRIVACY.md    # Security and privacy documentation
├── FAQ.md                 # Frequently asked questions (Arabic)
├── ROADMAP.md             # Future roadmap (Arabic)
├── CONTRIBUTING.md        # Contribution guidelines (Arabic)
├── CONTRIBUTING_EN.md     # Contribution guidelines (English)
├── CHANGELOG.md           # Version history
├── VISUAL_GUIDE.md        # Visual guide
├── INSTALLATION_GUIDE.md  # Installation guide
├── LICENSE                # MIT License
├── setup_venv.bat         # Virtual environment setup script
├── run_tool.bat           # CLI tool runner script
└── run_gui.bat            # GUI tool runner script
```

## Documentation

The project includes comprehensive documentation:

- **API Documentation**: How to use the tool as a library in other projects
- **Technical Documentation**: Technical overview of the tool's architecture and implementation
- **GUI Documentation**: Documentation for the graphical user interface
- **Testing Documentation**: Information about testing strategies and procedures
- **Security & Privacy**: Security considerations and privacy policy
- **Installation Guide**: Detailed installation instructions
- **Visual Guide**: Step-by-step visual guide for using the tool

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING_EN.md](CONTRIBUTING_EN.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is provided for informational and educational purposes only. The accuracy of the information provided depends on the data available from public sources and may not be complete or up-to-date. The developer is not responsible for any misuse of this tool or for any damages resulting from its use.

The tool does not store or log any phone numbers or results. All processing is done locally on your machine.

---

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com