import numpy as np
class GridAnalyzer:
        def __init__(self):
            self.grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        def view_slice(self,choice):
            if choice==1:
               first_row=self.grid[0,:]
               return first_row
            elif choice==2:
                center_row=self.grid.diagonal()
                return center_row
            else:
                last_row=self.grid[-1,:]
                return last_row

user_input=int(input("Which Row You Want to see Select One \n 1) First Row \n 2)Center Row \n 3)Last Row: "))
analyzer=GridAnalyzer()
result=analyzer.view_slice(user_input)
print(result)