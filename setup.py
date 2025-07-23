"""
Setup script for building the Currency Converter executable
Author: Currency Converter Team
Version: 1.0.0
"""

import os
import shutil
import sys

import PyInstaller.__main__


def build_executable():
    """Build the executable using PyInstaller"""

    # Application information
    APP_NAME = 'Currency_Converter'
    APP_VERSION = '1.0.0'
    APP_DESCRIPTION = 'Real-time Currency Converter with Autocomplete'
    APP_AUTHOR = 'Currency Converter Team'

    # Define the build arguments
    args = [
        '--onefile',  # Create a one-file bundled executable
        '--windowed',  # Hide console window (GUI app)
        '--name=' + APP_NAME,  # Name of the executable
        '--distpath=dist',  # Output directory
        '--workpath=build',  # Temporary build directory
        '--specpath=.',  # Spec file location
        '--clean',  # Clean PyInstaller cache
        '--noconfirm',  # Replace output directory without asking
        '--optimize=2',  # Optimize bytecode
        '--noupx',  # Don't use UPX compression

        # Icon (if available)
        '--icon=assets/icon/currency-converter.ico',

        # Hidden imports for modules PyInstaller might miss
        '--hidden-import=tkinter',
        '--hidden-import=tkinter.ttk',
        '--hidden-import=tkinter.messagebox',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.scrolledtext',
        '--hidden-import=requests',
        '--hidden-import=json',
        '--hidden-import=urllib3',
        '--hidden-import=urllib.request',
        '--hidden-import=urllib.parse',
        '--hidden-import=dotenv',
        '--hidden-import=PIL',
        '--hidden-import=PIL.Image',
        '--hidden-import=PIL.ImageTk',
        '--hidden-import=frontend.controllers.main_controller',
        '--hidden-import=frontend.ui.main_window',
        '--hidden-import=backend.models',
        '--hidden-import=backend.services',
        '--hidden-import=backend.data',

        # Collect data files
        '--collect-data=backend',
        '--collect-data=frontend',

        # Add data files
        '--add-data=assets;assets',
        '--add-data=backend;backend',
        '--add-data=frontend;frontend',

        # Main Python file
        'main.py'
    ]

    print("=" * 60)
    print(f"Building {APP_NAME} v{APP_VERSION}")
    print("=" * 60)
    print(f"Platform: {sys.platform}")
    print(f"Python version: {sys.version}")
    print()

    try:
        # Check if icon exists
        if not os.path.exists('assets/icon/currency-converter.ico'):
            print("Warning: Icon file not found. Building without icon.")
            # Remove icon argument
            args = [arg for arg in args if not arg.startswith('--icon=')]

        # Run PyInstaller
        print("Starting build process...")
        PyInstaller.__main__.run(args)

        print()
        print("=" * 60)
        print("Build completed successfully!")
        print("=" * 60)
        print(f"Executable location: {os.path.abspath('dist/' + APP_NAME + '.exe')}")

        # Create distribution files
        create_distribution_files(APP_NAME, APP_VERSION, APP_AUTHOR)

        print("\nDistribution files created successfully!")
        print("\nYour Currency Converter is ready to distribute!")

    except Exception as e:
        print(f"Build failed: {e}")
        sys.exit(1)


