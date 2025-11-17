import foampy,menu,make

while True:
    choice=menu.root()
    if choice==1:
        task=menu.p(1)
        if   task==1: foampy.update_p1()
        elif task==2: foampy.delete_p1()
        elif task==3: make.p1
        elif task==4: foampy.postProcessing_p1()
        elif task==5: foampy.foamRun_p1()
        elif task==6: foampy.parallelRun_p1()
        elif task=='quit':print('Process Exiting...');break
        

    elif choice==2:
        task=menu.p(2)
        if   task==1: foampy.update_p2()
        elif task==2: foampy.delete_p2()
        elif task==3: make.p2
        elif task==4: foampy.postProcessing_p2()
        elif task==5: foampy.foamRun_p2()
        elif task==6: foampy.parallelRun_p2()
        elif task=='quit':print('Process Exiting...');break

    elif choice==3:
        task=menu.check()
        if   task==1: make.check
        elif task==2: foampy.forces_check()
        elif task==3: foampy.foamRun_check()
        elif task==4: foampy.decompose_check()
        elif task=='quit':print('Process Exiting...');break

    elif choice is None:print('제대로 입력하세요 좀')
    elif choice=='quit':print('Process Exiting...');break
    else:print('[Fatal] Invalid Choice')