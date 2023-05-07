# Gun Violence Protest Letter Generator

A python script for creating letters to politicians asking for gun reform. 

Inspired by: https://astral.camp/@endeavorance/110324509173162279


This script generates a polite but firm letter to a politician, protesting gun violence and citing a specific tragedy. It encourages the politician to pass meaningful and substantive gun safety legislation. The output letter is saved in a markdown file.

## Requirements

- Python 3.6 or higher
- An OpenAI API key. You can sign up for an API key at https://beta.openai.com/signup/.
- The `openai` Python library. Install it using pip:

```bash
pip3 install openai
```

## Usage

1. Clone this repository or download the `generate_letter.py` script.
2. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key:

\```bash
export OPENAI_API_KEY=your_api_key_here
\```

Replace `your_api_key_here` with your actual API key.

3. Run the script with the required parameters: politician_name, shooting_city_name, and shooting_date:

```bash
python3 generate_letter.py "John Doe" "Anytown" "2023-05-01"
```

Replace the example values with the appropriate politician name, city name, and date.

The script will generate a letter, print it to the console, and save it to a markdown file with a name like `letter_to_John_Doe.md`.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.

## This is a start, not an end

This is a simple script. Please fork it, augment it, change it, improve upon it. This is meant to get the ball rolliing. If the bad guys can use LLMs for their goals, so can we.


