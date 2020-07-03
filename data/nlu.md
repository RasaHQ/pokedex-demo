## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- yo

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- Ciao
- later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:demand_joke
- got a pokemon gag?
- could you tell me a joke?
- please give me a funny
- know any good pokemon puns?
- give me a wisecracker
- tell me of a good antic
- tell me a joke
- no, i want to hear a joke
- tell me another joke
- give me another one
- give me a good pokemon joke
- give me another joke
- oke, make me laugh one more time
- make me laugh

## intent:confirm_exists
- is [bulbasaur](pokemon_name) a pokemon
- does [ninetails](pokemon_name) exist
- ever heard of [pikachu](pokemon_name)
- are [pikachu](pokemon_name) and [charmander](pokemon_name) pokemon?
- is [rasa](pokemon_name) a pokemon?
- hey is [rasa](pokemon_name) a pokemon?
- are [pichuka](pokemon_name) and [charmander](pokemon_name) pokemon?
- are [snorlax](pokemon_name), [gariddos](pokemon_name) and [dittto](pokemon_name) pokemon?

## intent:name_translation
- What is the [french](language) name of [Snorlax](pokemon_name)?
- What is the [spanish](language) name of [Snorlax](pokemon_name)?
- What is the [german](language) name of [Snorlax](pokemon_name)?

## intent:faq/what_is_pokemon
- what is pokemon?
- can you tell me what pokemon is?

## intent:faq/how_many
- how many pokemon are there?
- are there a lot of pokemon?

## intent:faq/ask_berries
- what are pokemon berries?
- tell me about pokemon berries
- what are berries?
- what about these berries?

## intent:faq/pokemon_history
- when was Pokemon created?
- who created Pokemon?
- what's the history of Pokemon?

## intent:query_knowledge_base
- mention a few [pokemons]{"entity": "object_type", "value": "pokemon"}.
- give me some random [pokemons]{"entity": "object_type", "value": "pokemon"}.
- what are some [pokemons]{"entity": "object_type", "value": "pokemon"}?
- can you give examples of [pokemons]{"entity": "object_type", "value": "pokemon"}?

## synonym:pokemon
- pokemons

## lookup:pokemon_name
  data/pokenames.txt