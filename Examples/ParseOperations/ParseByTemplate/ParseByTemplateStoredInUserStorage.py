# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to parse a document using template from user storage.
class ParseByTemplateStoredInUserStorage:
    @classmethod  
    def Run(cls):
        # For example purposes create template if not exists.
        Common.CreateIfNotExist("templates/companies.json")

        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ParseOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "words-processing/docx/companies.docx"
        options.template_path = "templates/companies.json"
        
        request = groupdocs_parser_cloud.ParseRequest(options)
        result = parseApi.parse(request)
        
        for data in result.fields_data:
            if data.page_area.page_text_area is not None:
                print("Field name: " + data.name + ". Text :" + data.page_area.page_text_area.text)

            if data.page_area.page_table_area is not None:
                print("Table name: " + data.name)
                for cell in data.page_area.page_table_area.page_table_area_cells:
                    print("Table cell. Row " + str(cell.row_index) + " column " + str(cell.column_index) + ". Text: " + cell.page_area.page_text_area.text);

