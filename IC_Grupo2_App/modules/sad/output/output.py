import fitz
import pandas as pd

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
      doc.save(self.get_output_file_name(path, "pdf"), garbage=4, deflate=True, clean=True)
  
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

    df.to_csv(self.get_output_file_name(input_file_path, "csv"), index = False)

  def get_output_file_name(self, path, extension):
    file = path.split(os.path.sep)[-1]

    filename = file.split(".")[0]
    directory = "/".join(path.split(os.path.sep)[:-2])

    return directory + "/output/" + filename + "." + extension