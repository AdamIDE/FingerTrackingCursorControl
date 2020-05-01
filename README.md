# FingerTrackingCursorControl (FTCC)

Cursor control based on VGG-16 CNN from [MahmudulAlam](https://github.com/MahmudulAlam/Unified-Gesture-and-Fingertip-Detection)

Repo for ECE471 project (Private; not for distribution).


### Installation
We recomend running our program wtih `pipenv` but `pip3` can work as well.

#### Pipenv
Ensure you have `pipenv` installed globally,
```sh
$ pip3 install pipenv
```
 and then,

```sh
$ cd /path/to/FingerTrackingCursorControl/src
$ pipenv install -r requirements.txt
$ pipenv run python real-time.py
```

#### Pip3
```sh
$ cd /path/to/FingerTrackingCursorControl/src
$ pip3 install requirements.txt
$ python real-time.py
```

## Cursor Control Examples
The following section shows the various different cursor controls that can be triggered uniquely using the gestures decribed in the table and imagery below.

| Cursor Action |     Thumb     |      Index     |     Middle     |      Ring       | Pinky |
| ------------- |:-------------:| :-------------:| :-------------:| :-------------: | -----:|
|      Move     |     -     |     ✔️      |     -     |      -       | - |
|  Left Click   |     ✔️     |      -     |     -     |      -       | ✔️ |
|  Right Click  |     -     |      ✔️     |     -     |      -       | ✔️ |
|   Scroll Up   |     -     |      ✔️     |     ✔️     |      -       | - |
|  Scroll Down  |     -     |      ✔️     |     ✔️     |      ✔️       | ✔️ |
|      Exit     |     ✔️     |      ✔️     |     ✔️     |      ✔️       | ✔️ |

### Image Gestures

#### Move
##### Moves the cursor to a mapped point on the user's monitor (Dynamic mapping)
<img src="./images/move.PNG" width="50%" style="padding: -50px" />

#### Left Click
##### Imitates left click trigger at cursor location
<img src="./images/Click.PNG" width="50%" />

#### Right Click
##### Imitates right click trigger at cursor location
<img src="./images/rightclick.PNG" width="50%" />

#### Scroll Up
##### Imitates scrolling up at cursor location
<img src="./images/scrollup.PNG" width="50%" />

#### Scroll Down
##### Imitates scrolling down at cursor location
<img src="./images/scrolldown.PNG" width="50%" />

#### Exit
<img src="./images/exit.PNG" width="50%" />


### Dataset
[HCII - SCUT-Ego-Gesture](http://www.hcii-lab.net/data/SCUTEgoGesture/index.htm)


### License

MIT
