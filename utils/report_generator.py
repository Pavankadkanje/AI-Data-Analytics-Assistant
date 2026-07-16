from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(df, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Data Analytics Report</b>", styles["Title"]))

    elements.append(Paragraph(f"Rows : {df.shape[0]}", styles["Normal"]))
    elements.append(Paragraph(f"Columns : {df.shape[1]}", styles["Normal"]))
    elements.append(Paragraph(f"Missing Values : {df.isnull().sum().sum()}", styles["Normal"]))
    elements.append(Paragraph(f"Duplicate Rows : {df.duplicated().sum()}", styles["Normal"]))

    elements.append(Paragraph("<br/><b>Column Information</b>", styles["Heading2"]))

    for col in df.columns:
        text = (
            f"{col} | "
            f"Datatype: {df[col].dtype} | "
            f"Missing: {df[col].isnull().sum()} | "
            f"Unique: {df[col].nunique()}"
        )
        elements.append(Paragraph(text, styles["Normal"]))

    doc.build(elements)