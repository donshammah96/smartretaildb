from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def add_shirt_image(self, image_path):
        self.image(image_path, x=0, y=60, w=210)

    def add_name(self, name):
        self.set_xy(0, 140)
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)
        self.cell(210, 10, name, 0, 1, "C")

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.add_shirt_image("shirtificate.png")
    pdf.add_name(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()