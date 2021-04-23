from extractors.information_extractor import InformationExtractor
from helpers.directory import Directory
from readers.ocr_reader import OCRDocumentReader
from readers.simple_reader import SimpleDocumentReader
from output.output import Output
from searchers.fuzzy_search import FuzzySearch

class Application:
  def __init__(self, input_file_path: str, address:str, directory:Directory, readers:[DocumentReader], extractor:InformationExtractor, output:Output, search: FuzzySearch):
    self.output = output
    self.search = search
    self.readers = readers
    self.address = address
    self.directory = directory
    self.extractor = extractor
    self.input_file_path = input_file_path

  def run(self):
    extracted_text = self.readers[0].read_document(self.input_file_path)
    fields = self.extractor.extract_all_informations(extracted_text)

    if (self.should_try_ocr(fields)):
      extracted_text = self.readers[1].read_document(self.input_file_path)
      fields = self.extractor.extract_all_informations(extracted_text)

    self.output.generate_highlighted_pdf(self.input_file_path, fields)

    office_no, process_no, subject, originator = fields

    addresses = self.search.for_address('Endereço', self.address)

    self.output.generate_csv(self.input_file_path, office_no, process_no, subject, originator, addresses[['Endereço', 'Bairro', 'Município']])
  
  def should_try_ocr(self, extracted_information:[str]):
    return all(information is "" for information in extracted_information)

obj = InformationExtractor()
print(obj.search_pattern("123/1234"))