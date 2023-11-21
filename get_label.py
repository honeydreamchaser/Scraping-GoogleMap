import requests
import re
from bs4 import BeautifulSoup

url = "https://www.google.com/maps/d/viewer?mid=1lV1VB6i_FJcFOB7l45uQHwrT5K2cHEkU&ll=53.302057596360065%2C-1.1544521152145024&z=8"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html5lib')
# data = {}
# data['html'] = str(soup)
# with open("output.json", 'w') as json_file:
#     json.dump(data, json_file)

# Find the elements containing the address data
address_elements = soup.find_all('script')[1]
variables_dict = {}
variables = address_elements.string.replace('}', '').split(';')
for variable in variables:
    variable = variable.strip()
    if variable.startswith('var'):
        variable_name, variable_value = variable.split('=')
        variable_name = variable_name.replace('var', '').strip()
        variable_value = variable_value.strip()
        variables_dict[variable_name] = variable_value

pattern = r'[\w]* [\w]* - [\w ]*'
matches = re.findall(pattern, variables_dict['_pageData'])
matches = list(set(matches))
with open('names.txt', 'w') as output:
    for match in matches:
        output.write(match + '\n')