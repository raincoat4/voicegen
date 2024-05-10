#!/bin/bash

# Start backend
cd backend
python3 predict.py &

# Start frontend
cd ../frontend
npm run dev 

