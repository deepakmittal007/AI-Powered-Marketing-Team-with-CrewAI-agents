AI-Powered-Marketing-Team-with-CrewAI-agents is the project title which gives the inspiration to use agents to save time and maximise our efforts more towards business alignment.
You may check out this in brief in the utils section where I have kept a .pdf version of my presentation which will cover every vertical and business use case undersatnding required.

Here, I will focus directly on how to use this application.

1. First step is to create your .env file and store it in the parent directory with the all the values, for privacy issues I have not shared the .env file but I will provide what
all features need to be filled there.

# LLM Credentials - required for building agents
OPENAI_API_KEY
OPENAI_API_VERSION
OPENAI_API_BASE
OPENAI_API_DEPLOYMENT_ID

# Web Scrapping - which required for web scrapping and you can create your own after signing to thier website and you will receive 2500 credits as signing bonus. 
SERPER_API_KEY=

DATAROBOT_ENDPOINT=

# RAG Details of DataRobot Chatbot - Details can be fetched once the RAG playground is deployed from the Prediction API environment.
API_URL_DataRobot
API_KEY_DataRobot
DATAROBOT_KEY_DataRobot
DEPLOYMENT_ID_DataRobot

# RAG details of Persistent Chatbot - Details can be fetched once the RAG playground is deployed from the Prediction API environment.
API_URL_Persistent
API_KEY_Persistent
DATAROBOT_KEY_Persistent
DEPLOYMENT_ID_Persistent

# You need to use your own keys everywhere.

2. Once this is done, you are all set. Run the below command to start the crew agents, this will take sometime, relax and wait for sometime to get the task complete.
Before running this command, you may choose to delete all the files in resources folder as they are going to be overwritten after hitting the below command.
# python crew.py

3. Running chatbot individually for both the organisations. use the below command, before hitting just check you are in chatbot directory.
# streamlit run datarobot.py
# streamlit run persistent.py

4. Using Predictor Application, this is acccessible via link which is already been provided in the utils/predictive_application_info but still providing here as well.
# https://app.datarobot.com/applications/68d3d9632ea75184f6863242/?token=zSAL2p_tRrt9zM5_XxsdyCr_xN41UqD42D6Xz6aOWEk

You are now very well equiped to use the application fully, still you face any difficulty in accessing the application, feel free to connect.



