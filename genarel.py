import pygame


win =pygame.display.set_mode((500,500))
pygame.display.set_caption("Frist Game")
x=(40)
y=(40)
hight=40
wight=60
vel=5


run=True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            x-=vel
    if keys[pygame.K_RIGHT]:
            x+=vel
    if keys[pygame.K_UP]:
            y-=vel
    if keys[pygame.K_DOWN]:
            y+=vel

            

    win.fill((0,0,0)) 
    pygame.draw.rect(win,(200,0,0),(x,y,wight,hight))
    pygame.display.update()

pygame.quit()
    


