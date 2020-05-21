# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to extract images from pages range.
class ExtractImagesByAPageNumberRange:
    @classmethod  
    def Run(cls):
        parseApi = groupdocs_parser_cloud.ParseApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.ImagesOptions()
        options.file_info = groupdocs_parser_cloud.FileInfo()
        options.file_info.file_path = "slides/three-slides.pptx"
        options.start_page_number = 1
        options.count_pages_to_extract = 2

        request = groupdocs_parser_cloud.ImagesRequest(options)
        result = parseApi.images(request)

        for page in result.pages:
            print("Images from " + str(page.page_index) + " page.")
            for image in page.images:
                print("Image path in storage: " + image.path + ". Download url: " + image.download_url)
