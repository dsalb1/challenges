#pip install requests
import requests

"""
a function that takes a url and an object id and makes an http delete request to that url.
Prints the response (which is now empty) and the status_code to the terminal
"""

def delete_to_do(url, id):
    url = url + "/" + str(id)
    response = requests.delete(url)
    print(response.text)
    print(response.status_code)

if __name__ == "__main__":
    url = 'http://jsonplaceholder.typicode.com/todos'
    id = 21
    #get_response = requests.get('http://jsonplaceholder.typicode.com/todos/21')
    #print(get_response.text)
    #print(get_response.status_code)
    delete_to_do(url, id)