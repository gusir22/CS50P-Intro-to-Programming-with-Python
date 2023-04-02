from fpdf import FPDF


user_name = input("Name: ")
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("helvetica",style="B", size=50)
pdf.cell(txt="CS50 Shirtificate", w=0, align="C")
pdf.image("shirtificate.png", x=0, y=50)
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=47.5, y=140, txt=f"{user_name.capitalize()} took CS50")
pdf.output("shirtificate.pdf")
