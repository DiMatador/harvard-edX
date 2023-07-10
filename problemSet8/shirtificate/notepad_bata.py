from fpdf import FPDF

# create a FPDF object
pdf = FPDF()

# add a page to the pdf
pdf.add_page()

# before printing we must first set the font type, B=bold size=16
pdf.set_font("helvetica", "B", 16)

# cell will print the cell, cell is a rectangle area, defaulf is current possition
pdf.cell(40, 10, "Hello world!")

# add a new cell next to the last cell, centered text and to the next
# line use this 
pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')

# Finally, the document is closed and saved under the provided file path using output. 
# Without any parameter provided, output() returns the PDF bytearray buffer.
pdf.output("tuto1.pdf")
