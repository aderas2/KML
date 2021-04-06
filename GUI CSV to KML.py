import simplekml
import pandas as pd
import tkinter
from tkinter.filedialog import askopenfilename


def browse():
  global infile
  infile = askopenfilename()
  


def kmlFunction(outfile='points.kml'):
  df = pd.read_csv(infile)
  kml = simplekml.Kml()
  for lon,lat in zip(df['Longitude'],df['Latitude']):
    kml.newpoint(coords = [(lon,lat)])
  kml.save(outfile)


root = tkinter.Tk()
root.title('KML Generator')
label = tkinter.Label(root,text='This program generates a KML file')
label.pack()
browseButton = tkinter.Button(root,text='Browse',command=browse)
browseButton.pack()
kmlButton = tkinter.Button(root,text='Generate KML', command= kmlFunction)
kmlButton.pack()
root.mainloop()