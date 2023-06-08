# This is Fine Meme Generator

Built with [LangChain](https://github.com/hwchase17/langchain) and [Chainlit](https://github.com/Chainlit/chainlit)

1. Input a topic
2. Generate your meme

![image info](https://i.imgflip.com/7opvgm.jpg)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Installed a recent version of Python (3.7 or newer) installed and a way to create virtual environments (virtualenv or conda)
- Created OpenAI API account and obtain an OpenAI API key
- Created a Imgflip account and save your username and password

## Getting Started

Clone the repo

```bash
git clone https://github.com/waseemhnyc/...
```

Create a virutalenv and source the environment

```bash
python3 -m venv myenv
source venv/bin/activate
```

Install the necessary libraries

```bash
pip install -r requirements.txt
```

Create a .env file and input your OpenAI API Key and Imgflip credentials in the file

```bash
cp .env.example .env
```

## Usage

To run the program, run the following command in the terminal:

```bash
chainlit run app.py
```

## Questions or Get in Touch

- Twitter: https://twitter.com/waseemhnyc
- Email: waseemh.nyc@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.
