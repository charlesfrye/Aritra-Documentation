import os

list_dir = os.listdir('CODE')
for dir in list_dir:
    list_file = os.listdir('CODE/{}'.format(dir))
    if not os.path.exists('DOCS/{}'.format(dir)):
        os.mkdir('DOCS/{}'.format(dir))
    for f in list_file:
        # print("python doc_generator.py CODE/{0}/{1} DOCS/{0}/{1}".format(dir,f))
        os.system("python doc_generator.py CODE/{0}/{1} DOCS/{0}/{1}".format(dir,f))