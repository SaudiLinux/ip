@echo off
echo Starting Phone Information Gathering Tool...
echo.

python -m pip install -r requirements.txt

echo.
echo Dependencies installed successfully!
echo.

python phone_info_tool.py %*

pause