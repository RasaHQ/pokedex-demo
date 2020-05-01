
## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

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
  - utter_goodbyez

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
