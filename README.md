# How It Works

**Udderly Sneaky** is a tool designed for covert data transmission using PDF files and network sockets. This program utilizes 
 is a tool designed for covert data transmission using PDF files and network sockets. This program utilizes steganography to hide data within the metadata of PDF files and employs sockets for data transfer between a server and a client.

### Overview

1. **SOCKETS**: The server and the client hold a connection via a TCP Socket

2. **Steganography**: The encoder will hide your message as a zipped base 64 encoding into the Title field of the PDF.

This tool is ideal for scenarios where covert data transmission is needed within environments where PDFs are frequently used, and provides a discreet method for sending information over a network.
d

# Communication Protocol Setup

## Server User
1. Run the server Python file.
2. You should be presented with a hanging Python program.

## Client User
1. Run the client Python file.
2. You will be alerted of a successful connection by a prompt stating `"Data to send -> "`.
3. Enter the text you want to send to the server and hit Enter.
4. You will be prompted for the filename of the PDF where you want to encode the data.
5. Enter the PDF filename as a string. Ensure that the input matches the filename exactly, including the `.pdf` extension. This file should be in the same directory as the client Python program.
6. If the Python program hangs, you have successfully transmitted the information, and the connection is still active.

## Server User
1. You will be alerted of a successful connection by a prompt stating `"Data to send -> "`.
2. Enter the text you want to send to the client and hit Enter.
3. You will be prompted for the filename of the PDF where you want to encode the data.
4. Enter the PDF filename as a string. Ensure that the input matches the filename exactly, including the `.pdf` extension. This file should be in the same directory as the server Python program.
5. If the Python program hangs, you have successfully transmitted the information, and the connection is still active.

## Loop
- This process will loop.

## Termination
- Either user can terminate the communication by ending the Python program with `^C` at any time.
