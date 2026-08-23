from modelscope import snapshot_download
print("Bharat-Omni Base Model Download ho raha hai... Qwen/Qwen3-Omni-30B-A3B-Instruct")
snapshot_download('Qwen/Qwen3-Omni-30B-A3B-Instruct', local_dir='./models/Bharat-Omni-Base')
print("✅ Ho gaya! Model models/Bharat-Omni-Base me hai")
