# example taken from https://medium.com/snake-charmer-python-and-analytics/publishing-workbooks-to-tableau-server-via-python-and-rest-api-calls-f4bd26e54300
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects_dataframe


#  Set the following constants according to your environment
YOUR_PROJECT_ID = 'ENTER_YOUR_TS_PROJECT_ID'
YOUR_WORKBOOK_FILE_PATH = 'ENTER_YOUR_WORKBOOK_FILE_PATH'
YOUR_WORKBOOK_NAME = 'ENTER_YOUR_DESIRED_WORKBOOK_NAME'
YOUR_TABLEAU_SERVER_ADDRESS = 'ENTER_YOUR_TABLEAU_SERVER_ADDRESS'
YOUR_DB_SERVER_ADDRESS = 'ENTER_YOUR_DB_SERVER_ADDRESS'
YOUR_DB_PORT_NUMBER = None
YOUR_DB_USERNAME = 'ENTER_YOUR_DB_USERNAME'
YOUR_DB_PASSWORD = 'ENTER_YOUR_DB_PASSWORD'
YOUR_EMBED_FLAG = True

TS_CONFIG = {
        'my_env': {
                'server': 'https://YourTableauServer.com',
                'api_version': '<YOUR_API_VERSION>',
                'username': '<YOUR_USERNAME>',
                'password': '<YOUR_PASSWORD>',
                'site_name': '<YOUR_SITE_NAME>',
                'site_url': '<YOUR_SITE_CONTENT_URL>'
        }
}


conn = TableauServerConnection(config_json=TS_CONFIG, env='my_env')
conn.sign_in()

projects_df = get_projects_df(conn)
print(projects_df)

#  publish a workbook with a single connection to a published data source
response = conn.publish_workbook(workbook_file_path=YOUR_WORKBOOK_FILE_PATH, 
                                 workbook_name=YOUR_WORKBOOK_NAME, 
                                 project_id=YOUR_PROJECT_ID, 
                                 server_address=YOUR_TABLEAU_SERVER_ADDRESS)
print(response.json())

#  publish a workbook with embedded credentials
response = conn.publish_workbook(workbook_file_path=YOUR_WORKBOOK_FILE_PATH, 
                                 workbook_name=YOUR_WORKBOOK_NAME, 
                                 project_id=YOUR_PROJECT_ID, 
                                 server_address=YOUR_DB_SERVER_ADDRESS,
                                 port_number=YOUR_DB_PORT_NUMBER,
                                 connection_username=YOUR_DB_USERNAME,
                                 connection_password=YOUR_DB_PASSWORD, 
                                 embed_credentials_flag=YOUR_EMBED_FLAG)
print(response.json())

conn.sign_out()