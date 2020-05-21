# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract text from pages range.
class ExtractTextByAPageNumberRange:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.TextOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "cells/two-worksheets.xlsx"
        options.start_page_number = 1
        options.count_pages_to_extract = 1

        request = groupdocs_parser_cloud.TextRequest(options)
        result = parseApi.text(request)
        
        for page in result.pages:
            print("PageIndex: " + str(page.page_index) + ". Text: " + page.text)
