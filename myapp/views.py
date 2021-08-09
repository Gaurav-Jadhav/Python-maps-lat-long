from django.shortcuts import render
import openpyxl


# Create your views here.
def hello(request):
    excel_file = request.FILES["excel_file"]
    file_data = openpyxl.load_workbook(excel_file)
    #for data in file_data:
    worksheet = file_data["Sheet1"]
    print(file_data["Sheet1"])
    excel_data = list()
    # iterating over the rows and
    # getting value from each cell in row
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    print(excel_data)
    return render(request,"map.html", {"data":excel_data})

def index(request):
    return render(request,"index.html", {})
