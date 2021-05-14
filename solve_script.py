from sudoku import solve_all
import grids
import sys

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        
        grid = str(sys.argv[1])

        # check is user is using grids.py options
        try:
            grid = getattr(grids,grid)
        except:
            print("The selected grid option doesn't exist. Will verify your grid.")

        # check grid for right length (81)
        if len(grid) != 81:
            print("Provided grid is has %s numbers. Using sample grid." % (len(grid)))
            grid = grids.grid1

        # check grid has valid characters . or integers 0-9
        valid = '.0123456789'
        for c in grid:
            if c not in valid:
                print("Provided grid has character that is not . or integer 0-9. Using sample grid.")
                grid = grids.grid1
                break

    else:
        grid = grids.grid1
        print("No grid provided; using sample grid. Perhaps check example grids in grids.py")

    #solve_all([grid2,grid1])
    solve_all([grid])