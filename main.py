def on_on_overlap(sprite, otherSprite):
    mySprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_on_destroyed(sprite):
    global myEnemy, projectile
    music.ba_ding.play()
    info.change_score_by(1)
    myEnemy = sprites.create(img("""
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . d d d d d . . . . . . . . . . . 
                    . . . . . . . . . . . . . . d d f f d f f d d . . . . . . . . . 
                    . . . . . . . . . . . . . d d d f f d f f d d . . . . . . . . . 
                    . . . . . . . . e e e e e e e e e d d d d e e e e e . . . . . . 
                    . . . . . . . . . e e e e e e e e e e e e e e e e . . . . . . . 
                    . . . . . . . . . e e e e e e e e e e e e e e e e . . . . . . . 
                    . . . . . . . . e e e e . . 5 5 2 2 2 5 5 5 . . . e . . . . . . 
                    . . . . . . . . . . . . 5 5 5 5 2 2 2 5 5 5 5 . . . . . . . . . 
                    . . . . . . . . . . . 5 5 5 5 5 2 2 2 5 5 5 5 2 2 . . . . . . . 
                    . . . . . . . . 2 2 2 5 5 5 5 5 2 2 2 5 5 5 2 2 2 2 2 . . . . . 
                    . . . . . . . 2 2 2 2 5 5 5 5 5 2 2 2 5 5 5 2 2 2 2 2 2 . . . . 
                    . . . . . . 2 2 2 2 2 2 5 5 5 5 2 2 2 5 5 2 2 2 2 2 2 2 2 . . . 
                    . . . . . . 2 2 2 2 2 2 2 2 5 5 2 2 2 5 5 2 2 2 2 2 2 2 2 2 . . 
                    . . . . . 2 2 2 2 2 2 2 2 2 2 5 2 2 2 5 2 2 2 2 2 2 2 2 2 2 2 . 
                    . . . . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 
                    . . . . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    . . . 2 2 2 2 . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 2 2 2 2 2 
                    . . . 2 2 2 2 . f f f f f f f f f f f f f f f f f f . . 2 2 1 1 
                    . . . 2 2 2 . . . f f f f f f f f f f f f f f f f . . . 1 1 1 1 
                    . . 1 1 1 1 1 . . . . f f f f f f f f f f f f f . . . . 1 1 1 1 
                    . 1 1 1 1 1 1 . . . . . f f f f f f f f f f . . . . . . 1 1 1 1 
                    . 1 1 1 1 1 1 . . . . . . f f f f f f f . . . . . . . . . . . . 
                    . . 1 1 1 1 1 . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
                    . . . . . . . . . f f f f f f . . . . f f f f f f . . . . . . .
        """),
        SpriteKind.enemy)
    myEnemy.set_position(randint(0, 100), randint(0, 100))
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . f f . . . 
                    . . . f f . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . .
        """),
        myEnemy,
        50,
        50)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_on_destroyed2(sprite):
    global mySprite
    mySprite = sprites.create(img("""
            . . . . . . 8 8 . . . . 8 . . . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 . . . 
                    . 8 8 8 8 1 1 1 8 8 8 8 8 . . . 
                    8 8 8 8 8 1 1 1 1 8 1 1 8 . . . 
                    8 8 8 8 8 1 1 1 f 1 1 f 8 . . . 
                    . . 8 8 8 1 1 1 f 1 1 f 8 . . . 
                    . 8 8 8 8 d d d d d d f f f . . 
                    8 8 8 8 8 d d d d d d d 8 . . . 
                    8 8 8 8 8 8 8 8 8 8 8 8 . . . . 
                    8 8 8 . d 8 8 d d 8 8 d . . . . 
                    . . . d . 8 d d d d 8 . d . . . 
                    . . . d . 8 8 8 d d 8 . d . . . 
                    . . 1 1 . . 8 . 8 8 . . 1 1 . . 
                    . . 1 1 . . 8 . . 8 . . 1 1 . . 
                    . . . . . . 8 . . 8 . . . . . . 
                    . . . . . . 2 2 2 2 2 2 . . . .
        """),
        SpriteKind.player)
    controller.move_sprite(mySprite)
sprites.on_destroyed(SpriteKind.player, on_on_destroyed2)

def on_on_overlap2(sprite, otherSprite):
    myEnemy.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
myEnemy: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . 8 8 . . . . 8 . . . 
            . . 8 8 8 8 8 8 8 8 8 8 8 . . . 
            . 8 8 8 8 1 1 1 8 8 8 8 8 . . . 
            8 8 8 8 8 1 1 1 1 8 1 1 8 . . . 
            8 8 8 8 8 1 1 1 f 1 1 f 8 . . . 
            . . 8 8 8 1 1 1 f 1 1 f 8 . . . 
            . 8 8 8 8 d d d d d d f f f . . 
            8 8 8 8 8 d d d d d d d 8 . . . 
            8 8 8 8 8 8 8 8 8 8 8 8 . . . . 
            8 8 8 . d 8 8 d d 8 8 d . . . . 
            . . . d . 8 d d d d 8 . d . . . 
            . . . d . 8 8 8 d d 8 . d . . . 
            . . 1 1 . . 8 . 8 8 . . 1 1 . . 
            . . 1 1 . . 8 . . 8 . . 1 1 . . 
            . . . . . . 8 . . 8 . . . . . . 
            . . . . . . 2 2 2 2 2 2 . . . .
    """),
    SpriteKind.player)
