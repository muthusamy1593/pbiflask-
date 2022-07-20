
class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '0875c93a-bdb2-4354-9941-691ad286c1cc'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '57d4c1d2-3811-42c5-ad60-277a7581ba61'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '24204333-c312-4a4c-a607-65f64a7ace43'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '3fd00a6f-252d-4208-949a-5407098d7942'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'FWF8Q~pueWNkxGi2_jtSXEg5SFxd9MK1MFxLAbAn'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''
