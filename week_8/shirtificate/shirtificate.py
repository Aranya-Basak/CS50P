from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", style="B", size=40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", x=5, y=80, w=200)
        self._pdf.set_font_size(35)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.cell(0, 180, align="C", text=f"{name} took CS50")

    def output(self, name):
        self._pdf.output(name)

def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
