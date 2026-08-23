# Bharat-Omni Training Script - All-to-All
# Base: Qwen/Qwen3-Omni-30B-A3B-Instruct

import argparse

print("🇮🇳 Bharat-Omni Training Shuru...")

# Yaha swift / LLaMA-Factory ka code ayega
# Demo ke liye abhi sample check kar rahe hain

from pathlib import Path
import json

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', default='data/sample.json')
args = parser.parse_args()

with open(args.dataset, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"✅ Dataset Loaded: {len(data)} samples")
for i, sample in enumerate(data[:2]):
    print(f"\nSample {i+1}: {sample['messages'][0]['content'][:80]}...")

print("\nAgla Step:")
print("swift sft --model ./models/Bharat-Omni-Base --dataset data/sample.json --train_type lora --lora_rank 64")

print("\nJai Hind! Bharat-Omni Ready ho raha hai!")
