#!/bin/bash
echo "Bharat-Omni Setup Shuru..."
pip install -r requirements.txt
pip install modelscope
modelscope download --model Qwen/Qwen3-Omni-30B-A3B-Instruct --local_dir ./models/Bharat-Omni-Base
echo "Ho gaya! Model models/ folder me hai"
