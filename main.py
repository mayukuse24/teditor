while 1:
    text = ""
    stopword = "^"
    while True:
        line = raw_input()
        if line.strip() == stopword:
            break
        text += "%s\n" % line
    print text
