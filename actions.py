import json
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    knowledge = Path("data/pokenames.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'pokemon_name':
                name = blob['value']
                if name in self.knowledge:
                    dispatcher.utter_message(text=f"Yes, {name} is a pokemon.")
                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
        return []


class ActionTranslateName(Action):
    """This action uses the Pokemon DB file
    to find the translated version of the name.
    """
    with open("data/pokemondb.json") as pokemon_db:
        knowledge = json.load(pokemon_db)

    languages = Path("data/languages.txt").read_text().split("\n")

    def name(self) -> Text:
        return "action_translate_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        language = None
        name = None

        # Get the entity values.
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'language':
                language = blob['value']
            if blob['entity'] == 'pokemon_name':
                name = blob['value']

        # Now we resolve the action.
        # But first, let's check if the Pokemon and language entity are valid.
        if name is None:
            dispatcher.utter_message(
                text=f"I do not recognize that name.")
            return []

        if language not in self.languages:
            dispatcher.utter_message(
                text=f"I do not yet support that language.")
            return []

        # If the Pokemon and language are found...
        for pokemon in self.knowledge['pokemon']:
            if pokemon['name'] != name:
                continue

            # Get the translated name.
            translated_name = pokemon.get(
                'name_language', {}).get(language)

            dispatcher.utter_message(
                text=f"{name}'s {language} name is {translated_name}."
            )

        return []


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/pokemondb.json")
        super().__init__(knowledge_base)
