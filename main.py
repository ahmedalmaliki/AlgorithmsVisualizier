from tkinter import *
top = Tk()
top.title("Algorithms Visualizer")
top.geometry("1580x800")
###Binary Search###

class BinarySearchForPeakFiding():
    def __init__(self):
        self.infoLabel = Label(top, bg='#a8dadc', height=5, width=1580,
                               highlightbackground='black', relief='solid', borderwidth=2,
                               text = 'Peak finding with binary search is an algorithm used to find a peak in an array of integers.\nTime Complexity: O(Logn).\n Space complexity: O(1).')
        self.button = Button(top, bg='#a8dadc', height = 2, width= 5, relief = 'raised',
                             text= "Start")
    def render(self):
        self.infoLabel.pack(side =BOTTOM)
        self.button.place(relx = 0.95, rely = 0.1)
    @staticmethod
    def algo_body( array, high, low):
        mid = int(low + ((high - low)/ 2))
        if high >= low :
            if  array[mid] >= array[mid - 1] and array[mid] >= array[mid + 1]:
                return array[mid]
            elif array[mid - 1] > array[mid]:
                return  BinarySearchForPeakFiding.algo_body( array = array ,
                                                             high = mid -1, low = low)
            elif array[mid + 1] > array[mid]:
                return BinarySearchForPeakFiding.algo_body(array = array,
                                                           high = high, low=mid + 1)
            else:
                return -1

top.configure(bg='white' )
peak_finder = BinarySearchForPeakFiding()
peak_finder.render()
top.mainloop()