import helper

with open('Rebirth.txt') as file:
    id = 0
    for line in file:
        line = line.split(',')
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

        # print(a.lower()+name.lower()+'rebirth', ',', number, ',', title, ',', arc, ',', price)

        name_vol = helper.convert_title(a+name, 'rebirth')

        print('INSERT INTO {} VALUES("{}", "{}", "{}", "{}", "{}");'.format(name_vol, id, number, title, arc, price))
