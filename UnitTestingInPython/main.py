import requests

def len_joke():
    joke = get_joke()
    # print('The joke from get_joke():', joke)
    return (len(joke))

def get_joke():
    url = 'https://type.fit/api/quotes'
    response = requests.get(url)
    print(response.json()[0]['text'])

    if response.status_code == 200:
        joke = response.json()[0]['text']
    else:
        joke = 'No jokes'

    return joke 
# response[0]

if __name__ == '__main__':
    print(get_joke())
