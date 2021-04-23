import DocumentReader
from pikepdf import Pdf, PdfImage

class OCRDocumentReader(DocumentReader):
  
  def read_document(self, path):
    pdf = Pdf.open(path)

    document = pdf.pages[0]

    (name, raw_image) = next(document.images.items())

    image = PdfImage(raw_image).as_pil_image()

    text = pytesseract.image_to_string(image)
    
    return self.process_text(text)
