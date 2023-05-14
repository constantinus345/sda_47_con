from configs import  cheia

import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = cheia

max_tokens_x = 300
prompt_x = 'scrie functia fibonacci in python cu metoda recursiva'
response = openai.Completion.create(model="text-davinci-003",
                                    prompt=prompt_x,
                                    temperature=0,
                                    max_tokens=max_tokens_x)
textul_raspuns = response["choices"][0]["text"]
print(textul_raspuns)