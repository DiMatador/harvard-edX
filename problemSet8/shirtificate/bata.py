# working file
from fpdf import FPDF


class MyShirtfificate(FPDF):
    def __init__(self, name):
        # initialize MyShirtificate class
        super().__init__()
        self.name = name

    def header(self):
        """
        Prints out a PDF file with  a header
        """
        # Setting colors for text: 122, 18, 51
        self.set_text_color(46, 139, 192)

        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)

        # Setting font
        self.set_font("Courier", style="BI", size=35)

        # Moving cursor to the right:
        self.cell(80)

        # Print title:
        self.cell(50, 40, "CS50 Shirtificate", align="C", ln=1)

    def create_image(self, name):
        """ Prints an image to the PDF.
        image must be
        1. Vertically Center
        2. have a phrase in the middle of it
        """
        self.name = F"{name} took CS50"
        # Rendering Image:
        self.image("shirtificate.png", x=0, y=60)

        # Setting color for text:
        self.set_text_color(46, 139, 192)

        # Setting font: helvetica bold 15
        self.set_font("Courier", style="BI", size=25)

        # Moving cursor to the right:
        self.cell(80)

        # Printing title:
        self.cell(50, 180, self.name, align="C", ln=1)

        # # Performing a line break:
        # self.ln(20)


def main():
    """ Prints out the resulting PDF file """
    your_name = input("Name: ")

    pdf = MyShirtfificate(your_name)

    # Create a pdf page
    pdf.add_page()

    # Add an image to the pdf with a phrase
    pdf.create_image(your_name)

    # print the page
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
