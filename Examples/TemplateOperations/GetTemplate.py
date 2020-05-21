# Import modules
import groupdocs_parser_cloud
from Common import Common

# This example demonstrates how to get template file from storage.
class GetTemplate:
    @classmethod  
    def Run(cls):
        # For example purposes create template if not exists.
        Common.CreateIfNotExist("templates/template-for-companies.json")

        templateApi = groupdocs_parser_cloud.TemplateApi.from_config(Common.GetConfig())
        options = groupdocs_parser_cloud.TemplateOptions()
        options.template_path = "templates/template-for-companies.json"
        request = groupdocs_parser_cloud.GetTemplateRequest(options)
        template = templateApi.get_template(request)
        
        for field in template.fields:
            print("Field: " + field.field_name)
        for table in template.tables:
            print("Table: " + table.table_name)
