init:
    image start_bg = Image("/images/back.avif")

label start:

    $ e = character("Eli")

    scene start_bg
    e "hello world"
    "hello WORLD"
    e "goodbye world"
