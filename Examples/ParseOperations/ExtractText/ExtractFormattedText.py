# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract formatted text from document.
class ExtractFormattedText:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.TextOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "words-processing/docx/formatted-document.docx"
        text_options = groupdocs_parser_cloud.FormattedTextOptions("Markdown")
        options.formatted_text_options = text_options

        request = groupdocs_parser_cloud.TextRequest(options)
        result = parseApi.text(request)
        print("Text:" + result.text)