# Visual Guide for Phone Information Tool

This document provides a step-by-step visual guide for using the Phone Information Tool.

## Table of Contents

1. [Installation](#installation)
2. [Command-Line Interface Usage](#command-line-interface-usage)
3. [Graphical User Interface Usage](#graphical-user-interface-usage)
4. [Exporting Results](#exporting-results)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Installation

### Automatic Installation

1. Download the project files to your computer
2. Locate the `setup_venv.bat` file in the project folder

   ![Setup File Location](images/setup_file_location.png)
   *(Image placeholder: Screenshot showing the setup_venv.bat file in File Explorer)*

3. Double-click the `setup_venv.bat` file to run it
4. Wait for the installation to complete

   ![Installation Process](images/installation_process.png)
   *(Image placeholder: Screenshot showing the installation process in the command prompt)*

5. When you see "Installation complete", the tool is ready to use

### Manual Installation

1. Open a command prompt in the project directory
2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

   ![Manual Installation](images/manual_installation.png)
   *(Image placeholder: Screenshot showing the manual installation steps in the command prompt)*

## Command-Line Interface Usage

### Starting the CLI

1. Locate the `run_tool.bat` file in the project folder

   ![Run Tool File Location](images/run_tool_location.png)
   *(Image placeholder: Screenshot showing the run_tool.bat file in File Explorer)*

2. Double-click the `run_tool.bat` file to run it
3. The command-line interface will open

   ![CLI Startup](images/cli_startup.png)
   *(Image placeholder: Screenshot showing the CLI startup with banner)*

### Analyzing a Phone Number

1. Enter a phone number when prompted (include the country code with a plus sign)

   ![Enter Phone Number](images/enter_phone_number.png)
   *(Image placeholder: Screenshot showing the phone number input prompt)*

2. The tool will analyze the phone number and display the results

   ![Analysis Results](images/analysis_results.png)
   *(Image placeholder: Screenshot showing the analysis results in the CLI)*

3. You will be prompted to export the results or analyze another number

## Graphical User Interface Usage

### Starting the GUI

1. Locate the `run_gui.bat` file in the project folder

   ![Run GUI File Location](images/run_gui_location.png)
   *(Image placeholder: Screenshot showing the run_gui.bat file in File Explorer)*

2. Double-click the `run_gui.bat` file to run it
3. The graphical user interface will open

   ![GUI Startup](images/gui_startup.png)
   *(Image placeholder: Screenshot showing the GUI window)*

### Analyzing a Phone Number in the GUI

1. Enter a phone number in the input field (include the country code with a plus sign)

   ![GUI Enter Phone Number](images/gui_enter_phone_number.png)
   *(Image placeholder: Screenshot showing the phone number input field in the GUI)*

2. Click the "Analyze" button
3. The results will be displayed in the results area

   ![GUI Analysis Results](images/gui_analysis_results.png)
   *(Image placeholder: Screenshot showing the analysis results in the GUI)*

### Using GUI Features

1. **Theme Selection**: Use the theme dropdown to change the appearance of the GUI

   ![Theme Selection](images/theme_selection.png)
   *(Image placeholder: Screenshot showing the theme dropdown menu)*

2. **Help Button**: Click the "Help" button to view information about using the tool

   ![Help Dialog](images/help_dialog.png)
   *(Image placeholder: Screenshot showing the help dialog)*

3. **About Button**: Click the "About" button to view information about the developer

   ![About Dialog](images/about_dialog.png)
   *(Image placeholder: Screenshot showing the about dialog)*

## Exporting Results

### Exporting from the CLI

1. After analyzing a phone number, you will be prompted to export the results
2. Enter the number corresponding to your desired export format (1-4)

   ![CLI Export Options](images/cli_export_options.png)
   *(Image placeholder: Screenshot showing the export options in the CLI)*

3. The file will be saved in the "exports" folder with a timestamp in the filename

   ![CLI Export Complete](images/cli_export_complete.png)
   *(Image placeholder: Screenshot showing the export completion message)*

### Exporting from the GUI

1. After analyzing a phone number, select the desired export format from the dropdown menu

   ![GUI Export Format Selection](images/gui_export_format.png)
   *(Image placeholder: Screenshot showing the export format dropdown)*

2. Click the "Export Results" button
3. A message will appear confirming that the results have been exported

   ![GUI Export Complete](images/gui_export_complete.png)
   *(Image placeholder: Screenshot showing the export completion message in the GUI)*

4. The file will be saved in the "exports" folder with a timestamp in the filename

### Viewing Exported Files

1. Navigate to the "exports" folder in the project directory

   ![Exports Folder](images/exports_folder.png)
   *(Image placeholder: Screenshot showing the exports folder in File Explorer)*

2. Open the exported file with the appropriate application:
   - JSON files: Any text editor or JSON viewer
   - CSV files: Excel, Google Sheets, or any spreadsheet application
   - Excel files: Microsoft Excel or compatible spreadsheet application
   - HTML files: Any web browser

   ![Exported File Example](images/exported_file_example.png)
   *(Image placeholder: Screenshot showing an example of an exported file)*

## Troubleshooting Common Issues

### Installation Issues

**Problem**: The installation fails with an error message

![Installation Error](images/installation_error.png)
*(Image placeholder: Screenshot showing an installation error)*

**Solution**:
1. Ensure you have Python 3.6 or higher installed
2. Check your internet connection
3. Try running the installation as administrator
4. Try the manual installation method

### Phone Number Validation Issues

**Problem**: The tool says the phone number is invalid

![Invalid Phone Number](images/invalid_phone_number.png)
*(Image placeholder: Screenshot showing an invalid phone number error)*

**Solution**:
1. Ensure you've included the country code with a plus sign (e.g., +966501234567)
2. Check that the phone number follows the correct format for its country
3. Try removing any spaces, dashes, or parentheses from the number

### GUI Not Starting

**Problem**: The GUI doesn't open when you run `run_gui.bat`

**Solution**:
1. Try running `gui_tool.py` directly from the command line with the virtual environment activated
2. Check if Python is installed with tkinter support
3. Reinstall the dependencies using `pip install -r requirements.txt`

### Export Errors

**Problem**: The export fails with an error message

![Export Error](images/export_error.png)
*(Image placeholder: Screenshot showing an export error)*

**Solution**:
1. Ensure the "exports" folder exists in the project directory
2. Check if you have write permissions for the folder
3. Close any open files that might be locked by other applications
4. Try a different export format

---

**Note**: The images in this guide are placeholders. In a complete installation, these would be replaced with actual screenshots of the application.

**Developer**: Saudi Linux  
**Email**: SaudiLinuxy7@gmail.com