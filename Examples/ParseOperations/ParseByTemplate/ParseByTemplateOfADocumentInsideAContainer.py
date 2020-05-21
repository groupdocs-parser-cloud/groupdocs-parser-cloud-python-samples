# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to parse a document placed inside a container.
class ParseByTemplateOfADocumentInsideAContainer:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ParseOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "containers/archive/companies.zip"
        container_info = groupdocs_parser_cloud.ContainerItemInfo()
        container_info.relative_path = "companies.docx"
        options.container_item_info = container_info
        options.template = Common.GetTemplate()
        request = groupdocs_parser_cloud.ParseRequest(options)
        result = parseApi.parse(request)
        
        for data in result.fields_data:
            if data.page_area.page_text_area is not None:
                print("Field name: " + data.name + ". Text :" + data.page_area.page_text_area.text)

            if data.page_area.page_table_area is not None:
                print("Table name: " + data.name)
                for cell in data.page_area.page_table_area.page_table_area_cells:
                    print("Table cell. Row " + str(cell.row_index) + " column " + str(cell.column_index) + ". Text: " + cell.page_area.page_text_area.text);

