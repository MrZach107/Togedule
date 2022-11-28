#pip install eel
import eel

eel.init("網站") #資料夾位址

@eel.expose
def App(): # App main Function
    print("Application Running")

App()

eel.start("index.html",size = (960,540)) #Run App window