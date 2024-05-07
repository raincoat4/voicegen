#!/bin/bash

# Start frontend
cd frontend
npm run dev &

# Start backend
cd ../backend
python3 predict.py
