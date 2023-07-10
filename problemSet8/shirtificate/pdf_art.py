from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="ASCII art text", ln=1)
pdf.output("ascii_art.pdf")
