"""
Python program to convert Excel To PDF
"""
import jpype
import os
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

#Getting Path to cwd,data and report
file_path = os.path.dirname(__file__)
data_Path = f"{file_path}\\data"
report_path = f"{file_path}\\report\\"

def main():
    #List comprehension for every file path
    data_path = [ f.path for f in os.scandir(data_Path) ]
    for data in data_path:
        if "gitkeep" in data: continue #Getting error processing gitkeep as xls file
        try:
            #Loading the xls File to aspose Workbook
            workbook = Workbook(data)
            #get sheets to do auto fit columns
            worksheet = workbook.getWorksheets().get(0)
            worksheet.autoFitColumns()
            #creating pdf file path to store the converted data
            pdf_data = report_path + (os.path.basename(data).replace(".xls",".pdf"))
            try:
                #Updating(Removing) already existing files
                os.remove(pdf_data)
            except:
                pass
            #class Workbook have save method with file path and saveformat as PDF
            workbook.save(f"{pdf_data}", SaveFormat.PDF)
            print(f"Coverted from {os.path.basename(data)} to {os.path.basename(pdf_data)}")
        except Exception as E:
            print(E)
            break
    else:
        """Run when there's no break in loop"""
        print("Coversion Completed Successfully...")
        jpype.shutdownJVM()
        exit()

    #If Error:
    print("Some Error Occured")
    jpype.shutdownJVM()


if __name__ == "__main__":
    main()