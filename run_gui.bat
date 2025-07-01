@echo off
echo ===================================================
echo    تشغيل الواجهة الرسومية لأداة معلومات الهاتف
echo ===================================================
echo.

:: التحقق من وجود البيئة الافتراضية
if not exist venv (
    echo [!] لم يتم العثور على البيئة الافتراضية.
    echo [!] يرجى تشغيل setup_venv.bat أولاً لإعداد البيئة.
    echo.
    echo هل تريد تشغيل setup_venv.bat الآن؟ (Y/N)
    choice /c YN /m "اختر"
    if %ERRORLEVEL% EQU 1 (
        call setup_venv.bat
    ) else (
        echo [!] تم إلغاء العملية.
        exit /b 1
    )
)

:: تنشيط البيئة الافتراضية
call venv\Scripts\activate.bat

:: تشغيل الواجهة الرسومية
echo [+] جاري تشغيل الواجهة الرسومية...
python gui_tool.py

if %ERRORLEVEL% NEQ 0 (
    echo [!] حدث خطأ أثناء تشغيل الواجهة الرسومية.
    echo [!] تأكد من تثبيت جميع المتطلبات باستخدام setup_venv.bat
    pause
    exit /b 1
)

:: إلغاء تنشيط البيئة الافتراضية عند الخروج
deactivate