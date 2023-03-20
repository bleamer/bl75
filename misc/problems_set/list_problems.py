# Python code to fetch LC problems from a CSV 
# and tabulate them basic no. of times they have been asked at G
# Reference: https://raw.githubusercontent.com/hxu296/leetcode-company-wise-problems-2022/main/companies/Google.csv

import csv
import requests
from tqdm import tqdm

# URL of the CSV file
url = "https://raw.githubusercontent.com/hxu296/leetcode-company-wise-problems-2022/main/companies/Google.csv"

class Data:
    def __init__(self, col1, col2, col3):
        self.url = col1
        self.title = col2
        self.n_asked = col3
        self.difficulty = None

    @property
    def difficulty(self):
        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, v):
        if not v.isdigit():
            v = 'Easy'
        self._difficulty = str(v)

    @difficulty.getter
    def difficulty(self):
        return self._difficulty

    def __str__(self) -> str:
        return (f'url:{self.url}, col2:{self.col2}, n_asked:{self.n_asked}, difficulty:{self.difficulty}')
    
def get_csv_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        csv_data = response.content.decode('utf-8')
        reader = csv.reader(csv_data.splitlines(), delimiter=',')
        next(reader)
        data = []
        for row in reader:
            data.append(Data(row[0], row[1], row[2]))
        return data
    else:
        return None

def get_problem_difficulty(data:Data):

    import requests
    from bs4 import BeautifulSoup

    # LeetCode problem URL
    url = data.url

    problem_id = url.split('/')[-2]

    # set up the GraphQL query
    # query = '''
    # query getQuestionDetail($titleSlug: String!) {
    #     question(titleSlug: $titleSlug) {
    #         difficulty
    #     }
    # }
    query = '''
    query questionTitle($titleSlug: String!) {  
        question(titleSlug: $titleSlug){
            questionId    
            questionFrontendId    
            title    
            titleSlug    
            isPaidOnly    
            difficulty    
            likes    
            dislikes  }
        }    

    
    '''

    # set up the variables for the GraphQL query
    variables = {
        'titleSlug': problem_id
    }
    json = {'query': query, 'variables': variables}
    # make the request to the GraphQL API
    response = requests.post('https://leetcode.com/graphql', json=json)
    try:
        # parse the JSON response and extract the difficulty level
        response_data = response.json()['data']
        difficulty = response_data['question']['difficulty']
    except:
        difficulty = 'unknown'
    return difficulty    

if __name__ == '__main__':
    data = get_csv_data(url)
    # data = data[:20]
    for d in tqdm(data):
        d.difficulty = get_problem_difficulty(d)
    data = [r for r in data if r.n_asked.isdigit()]
    data = sorted(data, key=lambda x: (str(x.difficulty), int(x.n_asked)), reverse=True)
    header = '''
| URl | Title | Asked# | Difficulty |
|--- |--- |--- |--- |
'''
    rows = ''
    for d in data:
        rows += f"| {d.url} | {d.title} | {d.n_asked} | {d.difficulty} |\n"
    table = header + rows

    with open("misc/LC-GOOG.md", "w") as f:
        f.write(table)

print("Table exported as Markdown!")