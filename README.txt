QR & Barcode Generator (Python Desktop App)
==========================================

A modern desktop application built using Python and Tkinter that allows users
to generate QR codes and Barcodes easily. The app supports preview, download,
and print functionality with a clean, modular project structure.

--------------------------------------------------
Features
--------------------------------------------------
- Generate QR Codes from text or URLs
- Generate Code128 Barcodes
- Live preview of generated QR / Barcode
- Download QR / Barcode as PNG image
- Print QR / Barcode directly from the app (Windows)
- Clean, modular folder structure
- Ready for conversion to Windows EXE
- Beginner-friendly Python project

--------------------------------------------------
Project Structure
--------------------------------------------------
qr_barcode_app/
|
|-- main.py                -> Application entry point
|
|-- app/
|     |-- window.py        -> Main window, navigation, layout
|
|-- pages/
|     |-- qr_page.py       -> QR Generator UI & logic
|     |-- barcode_page.py  -> Barcode Generator UI & logic
|
|-- core/                  -> (Optional for future services)
|
|-- assets/
|     |-- logo.png         -> App logo / icon
|
|-- temp_files/            -> Temporary generated images (optional)
|-- logs/                  -> Logs (optional)
|
|-- requirements.txt       -> Python dependencies
|-- README.txt             -> Project documentation

--------------------------------------------------
Requirements
--------------------------------------------------
- Python 3.10 or higher
- Windows OS (for print feature support)

Install required packages:
pip install -r requirements.txt

--------------------------------------------------
How to Run
--------------------------------------------------
1. Open terminal / command prompt
2. Go to project folder:
   cd qr_barcode_app
3. Run the app:
   python main.py

--------------------------------------------------
Dependencies
--------------------------------------------------
- qrcode
- Pillow
- python-barcode

--------------------------------------------------
Future Improvements (Optional)
--------------------------------------------------
- Add settings page (dark mode, themes)
- Save history of generated QR / Barcodes
- Export to PDF
- Build Windows EXE using PyInstaller

--------------------------------------------------
Author
--------------------------------------------------
Developed by: Saurabh kanaujiya
GitHub: https://github.com/your-username

--------------------------------------------------
License
--------------------------------------------------
This project is open-source and free to use for learning and personal projects.


