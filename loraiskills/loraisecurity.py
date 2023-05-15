import pyautogui , mouse , requests , cv2 , threading
pyautogui.FAILSAFE=False
def mouse_lock():
    if (mouse.get_position()[0] or mouse.get_position()[1] != 0):
        pyautogui.moveTo(x=0,y=0)
        print('mouse cordinations changed!')
while True:
    if (mouse.get_position()[0] or mouse.get_position()[1] != 0):
        cam = cv2.VideoCapture(0)
        result, image = cam.read()
        cv2.imwrite("hi.jpg", image)
        requests.put("https://ntfy.sh/lorAIwIEXn6Q",data=open(r"D:\Code\codes for me\python-lorai\hi.jpg",'rb'),headers={"Filename":"hi.jpg","Message":"This person try to using computer unauthorize.","Title":"Unauthorized access to the computer has been obtained!"})

    threading.Thread(target=mouse_lock).start()