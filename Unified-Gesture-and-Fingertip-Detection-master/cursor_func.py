import pyautogui


def cursorControl(prob, pos):
    
    # prob = array of which finger is visible to the camera
    # pos = array of the x,y co-ordinates of each finger 
    if prob[1] == 1 and prob[2] == 1 and prob[3] == 1:

        pyautogui.click(button='right')             # Right click (requires middle 3 fingers to trigger)

    elif prob[1] == 1 and prob[0] == 1:

        pyautogui.click(button='left')              # Left click (requires middle 3 fingers to trigger)

    elif prob[1] == 1:

        pyautogui.moveTo(3*pos[0],3*pos[1])