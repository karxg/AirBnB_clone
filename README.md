# AirBnB Clone Project Collaboration 🏠✨

## Background Context

Welcome to our collaborative effort to create an AirBnB clone! Before diving into the project, let's familiarize ourselves with the concept of AirBnB and its functionalities. Please refer to the [AirBnB concept page](https://www.airbnb.com/).

## Participants

### Participant 1: Ahmed Magdy

Hey everyone! I'm Ahmed, and I'm excited to work on this project. My background is in web development, and I'll be focusing on implementing the command-line interpreter and developing the serialization/deserialization flow 🚀

### Participant 2: Kareem Farrag

Hey, I'm Kareem! I'm passionate about backend development and testing. I'll be working on creating classes for AirBnB objects, implementing the storage engine, and writing unit tests to ensure everything works smoothly. 💻🔍

## Tasks Description

Our project consists of several tasks aimed at achieving the following objectives:

- Implement a command interpreter to manage AirBnB objects.
- Establish a parent class (BaseModel) for object initialization, serialization, and deserialization.
- Develop a flow for serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create classes for AirBnB objects (User, State, City, Place, etc.) inheriting from BaseModel.
- Implement the first abstracted storage engine: File storage.
- Write unit tests to validate all classes and the storage engine.

## What's a Command Interpreter?

The command interpreter allows users to perform various operations on AirBnB objects, including:

- Creating new objects (e.g., User, Place).
- Retrieving objects from files or databases.
- Performing operations on objects (counting, computing statistics, etc.).
- Updating attributes of objects.
- Deleting objects.

## Usage

Once the console application is running, you can use the following commands:

- quit: Exit the program.
- create [class_name]: Create a new instance of the specified class.
- show [class_name] [instance_id]: Display details of a specific instance.
- destroy [class_name] [instance_id]: Delete a specific instance.
- all [class_name] or all: Display details of all instances or of a specific class.
- update [class_name] [instance_id] [attribute_name] [attribute_value]: Update attributes of a specific instance.
- count [class_name]: Count the number of instances of a specific class.
- clear: Clear the console screen.

## Learning Objectives

By completing this project, we'll gain knowledge and skills in the following areas:

- Creating a Python package.
- Developing a command interpreter using the cmd module.
- Implementing Unit testing in a large project.
- Serializing and deserializing classes.
- Reading and writing JSON files.
- Managing datetime in Python.
- Understanding UUIDs.
- Utilizing *args and **kwargs in functions.
- Handling named arguments effectively.

## GitHub Repository

We've created a GitHub repository for our project collaboration. Each of us will have access to the repository to contribute code, documentation, and tests. Let's ensure smooth collaboration by following best practices and keeping our repository organized.

Let's embark on this journey together and create an amazing AirBnB clone! 💪🏼🏠✨
