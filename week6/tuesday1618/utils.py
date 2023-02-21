def read_file(fpath: str):
    with open(fpath, mode='r', encoding='utf8') as f:
        return f.read()
