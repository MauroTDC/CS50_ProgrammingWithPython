import fpdf
import sys


class PDF():
    def __init__(self, name: str):
        self._pdf = fpdf.FPDF(orientation="P", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 36)
        self._pdf.cell(w=0,h=0,text="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT",align='C')
        self._pdf.ln(h=20)
        try:
            self._pdf.image("./problem_set_8/shirtificate.png",w=self._pdf.epw)
        except:
            sys.exit("Error opening image")
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("helvetica", "B", 24)
        self._pdf.cell(w=0, h=-250,text=f"{name} took CS50", new_x="LMARGIN", new_y="NEXT",align='C')

    def save(self, filename: str):
        try:
            self._pdf.output(f"./problem_set_8/{filename}")
        except:
            sys.exit("Error saving file")


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()