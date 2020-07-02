
## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* query_knowledge_base
  - action_query_knowledge_base

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## bot challenge
* greet
  - utter_greet
* bot_challenge
  - utter_iamabot
* demand_joke
  - utter_joke
* confirm_exists
  - action_check_existence

## faq
* faq
  - respond_faq

## pokemon_faq
* query_knowledge_base
  - action_query_knowledge_base

## interactive_story_1
* greet
    - utter_greet
* confirm_exists{"pokemon_name": "charmander"}
    - slot{"pokemon_name": "charmander"}
    - action_check_existence
* confirm_exists{"pokemon_name": "rasa"}
    - slot{"pokemon_name": "rasa"}
    - action_check_existence

## interactive_story_1
* confirm_exists{"pokemon_name": "rasa"}
    - slot{"pokemon_name": "rasa"}
    - action_check_existence
* confirm_exists{"pokemon_name": "charmander"}
    - slot{"pokemon_name": "charmander"}
    - action_check_existence
* confirm_exists{"pokemon_name": "dittto"}
    - slot{"pokemon_name": "dittto"}
    - action_check_existence
