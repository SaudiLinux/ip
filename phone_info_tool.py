#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phone Information Gathering Tool
Developed by: Saudi Linux
Email: SaudiLinuxy7@gmail.com

This tool collects information about phone numbers including carrier, location,
time zone, and other metadata from various databases.
"""

import sys
import os
import re
import json
import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import requests
import pandas as pd
from datetime import datetime
import pytz
# استخدام رموز ANSI مباشرة بدلاً من مكتبة colored
from geopy.geocoders import Nominatim
# تجاوز استخدام مكتبة pretty-html-table
# from pretty_html_table import build_table

# ANSI color codes for terminal output
COLORS = {
    'green': '\033[32m',
    'blue': '\033[34m',
    'red': '\033[31m',
    'yellow': '\033[33m',
    'cyan': '\033[36m',
    'magenta': '\033[35m',
    'reset': '\033[0m',
    'bold': '\033[1m'
}


class PhoneInfoTool:
    """Main class for the Phone Information Gathering Tool"""
    
    def __init__(self):
        """Initialize the PhoneInfoTool"""
        self.results = {}
        self.phone_number = None
        self.parsed_number = None
        self.geolocator = Nominatim(user_agent="phone_info_tool")
        self.banner()
    
    def banner(self):
        """Display the tool banner"""
        banner_text = f"""
{COLORS['cyan']}{COLORS['bold']}╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  {COLORS['green']}Phone Information Gathering Tool{COLORS['cyan']}                     ║
║  {COLORS['blue']}Developed by: Saudi Linux{COLORS['cyan']}                           ║
║  {COLORS['yellow']}Email: SaudiLinuxy7@gmail.com{COLORS['cyan']}                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{COLORS['reset']}
        """
        print(banner_text)
    
    def validate_phone_number(self, phone_number):
        """Validate the phone number format"""
        try:
            # Remove any non-digit characters except the + sign
            cleaned_number = re.sub(r'[^\d+]', '', phone_number)
            
            # If the number doesn't start with +, assume it's missing the country code
            if not cleaned_number.startswith('+'):
                print(f"{COLORS['yellow']}[!] No country code provided. Assuming +1 (US/Canada).{COLORS['reset']}")
                cleaned_number = '+1' + cleaned_number
            
            parsed_number = phonenumbers.parse(cleaned_number, None)
            
            if not phonenumbers.is_valid_number(parsed_number):
                print(f"{COLORS['red']}[!] Invalid phone number format.{COLORS['reset']}")
                return None
            
            return parsed_number
        
        except Exception as e:
            print(f"{COLORS['red']}[!] Error validating phone number: {str(e)}{COLORS['reset']}")
            return None
    
    def get_basic_info(self):
        """Get basic information about the phone number"""
        try:
            country_code = self.parsed_number.country_code
            national_number = self.parsed_number.national_number
            country = geocoder.description_for_number(self.parsed_number, 'en')
            carrier_name = carrier.name_for_number(self.parsed_number, 'en')
            time_zones = timezone.time_zones_for_number(self.parsed_number)
            
            # Format the phone number in international format
            formatted_number = phonenumbers.format_number(
                self.parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
            
            # Check if the number is valid
            is_valid = phonenumbers.is_valid_number(self.parsed_number)
            
            # Check if the number is possible
            is_possible = phonenumbers.is_possible_number(self.parsed_number)
            
            # Get the number type (mobile, landline, etc.)
            number_type = phonenumbers.number_type(self.parsed_number)
            number_type_dict = {
                0: "FIXED_LINE",
                1: "MOBILE",
                2: "FIXED_LINE_OR_MOBILE",
                3: "TOLL_FREE",
                4: "PREMIUM_RATE",
                5: "SHARED_COST",
                6: "VOIP",
                7: "PERSONAL_NUMBER",
                8: "PAGER",
                9: "UAN",
                10: "UNKNOWN",
                27: "EMERGENCY",
                28: "VOICEMAIL",
                29: "SHORT_CODE",
                30: "STANDARD_RATE"
            }
            number_type_str = number_type_dict.get(number_type, "UNKNOWN")
            
            self.results['basic_info'] = {
                'formatted_number': formatted_number,
                'country_code': country_code,
                'national_number': national_number,
                'country': country if country else "Unknown",
                'carrier': carrier_name if carrier_name else "Unknown",
                'time_zones': list(time_zones) if time_zones else ["Unknown"],
                'is_valid': is_valid,
                'is_possible': is_possible,
                'number_type': number_type_str
            }
            
            return True
        
        except Exception as e:
            print(f"{COLORS['red']}[!] Error getting basic info: {str(e)}{COLORS['reset']}")
            return False
    
    def get_geolocation(self):
        """Get geolocation information for the phone number"""
        try:
            country = geocoder.description_for_number(self.parsed_number, 'en')
            if not country:
                country = "Unknown"
            
            # Try to get more detailed location information
            region = geocoder.description_for_number(self.parsed_number, 'en', region=True)
            if not region:
                region = "Unknown"
            
            # Get coordinates using geopy if country is known
            coordinates = {"latitude": "Unknown", "longitude": "Unknown"}
            if country != "Unknown":
                try:
                    location = self.geolocator.geocode(country)
                    if location:
                        coordinates = {
                            "latitude": location.latitude,
                            "longitude": location.longitude
                        }
                except Exception:
                    pass
            
            self.results['geolocation'] = {
                'country': country,
                'region': region,
                'coordinates': coordinates
            }
            
            return True
        
        except Exception as e:
            print(f"{COLORS['red']}[!] Error getting geolocation: {str(e)}{COLORS['reset']}")
            return False
    
    def get_timezone_info(self):
        """Get timezone information for the phone number"""
        try:
            time_zones = timezone.time_zones_for_number(self.parsed_number)
            
            tz_info = []
            for tz in time_zones:
                tz_info.append({
                    'name': tz,
                    'current_time': datetime.now().astimezone(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S %Z%z')
                })
            
            if not tz_info:
                tz_info = [{"name": "Unknown", "current_time": "Unknown"}]
            
            self.results['timezone_info'] = tz_info
            
            return True
        
        except Exception as e:
            print(f"{COLORS['red']}[!] Error getting timezone info: {str(e)}{COLORS['reset']}")
            return False
    
    def search_online_databases(self):
        """Search online databases for additional information"""
        try:
            # This is a placeholder for actual API calls to online databases
            # In a real implementation, you would integrate with various APIs
            # that provide phone number lookup services
            
            # For demonstration purposes, we'll just add some placeholder data
            self.results['online_databases'] = {
                'spam_score': "Low",  # This would come from a real spam database
                'reported_count': 0,   # Number of times reported as spam
                'last_reported': "Never",
                'tags': ["Not in database"],
                'note': "This is a placeholder. In a real implementation, this would connect to actual phone number databases."
            }
            
            return True
        
        except Exception as e:
            print(f"{COLORS['red']}[!] Error searching online databases: {str(e)}{COLORS['reset']}")
            return False
    
    def analyze_number(self, phone_number):
        """Analyze the provided phone number and gather all available information"""
        print(f"{COLORS['blue']}[*] Analyzing phone number: {phone_number}{COLORS['reset']}")
        
        self.phone_number = phone_number
        self.parsed_number = self.validate_phone_number(phone_number)
        
        if not self.parsed_number:
            return False
        
        print(f"{COLORS['blue']}[*] Gathering basic information...{COLORS['reset']}")
        self.get_basic_info()
        
        print(f"{COLORS['blue']}[*] Gathering geolocation information...{COLORS['reset']}")
        self.get_geolocation()
        
        print(f"{COLORS['blue']}[*] Gathering timezone information...{COLORS['reset']}")
        self.get_timezone_info()
        
        print(f"{COLORS['blue']}[*] Searching online databases...{COLORS['reset']}")
        self.search_online_databases()
        
        return True
    
    def display_results(self):
        """Display the gathered information in a formatted way"""
        if not self.results:
            print(f"{COLORS['red']}[!] No results to display.{COLORS['reset']}")
            return
        
        print(f"\n{COLORS['green']}{COLORS['bold']}===== PHONE NUMBER ANALYSIS RESULTS ====={COLORS['reset']}\n")
        
        # Display basic information
        if 'basic_info' in self.results:
            basic = self.results['basic_info']
            print(f"{COLORS['cyan']}{COLORS['bold']}Basic Information:{COLORS['reset']}")
            print(f"  Phone Number: {basic['formatted_number']}")
            print(f"  Country Code: +{basic['country_code']}")
            print(f"  National Number: {basic['national_number']}")
            print(f"  Country: {basic['country']}")
            print(f"  Carrier: {basic['carrier']}")
            print(f"  Number Type: {basic['number_type']}")
            print(f"  Valid Number: {'Yes' if basic['is_valid'] else 'No'}")
            print(f"  Possible Number: {'Yes' if basic['is_possible'] else 'No'}")
            print()
        
        # Display geolocation information
        if 'geolocation' in self.results:
            geo = self.results['geolocation']
            print(f"{COLORS['cyan']}{COLORS['bold']}Geolocation Information:{COLORS['reset']}")
            print(f"  Country: {geo['country']}")
            print(f"  Region: {geo['region']}")
            print(f"  Coordinates: Latitude {geo['coordinates']['latitude']}, Longitude {geo['coordinates']['longitude']}")
            print()
        
        # Display timezone information
        if 'timezone_info' in self.results:
            print(f"{COLORS['cyan']}{COLORS['bold']}Timezone Information:{COLORS['reset']}")
            for tz in self.results['timezone_info']:
                print(f"  Timezone: {tz['name']}")
                print(f"  Current Time: {tz['current_time']}")
            print()
        
        # Display online database results
        if 'online_databases' in self.results:
            db = self.results['online_databases']
            print(f"{COLORS['cyan']}{COLORS['bold']}Online Database Information:{COLORS['reset']}")
            print(f"  Spam Score: {db['spam_score']}")
            print(f"  Times Reported: {db['reported_count']}")
            print(f"  Last Reported: {db['last_reported']}")
            print(f"  Tags: {', '.join(db['tags'])}")
            print(f"  Note: {db['note']}")
            print()
    
    def export_results(self, format_type='json', filename=None):
        """Export the results to a file in the specified format"""
        if not self.results:
            print(f"{COLORS['red']}[!] No results to export.{COLORS['reset']}")
            return False
        
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            phone_part = re.sub(r'[^\d]', '', self.phone_number)[-4:]
            filename = f"phone_info_{phone_part}_{timestamp}"
        
        try:
            if format_type.lower() == 'json':
                with open(f"{filename}.json", 'w', encoding='utf-8') as f:
                    json.dump(self.results, f, indent=4)
                output_file = f"{filename}.json"
            
            elif format_type.lower() == 'csv':
                # Convert nested dict to flat structure for CSV
                flat_data = {}
                for category, data in self.results.items():
                    if isinstance(data, list):
                        for i, item in enumerate(data):
                            for key, value in item.items():
                                flat_data[f"{category}_{i+1}_{key}"] = value
                    elif isinstance(data, dict):
                        for key, value in data.items():
                            if isinstance(value, dict):
                                for subkey, subvalue in value.items():
                                    flat_data[f"{category}_{key}_{subkey}"] = subvalue
                            else:
                                flat_data[f"{category}_{key}"] = value
                
                df = pd.DataFrame([flat_data])
                df.to_csv(f"{filename}.csv", index=False)
                output_file = f"{filename}.csv"
            
            elif format_type.lower() == 'excel':
                # Similar to CSV but for Excel
                flat_data = {}
                for category, data in self.results.items():
                    if isinstance(data, list):
                        for i, item in enumerate(data):
                            for key, value in item.items():
                                flat_data[f"{category}_{i+1}_{key}"] = value
                    elif isinstance(data, dict):
                        for key, value in data.items():
                            if isinstance(value, dict):
                                for subkey, subvalue in value.items():
                                    flat_data[f"{category}_{key}_{subkey}"] = subvalue
                            else:
                                flat_data[f"{category}_{key}"] = value
                
                df = pd.DataFrame([flat_data])
                df.to_excel(f"{filename}.xlsx", index=False)
                output_file = f"{filename}.xlsx"
            
            elif format_type.lower() == 'html':
                # Create a simple HTML report
                flat_data = {}
                for category, data in self.results.items():
                    if isinstance(data, list):
                        for i, item in enumerate(data):
                            for key, value in item.items():
                                flat_data[f"{category}_{i+1}_{key}"] = value
                    elif isinstance(data, dict):
                        for key, value in data.items():
                            if isinstance(value, dict):
                                for subkey, subvalue in value.items():
                                    flat_data[f"{category}_{key}_{subkey}"] = subvalue
                            else:
                                flat_data[f"{category}_{key}"] = value
                
                df = pd.DataFrame([flat_data])
                # Replace build_table with pandas' to_html method with some basic styling
                html_table = df.to_html(classes='table table-striped table-hover', border=0)
                
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Phone Information Report</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; }}
                        h1 {{ color: #2c3e50; }}
                        .timestamp {{ color: #7f8c8d; font-size: 0.8em; }}
                        .footer {{ margin-top: 30px; font-size: 0.8em; color: #7f8c8d; }}
                    </style>
                </head>
                <body>
                    <h1>Phone Information Report</h1>
                    <p>Phone Number: {self.results.get('basic_info', {}).get('formatted_number', 'Unknown')}</p>
                    <p class="timestamp">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    {html_table}
                    <div class="footer">
                        <p>Generated by Phone Information Gathering Tool</p>
                        <p>Developed by: Saudi Linux | Email: SaudiLinuxy7@gmail.com</p>
                    </div>
                </body>
                </html>
                """
                
                with open(f"{filename}.html", 'w', encoding='utf-8') as f:
                    f.write(html_content)
                output_file = f"{filename}.html"
            
            else:
                print(f"{COLORS['red']}[!] Unsupported export format: {format_type}{COLORS['reset']}")
                return False
            
            print(f"{COLORS['green']}[+] Results exported to {output_file}{COLORS['reset']}")
            return True
        
        except Exception as e:
            print(f"{COLORS['red']}[!] Error exporting results: {str(e)}{COLORS['reset']}")
            return False


