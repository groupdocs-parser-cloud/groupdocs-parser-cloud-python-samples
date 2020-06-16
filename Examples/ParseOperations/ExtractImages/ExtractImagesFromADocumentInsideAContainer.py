# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract images from container item.
class ExtractImagesFromADocumentInsideAContainer:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ImagesOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "pdf/PDF with attachements.pdf"
        options.file_info.password = "password"
        container_info = groupdocs_parser_cloud.ContainerItemInfo()
        container_info.relative_path = "template-document.pdf"
        options.container_item_info = container_info
        options.start_page_number = 2
        options.count_pages_to_extract = 1

        request = groupdocs_parser_cloud.ImagesRequest(options)
        result = parseApi.images(request)

        for page in result.pages:
            print("Images from " + str(page.page_index) + " page.")
            for image in page.images:
                print("Image path in storage: " + image.path + ". Download url: " + image.download_url)
                print("Image format: " + image.file_format + ". Page index: " + str(image.page_index))
