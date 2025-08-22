CS336 Project 2: Natural Language to SQL

Team Members
- Benjamin Yu (bmy25)
- Krisha Patel (ksp162)
- Andrew Menyhert (amm926)
- Sheldon Yoon (ssy38)

Contributions
- Benjamin Yu & Krisha Patel: Wrote 'sshtunnel.py' 'stub.py' and 'database_llm', built LLM prompt structure and extraction logic, and integrated full loop logic.
- Andrew Menyhert & Sheldon Yoon: Handled LLM model download/setup and helped with 'llama-cpp-python' installation and troubleshooting on Windows 
                                    and helped configure and test 'sshtunnel.py' 'stub.py' and 'database_llm' on iLab.

Model Used:
https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF/blob/main/Phi-3.5-mini-instruct-Q4_K_M.gguf
- Download model to folder scripts are located in.
- Place stub.py in your home directory in iLab.

Challenges
- Installing 'llama-cpp-python' on Windows due to C++ toolchain requirements.
- Ensuring the local LLM produced accurate SQL from natural language prompts.
- Debugging iLab-side database errors caused by malformed or incomplete SQL.
- Creating a specific enough schema prompt to ensure that the LLM doesn't come up with non-existent table names.

Interesting Aspects
- Local models like Phi 3.5 Mini Instruct can reliably generate SQL queries when given well-formatted schemas.
- Full pipeline integration (LLM → SSH → SQL → output) provided valuable practice in real-world secure system design.

Extra Credit
- Extra credit (stdin-based data passing instead of argument passing) was not implemented.

AI Transcripts
We used multiple AI tools throughout the project for debugging and prompt optimization, including:
- OpenAI ChatGPT (GPT-4-turbo) for error resolution and prompt structuring

All AI transcripts are located in the "Group 20 - Project 2 Transcripts" file.