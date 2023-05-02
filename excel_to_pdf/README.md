# Excel to PDF
==============================

A simple Python programme to convert from Excel to PDF using the aspose-cells API.

Folder Structure
------------

    ├── data             <- Folder to save input datas
    |
    ├── report           <- Folder where output saves
    |
    ├── app.py           <- Main Python file
    └── requirements.txt <- Required Python Libraries

--------

Used Modules and Methods
------------------------

# <a target="_blank" href="https://jpype.readthedocs.io/en/latest/">jpype</a>
For running Java-specific libraries and packages.

# <a target="_blank" href="https://docs.python.org/3/library/os.html">os</a>
For getting file paths, scanning directories, getting file names of pdf files, etc.

# <a target="_blank" href="https://reference.aspose.com/cells/python-java/asposecells.api/Workbook">asposecells.api.Workbook</a>
represents a root object to create an Excel spreadsheet.

# <a target="_blank" href="https://reference.aspose.com/cells/python-java/asposecells.api/saveformat">asposecells.api.SaveFormat</a>
Utility class containing constants Represents the format in which the workbook is saved.