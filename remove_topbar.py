# https://stackoverflow.com/questions/30786337/tkinter-windows-how-to-view-window-in-windows-task-bar-which-has-no-title-bar/30819099#30819099

from ctypes import windll

class RemoveTopBar:
    # Defining functions
    GetWindowLongPtrW = windll.user32.GetWindowLongPtrW
    SetWindowLongPtrW = windll.user32.SetWindowLongPtrW

    # Constants
    GWL_STYLE = -16
    GWLP_HWNDPARENT = -8
    WS_CAPTION = 0x00C00000
    WS_THICKFRAME = 0x00040000

    def __init__(self, window=None):
        self.window = window
        self.main()

    def get_handle(self):
        self.window.update_idletasks()
        # This gets the window's parent same as `ctypes.windll.user32.GetParent`
        return self.GetWindowLongPtrW(self.window.winfo_id(), self.GWLP_HWNDPARENT)

    def main(self):
        hwnd = self.get_handle()
        style = self.GetWindowLongPtrW(hwnd, self.GWL_STYLE)
        style &= ~(self.WS_CAPTION | self.WS_THICKFRAME)
        self.SetWindowLongPtrW(hwnd, self.GWL_STYLE, style)


# Test
if __name__ == '__main__:
    import tkinter as tk
    root = tk.Tk()
    RemoveTopBar(root)
    root.mainloop()
