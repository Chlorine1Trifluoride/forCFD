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
def check():
    contents = [
        "",
        "",
        "I.   Case management",
        ''
        '  [  1  ]  initialize'
        "",
        "",
        "II.  OpenFOAM",
        "",
        "  [  2  ]  postProcessing",
        "  [  3  ]  foamRun",
        "  [  4  ]  PARALLEL foamRun",
        "",
        ""
        ]
    title = '[ AUTO PROCESSER: check ]'
    box(title, contents)

