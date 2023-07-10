from fpdf import FPDF

class MyShirtificate(FPDF):

    def __init__(self, name):
        # Initialize MyShirtificate class
        super().__init__()
        self.name = name

    def header(self):
        """
        Returns a PDF file with a header
        """

        """PDF file to be print out"""
        # page layout
        self.set_display_mode(zoom='default', layout='continuous')

        # Selecting font color
        self.set_text_color(46, 139, 192)

        # Setting frame thickness (1 mm)
        self.set_line_width(1)

        # Setting up the font
        self.set_font('Courier', style='BI', size=35)

        # Set cursor to the right
        self.cell(80)

        # Print Header
        self.cell(50, 40, "CS50 Shirtificate", align='C')

        # Line break
        self.ln(20)


    def create_image(self, name):
        """ Prints an image to the PDF.
        image must be
        1. Vertically Center
        2. have a phrase in the middle of it
        """
        # create a vertically centered image
        # self.set_margins(0, 0)
        # self.image("shirt.png", x=0, y=60)
        # PIL
        # set margin to 0
        #self.set_auto_page_break(auto=True, margin=0)
        # Shirt text variable
        on_shirt_text = F"{name} took CS50"

        # Set the image
        img = Image.open('shirtificate.png')

        # Create the image
        d = ImageDraw.Draw(img)

        # Setting up the font
        image_font = ImageFont.truetype('arial.ttf', 25)

        """
        calculate the text position, must be centered.
        we want to keep the text centered but not in the middle of the shirt
        """
        text_width, text_height = image_font.getsize(on_shirt_text)
        img_width, img_height = img.size
        text_x = (img_width - text_width) // 2
        text_y = (img_height - text_height) // 4

        # Add text to the image, color, and phrase to be printed
        d.text((text_x, text_y), on_shirt_text, (46, 139, 192), font=image_font)

        # save the img, this is not necesarry texting purposess only
        img.save('phrase.png')

        # Paste the image to an expecific location
        self.image('phrase.png', x=0, y=60)


def main():
    """ Prints out the resulting PDF file """
    your_name = input("Name: ")

    # instantiate class MyShirtificate
    pdf = MyShirtificate(your_name)

    # create a PDF page
    pdf.add_page()

    # create the image
    pdf.create_image(your_name)

    # Output the PDF
    pdf.output('shirtificate.pdf')


if __name__ == "__main__":
    main()
