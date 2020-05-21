# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract text from whole document.
class ExtractTextFromTheWholeDocument:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.TextOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "email/eml/embedded-image-and-attachment.eml"

        request = groupdocs_parser_cloud.TextRequest(options)
        result = parseApi.text(request)
        
        print("Text: " + result.text)
