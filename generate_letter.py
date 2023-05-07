import openai
import sys
import os

# Set up the OpenAI API client
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def generate_letter(politician_name, shooting_city_name, shooting_date):
    prompt = f"Write a polite but firm letter to {politician_name} to protest gun violence, citing the tragedy in {shooting_city_name} on {shooting_date}. Encourage the politician to pass meaningful and substantive gun safety legislation."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def save_to_markdown(content, filename):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_letter.py politician_name shooting_city_name shooting_date")
        sys.exit(1)

    politician_name = sys.argv[1]
    shooting_city_name = sys.argv[2]
    shooting_date = sys.argv[3]

    letter = generate_letter(politician_name, shooting_city_name, shooting_date)
    print("Generated letter:")
    print(letter)

    markdown_filename = f"letter_to_{politician_name.replace(' ', '_')}.md"
    save_to_markdown(letter, markdown_filename)
    print(f"Letter saved to {markdown_filename}")
