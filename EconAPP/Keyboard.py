import pygame

class Keyboard:
    def __init__(self):
        self.flush()

    def ret(self):
        return self._str

    def ev(self,event):
        ct=pygame.time.get_ticks()

        if event.type == pygame.KEYDOWN:#checks keys
            if(event.key<100000):
                if(event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
                    self._str=self._str[:-1]
                    self._held=True
                    self._held_time=pygame.time.get_ticks()
                else:
                    if(pygame.K_z>=event.key and event.key>=pygame.K_a and (event.mod==pygame.KMOD_LSHIFT or event.mod==pygame.KMOD_RSHIFT or event.mod==pygame.KMOD_CAPS)):
                        self._str+=chr(event.key-32)
                    else:
                        self._str+=chr(event.key)
                        
        if event.type == pygame.KEYUP:#stops the deleting 
            if(event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
                self._held=False
                
    def update(self):
        ct=pygame.time.get_ticks()
        
        if(ct-self._held_time>500 and self._held):#does the deleting
            if(ct-self._interval>20):
                self._str=self._str[:-1]
                self._interval=ct

    def flush(self):
        self._str=""
        self._prev=0
        self._held_time=0
        self._held=False
        self._interval=0
        
    def set(self,string):
        self._str=string

