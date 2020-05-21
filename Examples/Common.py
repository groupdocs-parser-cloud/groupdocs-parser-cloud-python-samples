import groupdocs_parser_cloud
import glob
import os

class Common:

    # This properties are set from main class
    app_sid = None
    app_key = None
    myStorage = None
    
    @classmethod  
    def GetConfig(cls):
        configuration = groupdocs_parser_cloud.Configuration(cls.app_sid, cls.app_key)
        configuration.api_base_url = "https://api.groupdocs.cloud"
        return configuration

    @classmethod  
    def UploadSampleFiles(cls):
        
        # api initialization
        storageApi = groupdocs_parser_cloud.StorageApi.from_config(cls.GetConfig())
        fileApi = groupdocs_parser_cloud.FileApi.from_config(cls.GetConfig())

        # upload sample files
        for filename in glob.iglob("Resources/**/*.*", recursive=True):
            destFile = filename.replace("Resources\\", "", 1)            
            fileExistsResponse = storageApi.object_exists(groupdocs_parser_cloud.ObjectExistsRequest(destFile))
            if not fileExistsResponse.exists:                                
                fileApi.upload_file(groupdocs_parser_cloud.UploadFileRequest(destFile, filename))
                print("Uploaded file: "+ destFile)
    
    @classmethod
    def CreateIfNotExist(cls, file_path):
        storageApi = groupdocs_parser_cloud.StorageApi.from_config(cls.GetConfig())
        fileExistsResponse = storageApi.object_exists(groupdocs_parser_cloud.ObjectExistsRequest(file_path))
        if not fileExistsResponse.exists:
            options = groupdocs_parser_cloud.CreateTemplateOptions()
            template = cls.GetTemplate()
            options.template = template
            options.template_path = file_path
            createRequest = groupdocs_parser_cloud.CreateTemplateRequest(options)
            templateApi = groupdocs_parser_cloud.TemplateApi.from_config(cls.GetConfig())
            templateApi.create_template(createRequest)

    @classmethod
    def GetTemplate(cls):
        field1 = groupdocs_parser_cloud.Field()
        field1.field_name = "Address"
        fieldPosition1 = groupdocs_parser_cloud.FieldPosition()
        fieldPosition1.field_position_type = "Regex"
        fieldPosition1.regex = "Company address:"
        field1.field_position = fieldPosition1
        field2 = groupdocs_parser_cloud.Field()
        field2.field_name = "CompanyAddress"
        fieldPosition2 = groupdocs_parser_cloud.FieldPosition()
        fieldPosition2.field_position_type = "Linked"
        fieldPosition2.linked_field_name = "ADDRESS"
        fieldPosition2.is_right_linked = True
        size2 = groupdocs_parser_cloud.Size()
        size2.width = 100
        size2.height = 10
        fieldPosition2.search_area = size2
        fieldPosition2.auto_scale = True
        field2.field_position = fieldPosition2
        field3 = groupdocs_parser_cloud.Field()
        field3.field_name = "Company"
        fieldPosition3 = groupdocs_parser_cloud.FieldPosition()
        fieldPosition3.field_position_type = "Regex"
        fieldPosition3.regex = "Company name:"
        field3.field_position = fieldPosition3
        field4 = groupdocs_parser_cloud.Field()
        field4.field_name = "CompanyName"
        fieldPosition4 = groupdocs_parser_cloud.FieldPosition()
        fieldPosition4.field_position_type = "Linked"
        fieldPosition4.linked_field_name = "Company"
        fieldPosition4.is_right_linked = True
        size4 = groupdocs_parser_cloud.Size()
        size4.width = 100
        size4.height = 10
        fieldPosition4.search_area = size4
        fieldPosition4.auto_scale = True
        field4.field_position = fieldPosition4
        table = groupdocs_parser_cloud.Table()
        table.table_name = "Companies"
        detectorparams = groupdocs_parser_cloud.DetectorParameters()
        rect = groupdocs_parser_cloud.Rectangle()
        size = groupdocs_parser_cloud.Size()
        size.height = 60
        size.width = 480
        position = groupdocs_parser_cloud.Point()
        position.x = 77
        position.y = 279
        rect.size = size
        rect.position = position
        detectorparams.rectangle = rect
        table.detector_parameters = detectorparams
        fields = [field1, field2, field3, field4]
        tables = [table]
        template = groupdocs_parser_cloud.Template()
        template.fields = fields
        template.tables = tables
        return template
