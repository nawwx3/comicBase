# works on server
database_location = '/var/www/myWebsite/myWebsite/comics_database.db'

# works at home
# database_location = 'comics_database.db'


def convert_title(issue_name, volume):
    issue_name = issue_name.lower()
    table_title = issue_name.lstrip().rstrip().replace(' ', '_')+'_'+str(volume)
    return table_title

def revert_title(title_name):
    title_info = title_name.split('_')
    volume = title_info[-1]  # the last one is the volume information
    issue_list = title_info[0:-1] # issue name is everything else
    issue = ''
    # reconstruct the issue name
    for word in issue_list:
        if issue != '':
            issue += ' '
        issue += word
    issue = issue.title()   # then make first lettes capital
    return issue, volume

def sort_tables(tables):
    # split them apart
    table_parts = []
    for table in tables:
        issue, volume = revert_title(table[0])
        table_parts.append([issue, volume])

    # sort them
    table_parts.sort()

    # put them back together`
    sorted_tables = []
    for table in table_parts:
        sorted_tables.append(convert_title(table[0], table[1]))

    return sorted_tables