def main():
    """Main function to run the tool"""
    tool = PhoneInfoTool()
    
    if len(sys.argv) > 1:
        # If phone number is provided as command line argument
        phone_number = sys.argv[1]
    else:
        # Otherwise, prompt the user for input
        phone_number = input(f"{COLORS['yellow']}Enter phone number (with country code, e.g., +1234567890): {COLORS['reset']}")
    
    if tool.analyze_number(phone_number):
        tool.display_results()
        
        # Ask if user wants to export the results
        export_choice = input(f"\n{COLORS['yellow']}Do you want to export the results? (y/n): {COLORS['reset']}")
        if export_choice.lower() in ['y', 'yes']:
            format_choice = input(f"{COLORS['yellow']}Export format (json/csv/excel/html) [default: json]: {COLORS['reset']}")
            if not format_choice:
                format_choice = 'json'
            
            custom_filename = input(f"{COLORS['yellow']}Custom filename (leave empty for auto-generated): {COLORS['reset']}")
            
            tool.export_results(format_choice, custom_filename)
    
    print(f"\n{COLORS['green']}Thank you for using the Phone Information Gathering Tool!{COLORS['reset']}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{COLORS['red']}[!] Program interrupted by user.{COLORS['reset']}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{COLORS['red']}[!] An unexpected error occurred: {str(e)}{COLORS['reset']}")
        sys.exit(1)