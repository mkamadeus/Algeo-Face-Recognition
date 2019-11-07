import os
import splashScreen as ss

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#009688 bold',
    Token.Instruction: '#FFC107',  # default
    Token.Answer: '#4CAF50 bold',
    Token.Question: '',
})

def promptInput():
    os.system('cls')
    ss.printPakRinaldi()

    os.system('cls')

    questions = [
    {
        'type': 'confirm',
        'name': 'extract_database',
        'message': 'Do you want to extract features from the image database?',
        'default': False
    },
    {
        'type': 'list',
        'name': 'similarity_method',
        'message': 'Choose your method:',
        'choices': ['Euclidean','Cosine'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'rawlist',
        'name': 'result_count',
        'message': 'How many results you want to be shown?',
        'choices': ['1','2','3','4','5'],
        'default': '2',
        'filter': lambda val: int(val)
    },
    {
        'type': 'list',
        'name': 'output_mode',
        'message': 'Choose output mode:',
        'choices': ['Percentage','Decimal'],
        'default': 'percentage',
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'comparison_mode',
        'message': 'Choose comparison mode:',
        'choices': ['Strict','Loose'],
        'default': 'percentage',
        'filter': lambda val: val.lower()
    },
    {
        'type': 'confirm',
        'name': 'randomize',
        'message': 'Randomize query?:',
        'default': True,
    },
    ]

    answers = prompt(questions, style=style)
    # pprint(answers)
    return answers