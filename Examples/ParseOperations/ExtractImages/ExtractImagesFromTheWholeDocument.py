# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract images from whole document.
class ExtractImagesFromTheWholeDocument:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ImagesOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "slides/three-slides.pptx"

        request = groupdocs_parser_cloud.ImagesRequest(options)
        result = parseApi.images(request)

        for image in result.images:
            print("Image path in storage: " + image.path + ". Download url: " + image.download_url)
            print("Image format: " + image.file_format + ". Page index: " + str(image.page_index))
