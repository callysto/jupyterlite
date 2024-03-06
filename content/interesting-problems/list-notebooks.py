import os
import json

readme = open('README.md', 'r')
contents = readme.read()
header = contents[:contents.find('##')+14]
readme.close()
readme = open('README.md', 'w')
readme.write(header)

url_stem = 'https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Finteresting-problems&branch=main&subPath=notebooks/'
for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.ipynb'):
            if not 'checkpoint' in filename:
                notebook_name_and_path = os.path.join(root, filename)
                notebook = json.load(open(notebook_name_and_path, encoding='utf-8'))
                second_cell = notebook['cells'][1]['source'][0]
                title = second_cell[2:second_cell.find('\n')]
                link = url_stem+filename+'&depth=1'
                code = '['+title+']('+link+')'
                readme.write(code)
                readme.write('\n\n')
readme.close()