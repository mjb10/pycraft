from pyscript import when

AppState = 0


@when("pointerover", selector=".parentDisplay")
def trigger():
    global AppState

    if AppState == 0:
        print("Hello world!")

    AppState = 1
