# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to delete template file from storage.
class DeleteTemplate:
    @classmethod  
    def Run(cls):
        # For example purposes create template if not exists.
        Common.CreateIfNotExist("templates/companies.json")

        templateApi = groupdocs_parser_cloud.TemplateApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.TemplateOptions()
        options.template_path = "templates/template-for-companies.json"
        request = groupdocs_parser_cloud.DeleteTemplateRequest(options)
        response = templateApi.delete_template(request)
        
        print("Done.")
