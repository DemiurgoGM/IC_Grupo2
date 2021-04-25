import os
import fitz
import pandas as pd

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

class Output:
  
  def generate_highlighted_pdf(self, path, to_highlight):
    doc = fitz.open(path)
    save_document = False
    
    for page in doc:
        for text in to_highlight:
          text_instances = page.searchFor(text)
          
          if text_instances is not None:
            for inst in text_instances:
                save_document = True
                highlight = page.addHighlightAnnot(inst)

    if save_document:
      path = default_storage.save('tmp/highlighted.pdf', ContentFile(""))

      return doc.save('tmp/highlighted.pdf', garbage=4, deflate=True, clean=True)
  
  def generate_csv(self, input_file_path, office_no, process_no, subject, originator, addresses):
    df = pd.DataFrame()
    
    for index, row in addresses.iterrows():
      data = {
          "ENDEREÇO": ("%s, %s, %s" % (row['Endereço'], row['Bairro'], row['Município'])),
          "INTERESSADO": originator,
          "AÇÃO": subject,
          "NUMERO_PROCESSO_SEI": process_no,
          "EXPEDIENTE": office_no,
      }

      df = df.append(data, ignore_index=True)

    path = default_storage.save('tmp/extracted_data.csv', ContentFile(""))
    return df.to_csv('tmp/extracted_data.csv', index = False)