import glob
import re


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def get_id_dct(file):
    dct = {}
    with open(file, "r") as f:
        for line in f:
            if '>' in line:
                id = re.findall(r'(\w\w\_\d+\.\d).*', line)
                id = id[0]
                dct[id] = file
    return dct


def write_ko_id(ko_dct, present_dct, filename):
    fh = open(filename, 'w')
    for key, value in present_dct.items():
        if key in ko_dct:
            save_txt = "{}\t{}\n".format(key, ko_dct[key])
            fh.write(save_txt)
        else:
            save_txt = "{}\n".format(key)
            fh.write(save_txt)

    fh.close()


ko_dct = {}
ko_list_file = "Cyano/query.ko.txt"
with open(ko_list_file, 'r') as file:
    for line in file:
        line = line.strip()
        line_list = line.split('\t')
        if len(line_list) >1:
            ko_dct[line_list[0]] = line_list[1]

id_file = ""
path = "Cyano/protein_fasta/*"
file_list = glob.glob(path)
merged_dct = {}
for filename in file_list:
    print(filename)
    new_path = re.sub("protein_fasta", "KO", filename)
    print(new_path)
    file_dct = get_id_dct(filename)
    write_ko_id(ko_dct, file_dct, new_path)