def create_distribution_files(app_name, app_version, app_author):
    """Create additional distribution files"""

    # Create README for distribution
    dist_readme = f"""Currency Converter - Distribution Package

Application: {app_name}
Version: {app_version}
Author: {app_author}
Build Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

FEATURES:
✓ Real-time Currency Exchange Rates
✓ Support for 150+ Currencies
✓ Autocomplete Currency Selection
✓ Offline Mode Support
✓ Clean and Intuitive Interface
✓ Fast and Accurate Conversions
✓ Error Handling and Validation
✓ Lightweight and Portable

CONTENTS:
- {app_name}.exe         : Main application executable
- README_DIST.txt        : This file
- LICENSE.txt            : License information
- User_Guide.pdf         : Detailed user manual (if available)

SYSTEM REQUIREMENTS:
- Windows 7/8/10/11 (32-bit or 64-bit)
- Minimum 2GB RAM
- 50MB free disk space
- Internet connection (for real-time rates)

INSTALLATION:
1. Simply run {app_name}.exe
2. No additional installation required
3. Application will create config files automatically

FIRST TIME SETUP:
1. Launch the application
2. The app will automatically fetch current exchange rates
3. Start converting currencies immediately
4. Set your preferred base currency if needed

FEATURES OVERVIEW:

💱 CURRENCY CONVERSION:
• Real-time exchange rates from ExchangeRate-API
• Support for all major world currencies
• Instant conversion as you type
• Historical rate tracking
• Offline mode with cached rates

🔍 SMART AUTOCOMPLETE:
• Type currency names or codes
• Intelligent search suggestions
• Quick selection from dropdown
• Support for currency symbols

⚡ PERFORMANCE:
• Fast startup time
• Minimal resource usage
• Efficient API rate limiting
• Background updates
• Responsive user interface

🛡️ RELIABILITY:
• Comprehensive error handling
• Automatic retry mechanisms
• Graceful offline degradation
• Input validation and sanitization

SUPPORTED CURRENCIES:
• USD - US Dollar
• EUR - Euro
• GBP - British Pound
• JPY - Japanese Yen
• AUD - Australian Dollar
• CAD - Canadian Dollar
• CHF - Swiss Franc
• CNY - Chinese Yuan
• INR - Indian Rupee
• And 140+ more currencies...

USAGE TIPS:
• Use currency codes (USD, EUR) or full names (US Dollar, Euro)
• The app remembers your last used currencies
• Check the status bar for last update time
• Right-click for additional options
• Use Tab key to navigate between fields

API INFORMATION:
This application uses ExchangeRate-API for real-time exchange rates.
• Updates every hour automatically
• Supports 168 currencies
• 99.9% uptime guarantee
• Professional-grade data source

SUPPORT:
For technical support or feature requests:
• Email: support@example.com
• GitHub: https://github.com/pyapril15/currency-converter
• Documentation: See built-in help system

COPYRIGHT:
© 2025 {app_author}. All rights reserved.
Licensed under MIT License - see LICENSE.txt for details.

DISCLAIMER:
Exchange rates are provided for informational purposes only.
Rates may vary from actual market rates.
Always verify rates with your financial institution for official transactions.
This software is not responsible for any financial decisions made using this data.
"""

    try:
        with open('dist/README_DIST.txt', 'w') as f:
            f.write(dist_readme)
    except Exception as e:
        print(f"Warning: Could not create dist README: {e}")

    # Copy additional files to dist
    files_to_copy = [
        ('LICENSE', 'LICENSE.txt'),
        ('README.md', 'README.md'),
    ]

    for src, dst in files_to_copy:
        try:
            if os.path.exists(src):
                shutil.copy2(src, f'dist/{dst}')
        except Exception as e:
            print(f"Warning: Could not copy {src}: {e}")

    # Create a simple installer batch file
    installer_content = f"""@echo off
echo ============================================
echo     Currency Converter Installer
echo ============================================
echo.

echo Installing Currency Converter...
echo.

set INSTALL_DIR=%PROGRAMFILES%\\Currency Converter

echo Creating installation directory...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Copying application files...
copy "{app_name}.exe" "%INSTALL_DIR%\\"
copy "README_DIST.txt" "%INSTALL_DIR%\\"
copy "LICENSE.txt" "%INSTALL_DIR%\\"

echo Creating desktop shortcut...
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%USERPROFILE%\\Desktop\\Currency Converter.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%INSTALL_DIR%\\{app_name}.exe" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%INSTALL_DIR%" >> CreateShortcut.vbs
echo oLink.Description = "Currency Converter - Real-time Exchange Rates" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs

echo Creating start menu entry...
set START_MENU=%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs
if not exist "%START_MENU%\\Currency Converter" mkdir "%START_MENU%\\Currency Converter"

echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateStartMenu.vbs
echo sLinkFile = "%START_MENU%\\Currency Converter\\Currency Converter.lnk" >> CreateStartMenu.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateStartMenu.vbs
echo oLink.TargetPath = "%INSTALL_DIR%\\{app_name}.exe" >> CreateStartMenu.vbs
echo oLink.WorkingDirectory = "%INSTALL_DIR%" >> CreateStartMenu.vbs
echo oLink.Description = "Currency Converter" >> CreateStartMenu.vbs
echo oLink.Save >> CreateStartMenu.vbs
cscript CreateStartMenu.vbs
del CreateStartMenu.vbs

echo.
echo ============================================
echo     Installation Completed Successfully!
echo ============================================
echo.
echo Currency Converter has been installed to:
echo %INSTALL_DIR%
echo.
echo Shortcuts created:
echo • Desktop shortcut
echo • Start Menu entry
echo.
echo You can now launch the application from:
echo 1. Desktop shortcut
echo 2. Start Menu → Currency Converter
echo 3. Direct execution from: %INSTALL_DIR%
echo.

set /p launch="Launch Currency Converter now? (y/n): "
if /i "%launch%"=="y" (
    echo Launching Currency Converter...
    start "" "%INSTALL_DIR%\\{app_name}.exe"
)

echo.
echo Thank you for using Currency Converter!
echo.
pause
"""

    try:
        with open('dist/install.bat', 'w') as f:
            f.write(installer_content)
        print("Installer script created: dist/install.bat")
    except Exception as e:
        print(f"Warning: Could not create installer script: {e}")


