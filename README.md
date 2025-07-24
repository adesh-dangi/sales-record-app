Application for tracking sales and maintain records of customer for company "X"

GUI: PYQT6
# pyqt6-tools --- install this to get designer tools to generate code
<!-- https://www.pythonguis.com/installation/install-qt-designer-standalone/ -->
database: SQLITE-db
backend: python3


Turn project to exe
To convert your Python project into a standalone .exe (including only important code and assets), follow these steps:

Install PyInstaller:
pip install pyinstaller

Run PyInstaller on your main script (e.g., main.py or start_window.py):

pyinstaller --onefile --windowed --add-data "gui/images;gui/images" --add-data "gui/*.ui;gui" --add-data "data/record_sales.db;data" start_window.py

--onefile: creates a single .exe file.
--windowed: no console window (for GUI apps).
--add-data: include folders/files (format: source;destination).
After building, your .exe will be in the dist folder.

Test the .exe on a clean machine to ensure all assets are included.

Tips:

Only add essential files (images, .ui, .db) using --add-data.
Remove unnecessary files from your project before building.
If you use external packages, PyInstaller will include them automatically.
Example command for your project:
pyinstaller --onefile --windowed --name "Sales_Record_App" --add-data "gui/images;gui/images" main.py

This will package your app and required assets into a single executable.

resources:
pyqt learning
https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/

install pyqt
https://www.pythonguis.com/installation/install-qt-designer-standalone/

for sql process using sqlalchemy
https://dev.to/jconn4177/guide-to-the-best-python-libraries-and-modules-for-sql-21p0