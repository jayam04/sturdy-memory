#!/usr/bin/env python3

import sys, os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def custom_read(f):
    for line in f.readlines():
        if line.strip() != None:
            print(line, end="")

filepath = sys.argv[1] 
filepath_splited = filepath.split('/')

if len(filepath_splited) == 1:
    contest = '.'
else:
    contest = '/'.join(filepath_splited[:-1])
problem = filepath_splited[-1]


files = os.listdir(contest)
# print(files)

for file in files:
    if file.startswith(problem):
        extension = file.split('.')[-1]
        if extension == 'py':
            continue
        if extension == 'inp':
            # print(f"Input {file.split('.')[0][1:]}:")
            with open(contest + '/' + file) as f:
                custom_read(f)
            # print(f"Actual Output {file.split('.')[0][1:]}:")
            print(f"\n-------------------------------{bcolors.OKBLUE}")
            os.system(f"python3 {filepath}.py < {contest}/{file}")
            print(bcolors.OKGREEN, end="")
            try:
                with open(contest + '/' + file.split('.')[0] + '.out') as f:
                    # print(f"Required Output {file.split('.')[0][1:]}:")
                    print(f.read())
            except:
                print("No output file found!")
            print(bcolors.ENDC)
            print()
        # os.rename(file, problem + '.cpp')
    else:
        continue
