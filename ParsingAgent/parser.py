import os
import OpenAi


def getPrompt():
    with open('ParserPrompt.txt', 'r') as prompt_file:
        prompt = prompt_file.read()
    return prompt

def Parse(to_parse, description, output_example):
    parser = OpenAi(api_key=os.getenv('OPEN_AI_API'))
    prompt = getPrompt() + f'\n Argument 1: {to_parse}' + f'\n Argument 2: {description}' + f'\n Argument 3: {output_example}' 
    output = parser.chat.completions.create(
        model="gpt-4o",
        message=[
            {"role": "user", "content": prompt}
        ]
    )
    return output.choices[0].message.content