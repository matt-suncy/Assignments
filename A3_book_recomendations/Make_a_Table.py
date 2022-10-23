'''
   20220204
   
   Robin Dawes
'''

import tkinter as tk 

window = tk.Tk()
window.geometry("1200x800")

col_0_head = tk.Label(window, text = "     n     ", pady = 20)  
# pady = 20 gives some vertical separation between this row and the next
col_0_head.grid(row = 0, column = 0)

col_1_head = tk.Label(window, text = "     n**2     ")
col_1_head.grid(row = 0, column = 1)

col_2_head = tk.Label(window, text = "     n**3     ")
col_2_head.grid(row = 0, column = 2)

rows = 10
columns = 3
for i in range(rows): 
   n = i + 1
   for j in range(columns): 
      exponent = j+1
      value = n**exponent
      x = tk.Label(window, text = str(value))   
      # note that tkinter doesn't care that we re-use the variable x
      x.grid(row = n, column = j)
      
window.mainloop()