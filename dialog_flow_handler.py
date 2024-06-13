from google.cloud import dialogflow_v2beta1 as dialogflow
from google.oauth2 import service_account


def detect_intent_texts(project_id, session_id, text, path_to_credentials, language_code='ru-RU'):
    credentials = service_account.Credentials.from_service_account_file(
        path_to_credentials
    )
    session_client = dialogflow.SessionsClient(credentials=credentials)

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={"session": session, "query_input": query_input})

    return response.query_result.fulfillment_text
