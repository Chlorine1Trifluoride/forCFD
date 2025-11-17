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
def answer():
    try: 
        choice=input("Enter NUMBER of task: ")
        if choice=='q': return 'quit'
        else:
            return int(choice)
    except ValueError:return None


def root():
    contents=['',
              '',
              '  [  1  ]  p1',
              '',
              '  [  2  ]  p2',
              '',
              '  [  3  ]  check',
              '',
              '',
              '  [  q  ]  quit'
              '',
              ''
              ]
    title = '[ Directories ]'
    box(title, contents)
    return answer()



def p(n):
    contents = [
        "",
        "",
        "I.   Case management",
        "",
        "  [  1  ]  Update File or Folder",
        "",
        "  [  2  ]  Delete File or Folder",
        '',
        '  [  3  ]  Initialize',
        "",
        "",
        "II.  OpenFOAM",
        "",
        "  [  4  ]  postProcessing",
        '',
        "  [  5  ]  foamRun",
        '',
        "  [  6  ]  PARALLEL foamRun",
        "",
        "",
        '',
        '',
        '  [  q  ]  quit'
        '',
        ''
        ]
    title = f'[ AUTO  PROCESSER: p{n} ]'
    box(title, contents)
    return answer()


def check():
    contents = [
        "",
        "",
        "I.   Case management",
        '',
        '  [  1  ]  Initialize',
        "",
        "",
        "II.  OpenFOAM",
        "",
        "  [  2  ]  postProcessing",
        '',
        "  [  3  ]  foamRun",
        '',
        "  [  4  ]  PARALLEL foamRun",
        "",
        "",
        '',
        '',
        '  [  q  ]  quit'
        '',
        ''
        ]
    title = '[ AUTO PROCESSER: check ]'
    box(title, contents)
    return answer()
    

    