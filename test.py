from sudoku import solve_all
import os,time

if __name__ == "__main__":

    grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    grid2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    hard1  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'

    solve_all([hard1])

    # Tesseract-OCR testing
    image = "eurotext.png"
    output = "output"
    options = ""
    command = "tesseract images\\%s %s %s" % (image,output,options)

    os.system(command)
    time.sleep(2) # let output.txt get regenerated

    f=open("%s.txt" % output,"r",encoding="utf8")
    print(f.read())
    f.close()