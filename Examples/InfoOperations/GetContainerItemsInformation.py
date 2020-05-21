# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to obtain container items information.
class GetContainerItemsInformation:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_parser_cloud.InfoApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ContainerOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "containers/archive/zip.zip"
        request = groupdocs_parser_cloud.ContainerRequest(options)
        result = infoApi.container(request)
        for item in result.container_items:        
            print("Name: " + item.name + ". FilePath: " + item.file_path)