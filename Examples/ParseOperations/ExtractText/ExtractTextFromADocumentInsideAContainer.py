# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract text from container item.
class ExtractTextFromADocumentInsideAContainer:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.TextOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "pdf/PDF with attachements.pdf"
        options.file_info.password = "password"
        container_info = groupdocs_parser_cloud.ContainerItemInfo()
        container_info.relative_path = "template-document.pdf"
        options.container_item_info = container_info
        options.start_page_number = 2
        options.count_pages_to_extract = 1

        request = groupdocs_parser_cloud.TextRequest(options)
        result = parseApi.text(request)
        
        print("Text: " + result.pages[0].text)
