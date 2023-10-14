# Python code to fetch LC problems from a CSV 
# and tabulate them basic no. of times they have been asked at G
# Reference: https://raw.githubusercontent.com/hxu296/leetcode-company-wise-problems-2022/main/companies/Google.csv

import csv
import requests
from tqdm import tqdm

# URL of the CSV file
# url = "https://raw.githubusercontent.com/hxu296/leetcode-company-wise-problems-2022/main/companies/Google.csv"
url = "https://raw.githubusercontent.com/snehasishroy/leetcode-companywise-interview-questions/master/google.csv"

class Data:
    LC_PROB_URL_PREFIX = "https://leetcode.com"
    DIFF_SORT_ORDER = ["Easy","Medium", "Hard"]
    REGEX_FREQ = ""
    def __init__(self, col1, col2, col3, col4, col5, col6):
        self.title = col1
        self.url = col2
        self.premium = col3
        self.acceptance = col4
        self.difficulty = col5
        self.frequency = col6

    # @property
    # def difficulty(self):
    #     return self._difficulty
    
    # @difficulty.setter
    # def difficulty(self, v):
    #     if not v.isdigit():
    #         v = 'Easy'
    #     self._difficulty = str(v)

    # @difficulty.getter
    # def difficulty(self):
    #     return self._difficulty
    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter    
    def frequency(self, v):
        self._frequency = float(str(v).replace("%","").replace(";",""))

    @frequency.getter
    def frequency(self):
        return self._frequency

    def __str__(self) -> str:
        return (f'url:{self.url}, col2:{self.col2}, frequency:{self.frequency}, difficulty:{self.difficulty}')
    
def get_csv_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        csv_data = response.content.decode('utf-8')
        reader = csv.reader(csv_data.splitlines(), delimiter=',')
        next(reader)
        data = []
        for row in reader:
            data.append(Data(row[1], row[2],row[3], row[4],row[5], row[6]))
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
    # for d in tqdm(data):
    #     d.difficulty = get_problem_difficulty(d)
    # data = [r for r in data if r.n_asked.isdigit()]
    diff_sorting_key = lambda x: (Data.DIFF_SORT_ORDER.index(x), x) if x in Data.DIFF_SORT_ORDER else (len(Data.DIFF_SORT_ORDER), x)

    data = sorted(data, key=lambda x: (diff_sorting_key(x.difficulty), float(x.frequency)), reverse=True)
    header = '''
| URl | Title | Asked# | Difficulty |
|--- |--- |--- |--- |
'''
    rows = ''
    for d in data:
        rows += f"| {Data.LC_PROB_URL_PREFIX}{d.url} | {d.title} | {d.frequency} | {d.difficulty} |\n"
    table = header + rows

    with open("misc/problems_set/LC-GOOG.md", "w") as f:
        f.write(table)

print("Table exported as Markdown!")