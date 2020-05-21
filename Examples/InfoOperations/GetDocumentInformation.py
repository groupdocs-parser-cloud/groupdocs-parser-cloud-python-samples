# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to get document information
class GetDocumentInformation:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_parser_cloud.InfoApi.from_config(Common.GetConfig())
        parse_options = groupdocs_parser_cloud.InfoOptions()
        parse_options.file_info = groupdocs_parser_cloud.FileInfo()
        parse_options.file_info.file_path = "words-processing/docx/password-protected.docx"
        parse_options.file_info.password = "password"
        request = groupdocs_parser_cloud.GetInfoRequest(parse_options)
        result = infoApi.get_info(request)
        print("InfoResult.PageCount: " + str(result.page_count))