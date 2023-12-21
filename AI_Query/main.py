from openai import OpenAI

client = OpenAI(api_key='your api token here...')

# Set your OpenAI API key

def generate_sql_query(table_name, column_name, user_input):
    # Use GPT-3 to generate SQL query
    prompt = f"Generate a parameterized SQL query to insert data into the {table_name} table. The query should insert '{user_input}' into the '{column_name}' column."
    
    response = client.completions.create(model="text-davinci-003",  # Specify the GPT-3 model
    prompt=prompt,
    max_tokens=100)

    # Extract the generated SQL query from the GPT-3 response
    generated_query = response['choices'][0]['text'].strip()

    return generated_query

table_name = "users"
column_name = "username"
user_input = "JohnDoe"

sql_query = generate_sql_query(table_name, column_name, user_input)
print(sql_query)