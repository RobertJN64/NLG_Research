def remove_quotes(x):
    if x[0] == '"' and x[-1] == '"':
        return x[1:-1].replace('""', '"')
    return x.replace('""', '"')

#INCORRECT, CORRECT
groups_quant = {}

def merge_groups(item):
    gram_list = ['grammar', 'typo', 'no space before "."', 'less mistakes']
    for g in gram_list:
        if g in item:
            return 'grammar'

    length_list = ['concise', 'short sentences', 'long sentences', 'less information', 'shorter']
    for g in length_list:
        if g in item:
            return 'length'

    if 'emotion' in item:
        return 'emotion'

    if '---' in item:
        return '-'

    details_list = ['detail', 'stats', 'facts', 'more info', 'opinions']
    for g in details_list:
        if g in item:
            return 'details'

    return item

def parse_group_item(ftype, cval, item):
    if cval == -1:
        return

    is_com = 'mc' in ftype
    item = merge_groups(item)
    if item in groups_quant:
        groups_quant[item][0] += (not is_com)
        groups_quant[item][1] += is_com

    else:
        groups_quant[item] = [int(not is_com), int(is_com)]


def parse_CSV():
    with open('qual.csv') as f:
        lines = [line.lower().strip().split('\t') for line in f.readlines()]

    lines = lines[1:]
    for line in lines:
        ftype = line[0]
        line = line[1:]
        for item in line:
            item = remove_quotes(item)
            item = item.split(' ')
            cval = item[0]
            item = ' '.join(item[1:])
            parse_group_item(ftype, int(cval), item)

parse_CSV()
print("Category\tOpen Source\tCommercial")
l = sorted(list(groups_quant.items()), key=lambda x:x[1][0] + x[1][1], reverse=True)
for r in l:
    print(r[0], r[1][0], r[1][1], sep='\t')