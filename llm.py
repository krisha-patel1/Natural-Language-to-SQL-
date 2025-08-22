import pandas as pd
from llama_cpp import Llama


# Path to your downloaded model
model_path = "./Phi 3.5 Mini Instruct GGUF.gguf"

# Load the model
llm = Llama(model_path=model_path, n_ctx=2048)  # you can adjust n_ctx if you want larger context windows

# Ask something
prompts = [
    "Translate 'Hello, world!' to French.",
    "Summarize the main points of the following text: 'The quick brown fox jumps over the lazy dog.'",
    "List three famous scientists."
    ]

output_data = []

for prompt in prompts:
    output = llm(prompt)
    generated_text = output["choices"][0]["text"].strip()
    output_data.append({"prompt": prompt, "generated_text": generated_text})

# Create a pandas DataFrame
df = pd.DataFrame(output_data)

# Specify the CSV filename
csv_filename = "single_llm_output.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"Output saved to {csv_filename} using pandas.")

