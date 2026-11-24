# Simple Encrypted Chatting App

Client-to-client chatting app with basic encryption, built in Python.

Built to explore how to break a networking problem into parts: UI, connection, encryption and message handling.

## What it does

- Client GUI to type and send a message
- Encrypts the message before sending it over the network
- Server receives the message, decrypts it, and replies
- Displays the decrypted reply in the client GUI

## Tech Stack

- Python
- CustomTkinter - dark mode GUI for the client
- socket - TCP client-server connection
- cryptography.fernet - symmetric encryption

## How it works

**Client (`frontend.py`):**
- Connects to the server via socket on port 4412
- Takes user input from `CTkEntry`
- Generates a Fernet key with `Fernet.generate_key()`
- Encrypts message with `cipher.encrypt(msg.encode("utf-8"))`
- Sends encrypted message + key to server
- Receives encrypted reply + key, decrypts it, shows it in `CTkTextbox`

**Server (`server.py`):**
- Binds to `0.0.0.0:4412` and listens for a client
- Receives encrypted message and key
- Decrypts with `Fernet(key)` and prints it
- Takes a reply via terminal input, encrypts it with a new key and sends it back

> Note: This version only works locally / on one device for testing, as noted in the server code.

## How to Run

1. Start the server:
```bash
python server.py
```

2. Start the client in another terminal:
```bash
python frontend.py
```

The client connects to the server IP in `frontend.py` (currently `192.168.0.18`).

## What I Learned

- Breaking a problem into parts: frontend UI, networking, encryption, receiving/decrypting
- Socket programming - `socket.AF_INET`, `SOCK_STREAM`, `bind`, `listen`, `accept`, `recv`, `send`
- Symmetric encryption with Fernet - key generation, encrypt / decrypt workflow
- Handling user input and displaying output in a GUI while managing network calls

## Limitations & Future Improvements

- Key is sent alongside the message, so it is not truly secure - future version would use key exchange / public-key cryptography
- Only handles one client at a time and uses blocking terminal input on the server side
- Would improve by adding proper error handling for disconnects, multiple clients with threading, and storing keys securely
