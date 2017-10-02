#pip install requests
import requests
#pip install json
import json

"""assuming the todo with the highest id is the most recent, prints each id,
    beginning with num (i.e., the most recently created todo), until a count of num is reached"""
def get_to_do(url, num):
    response = requests.get(url)
    todos = json.loads(response.text)
    count = 1
    while count <= num:
        print(todos[-count])
        count += 1

if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/todos'
    get_to_do(url, 200)