# Widgets Recommendations

## Button
```
activebackground = darker_than_bg
activeforeground = txt_color
relief = sunken
```
## Entry
```
insertbackground = txt_color
relief = flat
(and a line below entry widget to make it visible)
```
## Canvas
```
highlightbackground=bd_color
highlightthickness=bd_thickness
```
## Frame
```
highlightbackground=bd_color
highlightthickness=bd_thickness
```
## ProgressBar
```
from tkinter import ttk
s = ttk.Style()
s.theme_use('clam')
s.configure("grey.(Orientation).TProgressbar", background=fg, bordercolor=fg,
            troughcolor=bg, lightcolor=fg,darkcolor=fg)
progressbar = ttk.Progressbar(kw, style="grey.(Orientation).TProgressbar")
```
