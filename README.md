# Currency Converter

![Currency Converter](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A modern, feature-rich currency converter application built with Python and tkinter. Get real-time exchange rates for 150+ currencies with an intuitive interface and smart autocomplete functionality.

## 🌟 Features

### Core Functionality
- **Real-time Exchange Rates**: Powered by ExchangeRate-API for accurate, up-to-date rates
- **150+ Currencies Supported**: All major world currencies including cryptocurrencies
- **Smart Autocomplete**: Intelligent currency selection with search-as-you-type
- **Offline Mode**: Cached rates for use without internet connection
- **Instant Conversion**: Real-time conversion as you type

### User Experience
- **Clean Interface**: Modern, intuitive design built with tkinter
- **Fast Performance**: Optimized for quick startup and responsive operation
- **Error Handling**: Comprehensive error handling for network issues and invalid inputs
- **Cross-Platform**: Works on Windows, macOS, and Linux

### Technical Features
- **MVC Architecture**: Well-structured codebase with separation of concerns
- **API Integration**: Professional-grade ExchangeRate-API integration
- **Configuration Management**: Environment variables for API keys and settings
- **Extensible Design**: Easy to add new features and currency sources

## 📸 Screenshots

```
┌─────────────────────────────────────┐
│           Currency Converter        │
├─────────────────────────────────────┤
│ From: [USD - US Dollar     ▼] [100] │
│ To:   [EUR - Euro          ▼] [85.2]│
│                                     │
│ Rate: 1 USD = 0.852 EUR             │
│ Last Updated: 2024-12-19 14:30 UTC  │
│                                     │
│ [Convert] [Swap] [Refresh] [About]  │
└─────────────────────────────────────┘
```

## 🚀 Quick Start

### Option 1: Run from Executable (Recommended)
1. Download the latest release from [Releases](https://github.com/pyapril15/currency-converter/releases)
2. Run `Currency_Converter.exe` (no installation required)
3. Start converting currencies immediately!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/pyapril15/currency-converter.git
cd currency-converter

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## 🔧 Building from Source

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Internet connection (for dependencies)

### Build Steps

#### Windows (Automated)
```cmd
# Run the automated build script
build.bat
```

#### Manual Build
```bash
# Install build dependencies
pip install pyinstaller

# Install project dependencies
pip install -r requirements.txt

# Build executable using setup script
python setup.py

# Or build manually with PyInstaller
pyinstaller --onefile --windowed --name=Currency_Converter main.py
```

The executable will be created in the `dist/` directory.

## 📋 Requirements

### System Requirements
- **OS**: Windows 7+, macOS 10.12+, or Linux (any modern distribution)
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 50MB free space
- **Network**: Internet connection for real-time rates (optional for cached rates)

### Python Dependencies
```
requests~=2.32.3
python-dotenv~=1.0.1
pillow~=11.2.1
```

For building executables:
```
pyinstaller>=5.13.0
```

## 🏗️ Project Structure

```
currency-converter/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── setup.py               # Build script for executable
├── build.bat              # Windows build automation
├── README.md              # This file
├── LICENSE                # MIT License
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
│
├── assets/                # Application assets
│   ├── icon/              # Application icons
│   ├── images/            # UI images and graphics
│   └── screenshots/       # Screenshots for documentation
│
├── backend/               # Backend logic
│   ├── data/              # Data files and currency lists
│   │   └── currencies_with_flags.json
│   ├── models/            # Data models
│   └── services/          # API services and business logic
│
└── frontend/              # Frontend UI components
    ├── controllers/       # UI controllers
    │   └── main_controller.py
    └── ui/                # User interface
        └── main_window.py
```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
# API Configuration
EXCHANGE_API_KEY=your_api_key_here
EXCHANGE_API_URL=https://api.exchangerate-api.com/v4/latest/

# Application Settings
DEFAULT_FROM_CURRENCY=USD
DEFAULT_TO_CURRENCY=EUR
UPDATE_INTERVAL=3600
CACHE_DURATION=86400

# UI Settings
WINDOW_WIDTH=500
WINDOW_HEIGHT=400
THEME=modern
```

### API Setup
1. Get a free API key from [ExchangeRate-API](https://exchangerate-api.com/)
2. Add your API key to the `.env` file
3. Restart the application

## 🎯 Usage

### Basic Conversion
1. Launch the application
2. Select source currency from the dropdown
3. Select target currency from the dropdown
4. Enter amount to convert
5. View real-time conversion result

### Advanced Features
- **Autocomplete**: Start typing currency name or code in dropdown
- **Swap Currencies**: Click swap button to reverse conversion
- **Refresh Rates**: Manual refresh for latest exchange rates
- **Offline Mode**: App works with cached rates when offline

### Keyboard Shortcuts
- `Ctrl + R`: Refresh exchange rates
- `Ctrl + S`: Swap currencies
- `Tab`: Navigate between fields
- `Enter`: Perform conversion

## 🔌 API Integration

This application uses [ExchangeRate-API](https://exchangerate-api.com/) for real-time exchange rates:

### Features
- **168 currencies** supported
- **Real-time updates** every hour
- **Historical data** available
- **99.9% uptime** guarantee
- **Free tier** available (1,500 requests/month)

### Rate Limits
- Free tier: 1,500 requests/month
- Pro tiers: Up to 100,000+ requests/month
- Automatic caching to minimize API calls

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```bash
# Fork the repository
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available

# Run tests
python -m pytest tests/

# Run the application
python main.py
```

### Contribution Guidelines
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Include unit tests for new features
- Update documentation as needed

## 🐛 Troubleshooting

### Common Issues

#### Application Won't Start
- **Solution**: Ensure Python 3.7+ is installed
- **Check**: Verify all dependencies are installed (`pip install -r requirements.txt`)

#### No Exchange Rates Loading
- **Solution**: Check internet connection
- **Check**: Verify API key in `.env` file
- **Fallback**: App will use cached rates if available

#### Autocomplete Not Working
- **Solution**: Ensure currency data file exists in `backend/data/`
- **Check**: Verify file permissions

#### Build Errors
- **Solution**: Install PyInstaller (`pip install pyinstaller`)
- **Check**: Ensure all project files are present
- **Alternative**: Use manual PyInstaller command

### Getting Help
- 📧 **Email**: support@example.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/pyapril15/currency-converter/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/pyapril15/currency-converter/discussions)

## 📊 Supported Currencies

### Major Currencies
| Code | Currency | Symbol |
|------|----------|--------|
| USD | US Dollar | $ |
| EUR | Euro | € |
| GBP | British Pound | £ |
| JPY | Japanese Yen | ¥ |
| AUD | Australian Dollar | A$ |
| CAD | Canadian Dollar | C$ |
| CHF | Swiss Franc | Fr |
| CNY | Chinese Yuan | ¥ |
| INR | Indian Rupee | ₹ |

### Regional Currencies
- **Asia**: JPY, CNY, INR, KRW, SGD, HKD, THB, MYR, IDR, PHP
- **Europe**: EUR, GBP, CHF, SEK, NOK, DKK, PLN, CZK, HUF
- **Americas**: USD, CAD, MXN, BRL, ARS, CLP, COP, PEN
- **Middle East**: AED, SAR, QAR, KWD, BHD, OMR, JOD
- **Africa**: ZAR, EGP, NGN, KES, GHS, MAD, TND

And 100+ more currencies including cryptocurrencies!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ **Commercial use** allowed
- ✅ **Modification** allowed
- ✅ **Distribution** allowed
- ✅ **Private use** allowed
- ❌ **Liability** not accepted
- ❌ **Warranty** not provided

## 🌟 Acknowledgments

- **ExchangeRate-API** for providing reliable exchange rate data
- **Python Community** for excellent libraries and tools
- **tkinter** for the GUI framework
- **Pillow** for image processing capabilities
- **Requests** for HTTP functionality

## 📈 Roadmap

### Version 1.1.0 (Planned)
- [ ] Dark theme support
- [ ] Currency conversion history
- [ ] Favorite currencies
- [ ] Chart visualization of rate trends

### Version 1.2.0 (Future)
- [ ] Multi-language support
- [ ] Currency calculator mode
- [ ] Cryptocurrency support
- [ ] Rate alerts and notifications

### Version 2.0.0 (Future)
- [ ] Web interface
- [ ] Mobile app version
- [ ] Advanced analytics
- [ ] API for third-party integration

## 📞 Contact

- **Project**: [Currency Converter](https://github.com/pyapril15/currency-converter)
- **Author**: Currency Converter Team
- **Email**: support@example.com
- **Website**: [https://currency-converter.app](https://currency-converter.app)

---

<div align="center">

**Made with ❤️ by the Currency Converter Team**

[⭐ Star this project](https://github.com/pyapril15/currency-converter) • [🐛 Report Bug](https://github.com/pyapril15/currency-converter/issues) • [✨ Request Feature](https://github.com/pyapril15/currency-converter/issues)

</div>