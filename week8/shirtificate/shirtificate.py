import sys

from fpdf import FPDF
from fpdf.enums import Align


def main():
    value = input('Name: ')

    generate_pdf(value)


def generate_pdf(name):
    try:
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        # Header
        pdf.set_font(family="Helvetica", style="B", size=40)
        pdf.x = pdf.l_margin
        pdf.y = 10
        pdf.cell(text='CS50 Shirtificate', w=0, align=Align.C, border=1)

        # Shirt image
        pdf.image(name='shirtificate.png', x=Align.C, y=40, w=pdf.w - 10)

        # Test on shirt
        pdf.x = pdf.l_margin
        pdf.y = 100
        pdf.set_font(family="Courier", style='B', size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(text=f'{name} took CS50', w=0, align=Align.C)

        # Create PDF
        pdf.output('shirtificate.pdf')
    except Exception as e:
        sys.exit(99)


if __name__ == '__main__':
    main()
