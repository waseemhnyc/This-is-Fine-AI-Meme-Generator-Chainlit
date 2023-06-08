from langchain.schema import SystemMessage
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

import chainlit as cl

import random, requests, os

IMGFLIP_USERNAME = os.environ.get('IMGFLIP_USERNAME')
IMGFLIP_PASSWORD = os.environ.get('IMGFLIP_PASSWORD')

def get_random_temperature():
    return random.choice([0.1 * i for i in range(1, 11)])

def get_meme_text(user_input):
    chat_model = ChatOpenAI(temperature=get_random_temperature(), model_name="gpt-4")

    response_schemas = [
        ResponseSchema(name="first", description="Describes a relatable, often distressing situation that should be addressed seriously but is being ignored"),
        ResponseSchema(name="second", description="Depicts the ironic or funny reaction to the situation, typically nonchalant or grossly under-reacting, signifying the phrase 'This is Fine'"),
    ]

    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessage(content="You can create viral memes and specialize in the 'This is Fine' meme. Memes must be relatable, brief, unexpected, ironic, and funny. Do not use the word 'me'."),
            HumanMessagePromptTemplate.from_template("Generate a meme about:\n{topic}.\n{format_instructions}")
        ],
        input_variables=["topic"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(topic=str(user_input))
    output = chat_model(_input.to_messages())
    response = output_parser.parse(output.content)
    return response

def this_is_fine_meme_generator(user_input):
    response = get_meme_text(user_input=user_input)
    first_text = response['first']
    second_text = response['second']

    url = "https://api.imgflip.com/caption_image"

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    params = {
        "template_id": 55311130,
        "username": IMGFLIP_USERNAME,
        "password": IMGFLIP_PASSWORD,
        "font": "impact",
        "text0": first_text,
        "text1": second_text,
    }

    response = requests.post(url, headers=headers, data=params)

    try:
        new_image_url = response.json()['data']['url']
        return new_image_url
    except:
        print(response.json())

@cl.on_message
def main(message: str):
    image_url = this_is_fine_meme_generator(user_input=message)
    elements = [
        cl.RemoteImage(name="remote_image", url=image_url, display="inline")
    ]
    cl.Message(content=message, elements=elements).send()
