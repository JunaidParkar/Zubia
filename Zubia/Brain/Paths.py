import os
import sys
sys.path.append(os.environ.get('Zubia'))

LOCALAPPDATA = os.environ['LOCALAPPDATA']
LOCALFOLDER = f"{LOCALAPPDATA}\\Zubia"

DATABASE_FOLDER = f"{LOCALFOLDER}\\Database"

CHAT_DATA_FOLDER = f"{DATABASE_FOLDER}\\Chats"
CHAT_DATA_FILE = f"{CHAT_DATA_FOLDER}\\Chats.json"

TRAINED_DATA_FOLDER = f"{DATABASE_FOLDER}\\Train"
TRAINED_DATA_FILE = f"{TRAINED_DATA_FOLDER}\\TrainedData.pth"

LOCAL_COMMUNITY_FOLDER = f"{LOCALFOLDER}\\Community"
LOCALDATA_CONFIG_FILE = f"{LOCAL_COMMUNITY_FOLDER}\\Config.json"
SOFTWARE_CONFIG_FILE = f"{os.environ['Zubia']}\\Data\\Config.json"

DATASET_FOLDER = f"{LOCALFOLDER}\\Dataset"
LOCALDATA_INTENTS_FILE = f"{DATASET_FOLDER}\\Intents.json"
SOFTWARE_INTENTS_FILE = f"{os.environ['Zubia']}\\Brain\\Datasets\\Intents.json"


LOG_FOLDER = f"{LOCALFOLDER}\\Logs"
LOG_SETUP = f"{LOG_FOLDER}\\log.txt"