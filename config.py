import os

#basedir = os.path.abspath(os.path.dirname(_file_))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')# or 'secret-key'
    if not SECRET_KEY:
          raise ValueError("Need to define SECRET_KEY environment variable")
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')# or 'ENTER_STORAGE_ACCOUNT_NAME'
    if not BLOB_ACCOUNT:
          raise ValueError("Need to define BLOB_ACCOUNT environment variable")
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')# or 'ENTER_BLOB_STORAGE_KEY'
    if not  BLOB_STORAGE_KEY :
          raise ValueError("Need to define  BLOB_STORAGE_KEY environment variable")
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') #or 'ENTER_IMAGES_CONTAINER_NAME'
    if not BLOB_CONTAINER:
          raise ValueError("Need to define BLOB_CONTAINER environment variable")
    SQL_SERVER = os.environ.get('SQL_SERVER') #or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    if not SQL_SERVER:
          raise ValueError("Need to define  SQL_SERVER environment variable")
    SQL_DATABASE = os.environ.get('SQL_DATABASE') #or 'ENTER_SQL_DB_NAME'
    if not SQL_DATABASE:
          raise ValueError("Need to define SQL_DATABASE environment variable")
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') #or 'ENTER_SQL_SERVER_USERNAME'
    if not SQL_USER_NAME:
          raise ValueError("Need to define SQL_USER_NAME environment variable")
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') #or 'ENTER_SQL_SERVER_PASSWORD'
    if not SQL_PASSWORD:
          raise ValueError("Need to define SQL_PASSWORD environment variable")
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://"
    + SQL_USER_NAME + ":"
    + SQL_PASSWORD + "@"
    + SQL_SERVER + ".database.windows.net:1433/"
    + SQL_DATABASE
    + "?driver=ODBC+Driver+17+for+SQL+Server")
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TENANT_NAME=os.environ.get('TENANT_NAME') #or 'ENTER_YOUR_TENANT_NAME_HERE'
    if not TENANT_NAME:
          raise ValueError("Need to define TENANT_NAME environment variable")
    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    #CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    if not CLIENT_SECRET:
          raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_NAME}"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = os.environ.get('CLIENT_ID') 

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
