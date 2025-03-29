#!/bin/bash

# Ensure pip is available
/usr/bin/python3.9 -m ensurepip --upgrade

# Upgrade pip
/usr/bin/python3.9 -m pip install --upgrade pip

# Install dependencies from requirements.txt
/usr/bin/python3.9 -m pip install -r requirements.txt

# Create a build directory and copy necessary files
mkdir -p build
cp -r app.py vectorstore_manager.py text_extractor.py qa_retriever.py .env build/
