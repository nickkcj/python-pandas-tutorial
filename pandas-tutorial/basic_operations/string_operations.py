import pandas as pd

# Create sample data with text
df = pd.DataFrame({
    'name': ['John Doe', 'jane smith', 'BOB JOHNSON', 'Alice Brown', 'charlie wilson'],
    'email': ['john@email.com', 'jane@gmail.com', 'bob@yahoo.com', 'alice@hotmail.com', 'charlie@email.com'],
    'phone': ['123-456-7890', '(555) 123-4567', '555.987.6543', '123 456 7890', '555-123-4567'],
    'address': ['123 Main St, New York, NY', '456 Oak Ave, Los Angeles, CA', '789 Pine Rd, Chicago, IL', '321 Elm St, Houston, TX', '654 Maple Dr, Phoenix, AZ']
})

print(f"Original data:\n{df}")

# Basic string operations
df['name_upper'] = df['name'].str.upper()
df['name_lower'] = df['name'].str.lower()
df['name_title'] = df['name'].str.title()
df['name_length'] = df['name'].str.len()

print(f"String transformations:\n{df[['name', 'name_upper', 'name_lower', 'name_title', 'name_length']]}")

df[['first_name', 'last_name']] = df['name'].str.split(' ', expand=True)
print(f"Split names:\n{df[['name', 'first_name', 'last_name']]}")

df['email_domain'] = df['email'].str.split('@').str[1]
print(f"Email domains:\n{df[['email', 'email_domain']]}")

gmail_users = df[df['email'].str.contains('gmail')]
print(f"Gmail users:\n{gmail_users[['name', 'email']]}")

df['phone_clean'] = df['phone'].str.replace(r'[^\d]', '', regex=True)
df['phone_formatted'] = df['phone_clean'].str.replace(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', regex=True)
print(f"Phone formatting:\n{df[['phone', 'phone_clean', 'phone_formatted']]}")

df['state'] = df['address'].str.extract(r', ([A-Z]{2})$')
df['city'] = df['address'].str.extract(r', ([^,]+), [A-Z]{2}$')
print(f"Address extraction:\n{df[['address', 'city', 'state']]}")

df['first_initial'] = df['first_name'].str[0]
df['last_initial'] = df['last_name'].str[0]
df['initials'] = df['first_initial'] + '.' + df['last_initial'] + '.'
print(f"Initials:\n{df[['name', 'initials']]}")

