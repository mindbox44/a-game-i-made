sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    mySprite.destroy()
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite) {
    music.baDing.play()
    info.changeScoreBy(1)
    myEnemy = sprites.create(img`
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
        `, SpriteKind.Enemy)
    myEnemy.setPosition(randint(0, 100), randint(0, 100))
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . f f . . . 
        . . . f f . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        `, myEnemy, 50, 50)
})
sprites.onDestroyed(SpriteKind.Player, function (sprite) {
    mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
    controller.moveSprite(mySprite)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    myEnemy.destroy()
})
let projectile: Sprite = null
let myEnemy: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
myEnemy = sprites.create(img`
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
    `, SpriteKind.Enemy)
controller.moveSprite(mySprite)
scene.setBackgroundColor(9)
mySprite.setVelocity(100, 100)
mySprite.setPosition(76, 59)
myEnemy.setPosition(randint(0, 100), randint(0, 100))
projectile = sprites.createProjectileFromSprite(img`
    . . . . . . . . 
    . . . . . . . . 
    . . . . . . . . 
    . . . f f . . . 
    . . . f f . . . 
    . . . . . . . . 
    . . . . . . . . 
    . . . . . . . . 
    `, myEnemy, 50, 50)
info.setLife(3)
info.startCountdown(10)
