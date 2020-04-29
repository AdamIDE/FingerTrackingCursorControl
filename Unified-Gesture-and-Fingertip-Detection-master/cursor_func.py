import pyautogui
# pyautogui.PAUSE = 0.5

_width, _height = pyautogui.size()

async def cursorControl(prob, pos):
    
    # prob = array of which finger is visible to the camera
    # pos = array of the x,y co-ordinates of each finger 
    if prob[0] == 1 and prob[1] == 1 and prob[2] == 1 and prob[3] == 1 and prob[4] == 1:
        return True                                             # Exits (requires all 5 fingers)

    elif prob[1] == 1 and prob[2] == 1 and prob[3] == 1 and prob[4] == 1:
        pyautogui.scroll(-30)                                   # Scroll up (requires middle, ring fingers to trigger)

    elif prob[1] == 1 and prob[4] == 1:

        pyautogui.click(button='right')                         # Right click (requires index, middle, ring fingers to trigger)

    elif prob[1] == 1 and prob[2] == 1:

        pyautogui.scroll(30)                                    # Scroll up (requires index, middle fingers to trigger)

    elif prob[0] == 1 and prob[4] == 1:

        pyautogui.click(button='left')                          # Left click (requires thumb and pinky fingers to trigger)

    elif prob[1] == 1:

        pyautogui.moveTo(_width-3.5*pos[0],3.5*pos[1])          # move cursor to positionw (requires index finger to trigger)