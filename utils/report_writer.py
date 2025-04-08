from fpdf import FPDF

def save_pdf_report(target, data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Scan Report for {target}", ln=True, align='C')
    for category, results in data.items():
        pdf.ln(10)
        pdf.cell(200, 10, txt=category, ln=True, align='L')
        for item in results:
            for key, value in item.items():
                pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
    pdf.output("scan_report.pdf")
