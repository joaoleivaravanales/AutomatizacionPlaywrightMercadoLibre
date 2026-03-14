from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def generar_reporte_pdf(nombre_test, resultado, screenshots):

    os.makedirs("reports", exist_ok=True)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf_path = f"reports/{nombre_test}.pdf"

    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph("Reporte de Automatización QA", styles['Title']))
    elementos.append(Spacer(1,20))

    elementos.append(Paragraph(f"<b>Escenario:</b> {nombre_test}", styles['Normal']))
    elementos.append(Paragraph(f"<b>Resultado:</b> {resultado}", styles['Normal']))
    elementos.append(Paragraph(f"<b>Fecha:</b> {fecha}", styles['Normal']))

    elementos.append(Spacer(1,20))

    for step in screenshots:

        paso = step["paso"]
        img = step["imagen"]

        if os.path.exists(img):

            elementos.append(Paragraph(f"<b>Paso:</b> {paso}", styles['Normal']))
            elementos.append(Spacer(1,10))

            imagen = Image(img)
            imagen.drawHeight = 300
            imagen.drawWidth = 500

            elementos.append(imagen)
            elementos.append(Spacer(1,20))

    doc = SimpleDocTemplate(pdf_path)
    doc.build(elementos)

    print(f"Reporte PDF generado: {pdf_path}")

    # 🧹 borrar screenshots
    for step in screenshots:
        img = step["imagen"]

        if os.path.exists(img):
            os.remove(img)

    print("Screenshots eliminados")