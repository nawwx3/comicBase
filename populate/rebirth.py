# works on server
# import .myWebsite.comicBase.helper as helper

# works at home
import sys
sys.path.append('../myWebsite/comicBase')

import helper
import glob

for file_name in glob.glob('./input_files/*.txt'):
    with open(file_name) as file:
        id = 0
        for line in file:
            line = line.split('~')
            id += 1
            try:
                line2 = line[2].split('#')
                number = line2[1]
            except Exception:
                number = 1

            name = line2[0]

            if line[7] == 'Annual\n':
                a = 'annual '
            elif line[7] == 'DC Universe Rebirth\n':
                a = 'rebirth '
            else:
                a = ''

            title = line[3]
            price = line[6]
            arc = line[4]

            name_vol = helper.convert_title(a+name, 'rebirth')

            print('INSERT INTO {} VALUES("{}", "{}", "{}", "{}", "{}");'.format(name_vol, id, number, title, arc, price))
