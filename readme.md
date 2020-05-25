<img src="images/logo.png" width=150 height=200 align="right">

# Pokemon Demo Bot 

This is a demonstration of a digital assistant that can answer questions about pokemon. This is an open project and anybody can contribute to it. 

It deserves mentioning that this is to be considered a hobby project. We do not guarantee that all the information on pokemon is 100% accurate or canon since we're just a community of fans. We're in no way affiliated with Nintendo or the Pokemon Company.

## Getting Started Locally

To run the assistant locally you'll first need to clone. 

```
git clone git@github.com:RasaHQ/pokedex-demo.git
```

Next, install rasa. 

```
pip install rasa
```

Next you'll need to train the assistant. 

```
rasa train
```

Once trained, you can now talk to it. Since we're using custom python code 
in there we'll need to run an action server on the side. So first start an
action server via;

```
rasa run actions
```

With this running you can now talk to your assistant. 

```
rasa shell
```

## Extra Inspection 

If you want to get more of a view of what is happening you can also run; 

```
rasa shell nlu
```

By running it this way you'll get more of a glimpse in what the NLU components think.

If you want to supply the assistant with new data you can also 
handle this interactively via;

```
rasa interactive
```

## Features 

The digital assistant cannot do much yet, but here's some of the features;

- checking if a given pokemon name indeed does exist
- retreival of some basic pokemon-themed jokes
- very basic faq

## Contributing

If you're interested in expanding what pokebot can do; we're all ears!

1. We would love it if people could add training data to the repository. 
2. We would love it if folks could think of ways to make pokebot more awesome in terms of features. Let's discuss these in an issue before making a PR though. 

---  

## About Rasa

- **What does Rasa do? 🤔**
  [Check out our Website](https://rasa.com/)

- **I'm new to Rasa 😄**
  [Get Started with Rasa](https://rasa.com/docs/getting-started/)

- **I'd like to read the detailed docs 🤓**
  [Read The Docs](https://rasa.com/docs/)

- **I'm ready to install Rasa 🚀**
  [Written Installation Guide](https://rasa.com/docs/rasa/user-guide/installation/) - [Video Guides](https://www.youtube.com/playlist?list=PL75e0qA87dlEWUA5ToqLLR026wIkk2evk)

- **I want to learn how to use Rasa 🚀**
  [Tutorial](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)

- **I have a question ❓**
  [Rasa Community Forum](https://forum.rasa.com/)

- **Explore More Starter Kits ⌨️**
  [Financial Demo](https://github.com/RasaHQ/financial-demo) [Medicare Locator Demo](https://github.com/RasaHQ/medicare_locator)