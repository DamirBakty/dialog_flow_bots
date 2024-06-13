import json
import os

from environs import Env
from google.oauth2 import service_account


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    from google.cloud import dialogflow
    path_to_credentials = '/home/damir/Downloads/cred.json'

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path_to_credentials

    credentials = service_account.Credentials.from_service_account_file(
        path_to_credentials
    )
    intents_client = dialogflow.IntentsClient(

    )

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


env = Env()
env.read_env()
project_id = env.str('DIALOGFLOW_PROJECT_ID')

with open('/home/damir/Downloads/questions.json', 'r') as file:
    intents = json.load(file)
    for intent in intents:
        questions = intents[intent]['questions']
        answers = [intents[intent]['answer']]
        create_intent(
            project_id,
            intent,
            questions,
            answers
        )
