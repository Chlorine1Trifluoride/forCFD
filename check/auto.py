import pyfoam, menu

pyfoam.launch()
ans = None


menu.main()
ans =  input("enter the NUMBER of task you want: ")
choice = int(ans)

if   choice ==     1:  import make
    
elif choice ==     2:  pyfoam.postProcessing()

elif choice ==     3:  pyfoam.foamRun()

elif choice ==     4:  pyfoam.parallelRun()

else: print("[INVALID CHOICE]")

