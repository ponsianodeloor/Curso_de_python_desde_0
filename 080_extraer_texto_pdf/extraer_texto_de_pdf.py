import aspose.words as aw

pdf = aw.Document("acuerdo_de_integridad.pdf")

pdf.save("extracted-text.txt")

