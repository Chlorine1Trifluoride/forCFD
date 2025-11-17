def boxheader(title):
    padding = int((35-len(title))/2)
    print('┌'+'─'*padding+title+padding*'─'+'┐')
def boxcontent(string):
    print('│'+'  '+string+' '*(33-len(string))+'│')
def boxfooter():
    print("└───────────────────────────────────┘")
def box(title, contents):
    boxheader(title)
    for string in contents:
        boxcontent(string)
    boxfooter()
def p2():
    contents = [
        "",
        "",
        "I.   Case management",
        "",
        "  [  1  ]  Update FILE",
        "  [  2  ]  Update DIRECTORY",
        "",
        "  [  3  ]  Delete FILE",
        "  [  4  ]  Delete DIRECTORY",
        ''
        '  [  5  ]  initialize',
        "",
        "",
        "II.  OpenFOAM",
        "",
        "  [  6  ]  postProcessing",
        "  [  7  ]  foamRun",
        "  [  8  ]  PARALLEL foamRun",
        "",
        ""
        ]
    title = '[ AUTO  PROCESSER: p2 ]'
    box(title, contents)

