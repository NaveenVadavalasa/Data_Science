def read_replace_content(file, old_string, new_string):
    fp = open(file, 'r+')
    data = fp.read()
    new_data = data.replace(old_string, new_string)
    fp.write(new_data)

    fp.close()
    return "success"


read_replace_content("example.txt", "practice", "screeing")
