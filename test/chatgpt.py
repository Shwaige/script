import openai

# Set your API key
openai.api_key = "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"
# Use the GPT-3 model
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="用python写从0开始自增,并且自增后记住上一次自增的数字",
    max_tokens=1024,
    temperature=0.5
)
# Print the generated text
print(completion.choices[0].text)

