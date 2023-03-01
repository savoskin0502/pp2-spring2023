import shutil


# shutil.move(  # rename or move
#     # source, destination
    # './tt',
    # './t1'
# )
# shutil.move('./t1/rawdata.txt', '.')
# shutil.copy('rawdata.txt', './t1/a.txt')
# shutil.rmtree('./t1')
shutil.make_archive(
    './a',
    'zip',
    '.'
)
