# app.py
from flask import Flask, render_template, request, Response
import win32print
import win32ui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('print.html')

@app.route('/print', methods=['POST'])
def print_shared_printer():
    pdf_content = request.json.get('content')
    pdf_file = generate_pdf(pdf_content)
    printer_name = 'YourSharedPrinterName'  # Replace with the actual printer name
    print_to_shared_printer(pdf_file, printer_name)
    return "Printed to shared printer successfully!"

def generate_pdf(content):
    from io import BytesIO
    from reportlab.pdfgen import canvas
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, content)
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer.read()

def print_to_shared_printer(pdf_file, printer_name):
    printer_info = win32print.GetPrinter(printer_name)
    hprinter = win32print.OpenPrinter(printer_info['pPrinterName'])
    printer_defaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
    hprinter = win32print.OpenPrinter(printer_name, printer_defaults)

    printer_info = win32print.GetPrinter(hprinter, 2)
    printer_properties = printer_info['pDevMode']
    printer_properties.Orientation = win32print.DMORIENT_LANDSCAPE

    hprinter = win32print.OpenPrinter(printer_name, printer_defaults)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)
    hdc.StartDoc(pdf_file)
    hdc.StartPage()
    hdc.BitBlt((0, 0), (1500, 1200), hdc, (0, 0), win32con.SRCCOPY)
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()

if __name__ == '__main__':
    app.run(debug=True)
