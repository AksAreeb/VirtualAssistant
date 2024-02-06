# DeboAI

## Author

- **Areeb Shekhani**

## Overview

**DeboAI** is a virtual assistant designed to assist you with various tasks. It draws inspiration from the Computer Science teacher David Debono, incorporating personality traits that add a unique touch to your interactions. Explore its features and discover the influence of its inspiration as you continue to use it.

## Setup

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Initialize

#### Run the program and wait for the files to initialize. After a few seconds, a prompt saying "Speak..." will appear. Speak your task, and wait for the assistant to respond.

## Features

**Search Google:** Access information on the web.  
**Watch YouTube Videos:** Enjoy your favorite videos seamlessly.  
**Real-Time Weather:** Stay updated with the latest weather information.  
**Current Time:** Quickly find out the current time.  
**Open Apps:** Launch your preferred applications effortlessly.  
**Search GitHub:** Access code repositories with ease.  
**Message on WhatsApp:** Send messages to your contacts.  

## Triggers

**"Search" "text"** - Search on Google  
**"Youtube" "text"** - Search on Youtube  
**"Weather" "location"** - Get Weather  
**"Github" "account"** - Search GitHub  
**"Time"** - Current Time  
**"Open" "app-name"** - Open app  
**"Message" "message"** - Message (must add number in code)  
**"Wiki" "topic"** - Wiki a topic  

## How To Make Your Own Voice Model

**Step 1** - Gather audio from subject **or** create a list from ChatGPT for sentences that should be said to train a voice model.
**Step 2** - Make sure all sentences are in seperate files and are in .wav format.
**Step 3** - You can use either Coqui - TTS or Tortios or Bark AI to clone your desired voice.
**Step 4** - If you do not want real time voice cloning then you can use a longer audio file and add it into myvoice.Speechify.com . There is a free trial where you can clone around 1000 chars.
