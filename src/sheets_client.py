''''import os
import gspread
from google.oauth2.service_account import Credentials

# Define the path dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get project root
CONFIG_PATH = os.path.join(BASE_DIR, "config", "credentials.json")  # Locate credentials

# Define Google API scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

def authorize_gsheets():
    """Authorize and return a fresh Google Sheets client."""
    creds = Credentials.from_service_account_file(CONFIG_PATH, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet(sheet_name, worksheet_name):
    """Fetch a specific worksheet from a Google Sheet."""
    client = authorize_gsheets()  # Always get a fresh client
    return client.open(sheet_name).worksheet(worksheet_name)

def get_all_data(sheet_name, worksheet_name):
    """Fetch all data from a worksheet as a list of lists."""
    sheet = get_sheet(sheet_name, worksheet_name)
    return sheet.get_all_values()'''






'''
import os
import gspread
import json
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

# Load environment variables
load_dotenv()

# Define Google API scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
# Construct credentials from environment variables
service_account_info = {
    "type": "service_account",
    "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),  # Ensure correct format
    "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
}

def authorize_gsheets():
    """Authorize and return a fresh Google Sheets client."""
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet(sheet_name, worksheet_name):
    """Fetch a specific worksheet from a Google Sheet."""
    client = authorize_gsheets()
    return client.open(sheet_name).worksheet(worksheet_name)

def get_all_data(sheet_name, worksheet_name):
    """Fetch all data from a worksheet as a list of lists."""
    sheet = get_sheet(sheet_name, worksheet_name)
    return sheet.get_all_values()

'''




'''

import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define Google API scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Construct credentials from environment variables
service_account_info = {
    "type": "service_account",
    "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),  # Ensure correct format
    "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
}

def authorize_gsheets():
    """Authorize and return a fresh Google Sheets client."""
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet(sheet_name, worksheet_name):
    """Fetch a specific worksheet from a Google Sheet."""
    client = authorize_gsheets()
    return client.open(sheet_name).worksheet(worksheet_name)

def get_all_data(sheet_name, worksheet_name):
    """Fetch all data from a worksheet as a list of lists."""
    sheet = get_sheet(sheet_name, worksheet_name)
    return sheet.get_all_values()
'''




'''
import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define Google API scopes
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Function to print and check environment variables for debugging
def check_env_variables():
    print("Verifying Environment Variables:")
    print(f"GOOGLE_PROJECT_ID: {os.getenv('GOOGLE_PROJECT_ID')}")
    print(f"GOOGLE_PRIVATE_KEY_ID: {os.getenv('GOOGLE_PRIVATE_KEY_ID')}")
    print(f"GOOGLE_CLIENT_EMAIL: {os.getenv('GOOGLE_CLIENT_EMAIL')}")
    print(f"GOOGLE_CLIENT_ID: {os.getenv('GOOGLE_CLIENT_ID')}")
    print(f"GOOGLE_TOKEN_URI: {os.getenv('GOOGLE_TOKEN_URI')}")
    
    # Check for the private key's format
    private_key = os.getenv('GOOGLE_PRIVATE_KEY')
    if private_key:
        print("GOOGLE_PRIVATE_KEY: Key is loaded, checking formatting...")
        print(f"First 100 characters of the private key: {private_key[:100]}")
    else:
        print("GOOGLE_PRIVATE_KEY: Private key not found in environment variables.")
    
# Function to ensure private key is correctly formatted (replaces \n with actual newlines)
def get_private_key():
    private_key = os.getenv("GOOGLE_PRIVATE_KEY")
    if private_key:
        return private_key.replace("\\n", "\n")  # Ensure correct private key format
    return None

def authorize_gsheets():
    """Authorize and return a fresh Google Sheets client."""
    # Debug environment variables
    check_env_variables()

    # Construct credentials from environment variables
    service_account_info = {
        "type": "service_account",
        "project_id": os.getenv("GOOGLE_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
        "private_key": get_private_key(),
        "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
    }
    
    # Verify the credentials before using them
    if None in service_account_info.values():
        raise ValueError("Some credentials are missing. Check your environment variables.")
    
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet(sheet_name, worksheet_name):
    """Fetch a specific worksheet from a Google Sheet."""
    client = authorize_gsheets()  # Always get a fresh client
    return client.open(sheet_name).worksheet(worksheet_name)

def get_all_data(sheet_name, worksheet_name):
    """Fetch all data from a worksheet as a list of lists."""
    sheet = get_sheet(sheet_name, worksheet_name)
    return sheet.get_all_values()

'''


import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define Google API scopes (as per your request)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Function to ensure private key is correctly formatted (replaces \n with actual newlines)
def get_private_key():
    private_key = os.getenv("GOOGLE_PRIVATE_KEY")
    if private_key:
        return private_key.replace("\\n", "\n")  # Ensure correct private key format
    return None

def authorize_gsheets():
    """Authorize and return a fresh Google Sheets client."""
    
    # Construct credentials from environment variables
    service_account_info = {
        "type": "service_account",
        "project_id": os.getenv("GOOGLE_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
        "private_key": get_private_key(),
        "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
    }
    
    # Verify the credentials before using them
    if None in service_account_info.values():
        raise ValueError("Some credentials are missing. Check your environment variables.")
    
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    return gspread.authorize(creds)

def get_sheet(sheet_name, worksheet_name):
    """Fetch a specific worksheet from a Google Sheet."""
    client = authorize_gsheets()  # Always get a fresh client
    return client.open(sheet_name).worksheet(worksheet_name)

def get_all_data(sheet_name, worksheet_name):
    """Fetch all data from a worksheet as a list of lists."""
    sheet = get_sheet(sheet_name, worksheet_name)
    return sheet.get_all_values()
