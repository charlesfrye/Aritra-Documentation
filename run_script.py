import os

list_dir = os.listdir('CODE')
for dir in list_dir:
    list_file = os.listdir('CODE/{}'.format(dir))
    if not os.path.exists('DOCS/{}'.format(dir)):
        os.mkdir('DOCS/{}'.format(dir))
    for f in list_file:
        f_n = f.split('.')[0]
        os.system("python doc_gen.py CODE/{0}/{1}.py DOCS/{0}/{1}.md".format(dir,f_n))