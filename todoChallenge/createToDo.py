#pip install requests
import requests
#pip install json
import json

"""
Does not work with jsonplaceholder's fake api.
ToDo class that includes both a constructor and a method that builds a representation 
of an instance of the class in JSON
"""
class ToDo:
    def __init__(self, userId, tdId, title, completed=False):
        self.userId = userId
        self.toDoId = tdId
        self.title = title
        self.completed = completed

    def build_json(self):
        data = {}
        data['userId'] = self.userId
        data['id'] = self.toDoId
        data['title'] = self.title
        data['completed'] = self.completed
        json_data = json.dumps(data)
        return json_data


"""
Given the argument 'url', makes a post request and prints out 
the response and the status code to the terminal.
"""
def create_to_do(url):
    response = requests.post(url)
    print(response.text)
    print(response.status_code)

if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/todos'
    create_to_do(url)