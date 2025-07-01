@echo off
echo ===================================================
echo    إعداد بيئة افتراضية لأداة معلومات الهاتف
echo ===================================================
echo.

:: التحقق من وجود Python
python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [!] خطأ: لم يتم العثور على Python. يرجى تثبيت Python 3.6 أو أحدث.
    exit /b 1
)

:: التحقق من إصدار Python
for /f "tokens=2" %%I in ('python --version 2^>^&1') do set PYTHON_VERSION=%%I
echo [+] تم العثور على Python %PYTHON_VERSION%

:: إنشاء البيئة الافتراضية إذا لم تكن موجودة
if not exist venv (
    echo [+] إنشاء بيئة افتراضية جديدة...
    python -m venv venv
) else (
    echo [+] تم العثور على البيئة الافتراضية الموجودة
)

:: تنشيط البيئة الافتراضية وتثبيت المتطلبات
echo [+] تنشيط البيئة الافتراضية وتثبيت المتطلبات...
call venv\Scripts\activate.bat

:: تثبيت المتطلبات
pip install -r requirements.txt

if %ERRORLEVEL% NEQ 0 (
    echo [!] حدث خطأ أثناء تثبيت المتطلبات.
    exit /b 1
) else (
    echo [+] تم تثبيت جميع المتطلبات بنجاح!
)

echo.
echo ===================================================
echo    تم إعداد البيئة الافتراضية بنجاح!
echo    لتشغيل الأداة، استخدم: run_tool.bat
echo ===================================================

:: الحفاظ على البيئة الافتراضية نشطة
echo.
echo البيئة الافتراضية نشطة الآن. لإلغاء تنشيطها، اكتب: deactivate