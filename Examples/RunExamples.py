# Import modules
import groupdocs_parser_cloud
from Common import Common

# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
Common.app_sid = "XXXXXXXXXXXXXXXXXXX"
Common.app_key = "XXXXXXXXXXXXXXXXXXX"

Common.myStorage = "First Storage"

# Uploading sample test files from local disk to cloud storage
#Common.UploadSampleFiles()

from InfoOperations.GetSupportedFormats import GetSupportedFormats
GetSupportedFormats.Run()
from InfoOperations.GetDocumentInformation import GetDocumentInformation
GetDocumentInformation.Run()
from InfoOperations.GetContainerItemsInformation import GetContainerItemsInformation
GetContainerItemsInformation.Run()

from ParseOperations.ExtractImages.ExtractImagesByAPageNumberRange import ExtractImagesByAPageNumberRange
ExtractImagesByAPageNumberRange.Run()
from ParseOperations.ExtractImages.ExtractImagesFromADocumentInsideAContainer import ExtractImagesFromADocumentInsideAContainer
ExtractImagesFromADocumentInsideAContainer.Run()
from ParseOperations.ExtractImages.ExtractImagesFromTheWholeDocument import ExtractImagesFromTheWholeDocument
ExtractImagesFromTheWholeDocument.Run()

from ParseOperations.ExtractText.ExtractFormattedText import ExtractFormattedText
ExtractFormattedText.Run()
from ParseOperations.ExtractText.ExtractTextByAPageNumberRange import ExtractTextByAPageNumberRange
ExtractTextByAPageNumberRange.Run()
from ParseOperations.ExtractText.ExtractTextFromADocumentInsideAContainer import ExtractTextFromADocumentInsideAContainer
ExtractTextFromADocumentInsideAContainer.Run()
from ParseOperations.ExtractText.ExtractTextFromTheWholeDocument import ExtractTextFromTheWholeDocument
ExtractTextFromTheWholeDocument.Run()

from ParseOperations.ParseByTemplate.ParseByTemplateDefinedAsAnObject import ParseByTemplateDefinedAsAnObject
ParseByTemplateDefinedAsAnObject.Run()
from ParseOperations.ParseByTemplate.ParseByTemplateOfADocumentInsideAContainer import ParseByTemplateOfADocumentInsideAContainer
ParseByTemplateOfADocumentInsideAContainer.Run()
from ParseOperations.ParseByTemplate.ParseByTemplateStoredInUserStorage import ParseByTemplateStoredInUserStorage
ParseByTemplateStoredInUserStorage.Run()

from TemplateOperations.CreateOrUpdateTemplate import CreateOrUpdateTemplate
CreateOrUpdateTemplate.Run()
from TemplateOperations.DeleteTemplate import DeleteTemplate
DeleteTemplate.Run()
from TemplateOperations.GetTemplate import GetTemplate
GetTemplate.Run()