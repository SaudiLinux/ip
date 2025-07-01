#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for Phone Information Gathering Tool
Developed by: Saudi Linux
Email: SaudiLinuxy7@gmail.com
"""

import sys
from phone_info_tool import PhoneInfoTool

# Test phone numbers from different countries
TEST_NUMBERS = [
    "+1 (555) 123-4567",  # US
    "+44 20 7946 0958",   # UK
    "+966 50 123 4567",   # Saudi Arabia
    "+81 3-1234-5678",    # Japan
    "+61 2 1234 5678",    # Australia
    "12345"                # Invalid number
]

def test_phone_info_tool():
    """Test the PhoneInfoTool with various phone numbers"""
    print("\n===== TESTING PHONE INFORMATION GATHERING TOOL =====\n")
    
    tool = PhoneInfoTool()
    
    for i, number in enumerate(TEST_NUMBERS, 1):
        print(f"\n----- Test {i}: {number} -----\n")
        
        if tool.analyze_number(number):
            tool.display_results()
            
            # Export results for valid numbers
            if i < len(TEST_NUMBERS):  # Skip the last one which is invalid
                filename = f"test_result_{i}"
                tool.export_results('json', filename)
        
        print("\n" + "-" * 50)
    
    print("\n===== TESTING COMPLETED =====\n")

if __name__ == "__main__":
    try:
        test_phone_info_tool()
    except KeyboardInterrupt:
        print("\n[!] Test interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] An unexpected error occurred during testing: {str(e)}")
        sys.exit(1)