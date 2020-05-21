# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to save template file in storage.
class CreateOrUpdateTemplate:
    @classmethod  
    def Run(cls):
        templateApi = groupdocs_parser_cloud.TemplateApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.CreateTemplateOptions()
        options.template = Common.GetTemplate()
        options.template_path = "templates/template-for-companies.json"
        request = groupdocs_parser_cloud.CreateTemplateRequest(options)
        response = templateApi.create_template(request)
        
        print("Path to saved template in storage: " + response.template_path + ". Link to download template: " + response.url);

