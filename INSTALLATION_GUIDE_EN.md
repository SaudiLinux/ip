# Installation Guide for Phone Information Tool

This document provides detailed instructions for installing and setting up the Phone Information Tool on your system.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Automatic Installation](#automatic-installation)
3. [Manual Installation](#manual-installation)
4. [Project Structure](#project-structure)
5. [Running the Tool](#running-the-tool)
6. [Configuration and Customization](#configuration-and-customization)
7. [Troubleshooting](#troubleshooting)
8. [Uninstallation](#uninstallation)
9. [Updates](#updates)
10. [Technical Support](#technical-support)

## Prerequisites

Before installing the Phone Information Tool, ensure your system meets the following requirements:

### Software Requirements

- **Python**: Version 3.6 or higher
  - To check your Python version, open a command prompt and type: `python --version`
  - If Python is not installed or the version is below 3.6, download and install the latest version from [python.org](https://www.python.org/downloads/)

- **pip**: Python package manager (usually included with Python)
  - To check if pip is installed, open a command prompt and type: `pip --version`
  - If pip is not installed, follow the instructions at [pip.pypa.io](https://pip.pypa.io/en/stable/installation/)

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Disk Space**: At least 100 MB of free disk space
- **Memory**: At least 512 MB of RAM
- **Internet Connection**: Required for retrieving geolocation and timezone information

### Additional Requirements for GUI

- **Tkinter**: Python's standard GUI package (usually included with Python)
  - On Windows and macOS, Tkinter is typically included with Python
  - On Linux, you may need to install it separately (e.g., `sudo apt-get install python3-tk` on Ubuntu)

## Automatic Installation

The easiest way to install the Phone Information Tool is to use the provided batch file (Windows only).

### Steps for Automatic Installation

1. **Download the Project Files**
   - Ensure all project files are in a directory on your computer

2. **Run the Setup Script**
   - Navigate to the project directory
   - Double-click the `setup_venv.bat` file
   - This script will:
     - Check if Python is installed
     - Create a virtual environment if it doesn't exist
     - Activate the virtual environment
     - Install all required dependencies from `requirements.txt`

3. **Verify Installation**
   - The script will display a success message when the installation is complete
   - If any errors occur, refer to the [Troubleshooting](#troubleshooting) section

## Manual Installation

If you prefer to install the tool manually or if you're using macOS or Linux, follow these steps:

### Steps for Manual Installation

1. **Download the Project Files**
   - Ensure all project files are in a directory on your computer

2. **Open a Terminal or Command Prompt**
   - Navigate to the project directory

3. **Create a Virtual Environment**
   - Windows:
     ```
     python -m venv venv
     ```
   - macOS/Linux:
     ```
     python3 -m venv venv
     ```

4. **Activate the Virtual Environment**
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. **Install Dependencies**
   - With the virtual environment activated, run:
     ```
     pip install -r requirements.txt
     ```

6. **Verify Installation**
   - Run the following command to check if all dependencies are installed correctly:
     ```
     pip list
     ```
   - You should see all the required packages listed

## Project Structure

After installation, your project directory should have the following structure:

```
phone-info-tool/
├── venv/                      # Virtual environment (created during installation)
├── exports/                    # Directory for exported results
├── phone_info_tool.py         # Main command-line tool
├── gui_tool.py                # Graphical user interface
├── requirements.txt           # List of dependencies
├── setup_venv.bat             # Automatic installation script (Windows)
├── run_tool.bat               # Script to run the command-line tool (Windows)
├── run_gui.bat                # Script to run the GUI (Windows)
├── README.md                  # Project overview (Arabic)
├── README_EN.md               # Project overview (English)
├── API_DOCUMENTATION.md       # API documentation
├── TECHNICAL_DOCUMENTATION.md # Technical documentation
├── GUI_DOCUMENTATION.md       # GUI documentation (Arabic)
├── INSTALLATION_GUIDE.md      # Installation guide (Arabic)
├── INSTALLATION_GUIDE_EN.md   # Installation guide (English)
├── VISUAL_GUIDE.md            # Visual guide (Arabic)
├── VISUAL_GUIDE_EN.md         # Visual guide (English)
├── FAQ.md                     # Frequently asked questions (Arabic)
├── FAQ_EN.md                  # Frequently asked questions (English)
├── SECURITY_PRIVACY.md        # Security and privacy information
├── CONTRIBUTING.md            # Contribution guidelines (Arabic)
├── CONTRIBUTING_EN.md         # Contribution guidelines (English)
├── ROADMAP.md                 # Future development plans (Arabic)
├── CHANGELOG.md               # Version history
└── LICENSE                    # License information
```

## Running the Tool

After installation, you can run the Phone Information Tool in two ways:

### Command-Line Interface (CLI)

#### Using the Batch File (Windows)

1. Navigate to the project directory
2. Double-click the `run_tool.bat` file
3. Follow the on-screen instructions to analyze phone numbers

#### Using Python Directly

1. Open a terminal or command prompt
2. Navigate to the project directory
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Run the tool:
   - `python phone_info_tool.py`
5. Follow the on-screen instructions to analyze phone numbers

### Graphical User Interface (GUI)

#### Using the Batch File (Windows)

1. Navigate to the project directory
2. Double-click the `run_gui.bat` file
3. Use the GUI to analyze phone numbers

#### Using Python Directly

1. Open a terminal or command prompt
2. Navigate to the project directory
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Run the GUI:
   - `python gui_tool.py`
5. Use the GUI to analyze phone numbers

## Configuration and Customization

The Phone Information Tool can be customized in several ways:

### Export Directory

By default, all exported files are saved in the `exports` directory within the project folder. You can change this by modifying the `export_results` method in the `PhoneInfoTool` class in `phone_info_tool.py`.

```python
def export_results(self, export_format):
    # Change the export directory here
    export_dir = "custom/export/path"
    # Rest of the method...
```

### Export Formats

The tool currently supports the following export formats:
- JSON
- CSV
- Excel
- HTML

To add a new export format, you would need to modify the `export_results` method in the `PhoneInfoTool` class.

### GUI Themes

The GUI supports multiple themes that can be selected from the dropdown menu. To add new themes, modify the `set_theme` method in the `PhoneInfoGUI` class in `gui_tool.py`.

## Troubleshooting

### Common Installation Issues

#### Python Not Found

**Problem**: The installation script reports that Python is not found or not in the PATH.

**Solution**:
1. Ensure Python is installed correctly
2. Add Python to your system's PATH environment variable
3. Try specifying the full path to Python when creating the virtual environment

#### Permission Errors

**Problem**: You encounter permission errors when installing dependencies.

**Solution**:
1. Run the command prompt or terminal as administrator (Windows) or use sudo (macOS/Linux)
2. Check if you have write permissions for the project directory

#### Dependency Installation Failures

**Problem**: One or more dependencies fail to install.

**Solution**:
1. Check your internet connection
2. Update pip: `python -m pip install --upgrade pip`
3. Try installing the problematic dependency individually
4. Check if the dependency requires additional system libraries

### Common Runtime Issues

#### Virtual Environment Not Activated

**Problem**: You get an error about missing modules when running the tool.

**Solution**:
1. Ensure the virtual environment is activated before running the tool
2. If using the batch files, check if they correctly activate the virtual environment

#### GUI Does Not Start

**Problem**: The GUI fails to start or crashes immediately.

**Solution**:
1. Ensure Tkinter is installed with your Python installation
2. Check the console output for error messages
3. Try running the GUI from the command line to see detailed error messages

#### Phone Number Analysis Errors

**Problem**: The tool fails to analyze certain phone numbers.

**Solution**:
1. Ensure the phone number is in the correct format (with country code)
2. Check your internet connection for geolocation and timezone lookups
3. Verify that the phone number is valid and in use

## Uninstallation

To uninstall the Phone Information Tool:

1. Delete the project directory and all its contents
2. The virtual environment and all installed dependencies will be removed

Note: Since the tool runs in a virtual environment, it doesn't install anything system-wide, making uninstallation simple.

## Updates

To update the Phone Information Tool to a newer version:

1. Download the latest version of the project files
2. Replace the old files with the new ones, keeping your `exports` directory if needed
3. Run the installation process again to update dependencies

## Technical Support

If you encounter issues not covered in this guide, or if you need additional assistance, please contact the developer:

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com

---

Thank you for installing the Phone Information Tool. For more information about using the tool, please refer to the README_EN.md and other documentation files.