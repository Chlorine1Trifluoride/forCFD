import pyfoam, menu

pyfoam.launch()
ans = None


menu.main()
ans =  input("enter the NUMBER of task you want: ")
choice = int(ans)

if   choice ==     1:  import make

elif choice ==     6:  pyfoam.postProcessing()

elif choice ==     7:  pyfoam.foamRun()

elif choice ==     8:  pyfoam.parallelRun()

else: print("[INVALID CHOICE]")