def clean_build_files():
    """Clean up build files"""
    dirs_to_remove = ['build', '__pycache__']
    files_to_remove = ['Currency_Converter.spec']

    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"Cleaned up: {dir_name}")
            except Exception as e:
                print(f"Warning: Could not remove {dir_name}: {e}")

    for file_name in files_to_remove:
        if os.path.exists(file_name):
            try:
                os.remove(file_name)
                print(f"Cleaned up: {file_name}")
            except Exception as e:
                print(f"Warning: Could not remove {file_name}: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Build Currency Converter executable')
    parser.add_argument('--clean', action='store_true', help='Clean build files after building')
    parser.add_argument('--test', action='store_true', help='Test the built executable')

    args = parser.parse_args()

    # Check if required files exist
    if not os.path.exists('main.py'):
        print("Error: main.py not found!")
        print("Please ensure you are running this script from the project directory.")
        sys.exit(1)

    # Check for assets directory
    if not os.path.exists('assets'):
        print("Warning: assets directory not found. Creating assets structure...")
        os.makedirs('assets/icon', exist_ok=True)
        print("Please place your currency-converter.ico file in assets/icon/ directory")

    # Build the executable
    build_executable()

    # Test the executable if requested
    if args.test:
        print("\nTesting the executable...")
        try:
            import subprocess

            exe_path = 'dist/Currency_Converter.exe'
            if os.path.exists(exe_path):
                print(f"Launching {exe_path} for testing...")
                subprocess.Popen([exe_path])
                print("Executable launched successfully!")
            else:
                print("Error: Executable not found for testing.")
        except Exception as e:
            print(f"Error testing executable: {e}")

    # Clean up if requested
    if args.clean:
        print("\nCleaning up build files...")
        clean_build_files()

    print("\n" + "=" * 60)
    print("Build process completed!")
    print("=" * 60)
    print("\nFiles created in 'dist' directory:")
    print("• Currency_Converter.exe - Main application")
    print("• README_DIST.txt - User documentation")
    print("• LICENSE.txt - License information")
    print("• install.bat - Optional installer script")
    print("\nYour Currency Converter is ready for distribution!")