myEnemy = sprites.create(img("""
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . d d d d d . . . . . . . . . . . 
            . . . . . . . . . . . . . . d d f f d f f d d . . . . . . . . . 
            . . . . . . . . . . . . . d d d f f d f f d d . . . . . . . . . 
            . . . . . . . . e e e e e e e e e d d d d e e e e e . . . . . . 
            . . . . . . . . . e e e e e e e e e e e e e e e e . . . . . . . 
            . . . . . . . . . e e e e e e e e e e e e e e e e . . . . . . . 
            . . . . . . . . e e e e . . 5 5 2 2 2 5 5 5 . . . e . . . . . . 
            . . . . . . . . . . . . 5 5 5 5 2 2 2 5 5 5 5 . . . . . . . . . 
            . . . . . . . . . . . 5 5 5 5 5 2 2 2 5 5 5 5 2 2 . . . . . . . 
            . . . . . . . . 2 2 2 5 5 5 5 5 2 2 2 5 5 5 2 2 2 2 2 . . . . . 
            . . . . . . . 2 2 2 2 5 5 5 5 5 2 2 2 5 5 5 2 2 2 2 2 2 . . . . 
            . . . . . . 2 2 2 2 2 2 5 5 5 5 2 2 2 5 5 2 2 2 2 2 2 2 2 . . . 
            . . . . . . 2 2 2 2 2 2 2 2 5 5 2 2 2 5 5 2 2 2 2 2 2 2 2 2 . . 
            . . . . . 2 2 2 2 2 2 2 2 2 2 5 2 2 2 5 2 2 2 2 2 2 2 2 2 2 2 . 
            . . . . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 
            . . . . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            . . . 2 2 2 2 . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 . 2 2 2 2 2 
            . . . 2 2 2 2 . f f f f f f f f f f f f f f f f f f . . 2 2 1 1 
            . . . 2 2 2 . . . f f f f f f f f f f f f f f f f . . . 1 1 1 1 
            . . 1 1 1 1 1 . . . . f f f f f f f f f f f f f . . . . 1 1 1 1 
            . 1 1 1 1 1 1 . . . . . f f f f f f f f f f . . . . . . 1 1 1 1 
            . 1 1 1 1 1 1 . . . . . . f f f f f f f . . . . . . . . . . . . 
            . . 1 1 1 1 1 . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . . . . . . f . . . . f . . . . . . . . . . . . 
            . . . . . . . . . f f f f f f . . . . f f f f f f . . . . . . .
    """),
    SpriteKind.enemy)
controller.move_sprite(mySprite)
scene.set_background_color(9)
mySprite.set_velocity(100, 100)
mySprite.set_position(76, 59)
myEnemy.set_position(randint(0, 100), randint(0, 100))
projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . 
            . . . . . . . . 
            . . . . . . . . 
            . . . f f . . . 
            . . . f f . . . 
            . . . . . . . . 
            . . . . . . . . 
            . . . . . . . .
    """),
    myEnemy,
    50,
    50)
info.set_life(3)
info.start_countdown(10)