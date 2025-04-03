import pygame
import random


pygame.init()
pygame.mixer.init()  

correct_sound = pygame.mixer.Sound("correct.wav")
incorrect_sound = pygame.mixer.Sound("incorrect.wav")
timer_warning_sound = pygame.mixer.Sound("timer_warning.wav")


WIDTH, HEIGHT = 1200, 650
FONT_SIZE = 48
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN=(0,255,0)
BLUE=(0,0,255)
PINK=(255, 192, 203)
YELLOW=(255,255,0)
ASH=(178,190,181)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Scramble Game")
icon=pygame.image.load("jumbled-word.jpg")
pygame.display.set_icon(icon)

background=pygame.image.load("Background.png")


font = pygame.font.Font(None, FONT_SIZE)


words = ["apple", "banana", "car", "dog", "elephant", "flower", 
         "grape", "house", "island", "jacket", "kite", "lamp", 
         "mountain", "notebook", "orange", "pen", "queen", "robot", 
         "sun", "tree", "umbrella", "vase", "window", "xylophone", 
         "yellow", "zebra", "airplane", "book", "cat", "desk", "egg", 
         "fish", "guitar", "hat", "ice", "juice", "king", "lemon", "mango", 
         "necklace", "octopus", "pencil", "quilt", "rose", "snow", "table", 
         "unicorn", "volcano", "water", "yacht", "zoo", "ant", "butterfly", 
         "cloud", "drum", "elephant", "frog", "giraffe", "helicopter", "insect", 
         "jaguar", "koala", "lizard", "mouse", "nut", "octagon", "parrot", 
         "quince", "rabbit", "snake", "tiger", "universe", "vulture", "whale", 
         "xenon", "yak", "zombie", "anchor", "ball", "camera", "doghouse", "ear", 
         "fence", "glove", "hatchet", "iceberg", "jewel", "kettle", "ladder", 
         "moose", "noodle", "oak", "plank", "quiver", "rowboat", "scissors", 
         "telescope", "unicorn", "vest", "wallet", "x-ray", "yarn", "zipper", 
         "air", "bicycle", "cart", "doll", "eggplant", "flood", "guitar", 
         "hole", "inbox", "jacket", "knot", "log", "mushroom", "neck", 
         "orange", "purse", "quiz", "rope", "swing", "tray", "unicorn", 
         "vortex", "whistle", "xmas", "yellowstone", "zippers", "applause", 
         "beach", "cherry", "deer", "elephant", "fall", "game", "harp", 
         "inbox", "joke", "key", "lemon", "money", "noose", "peach", "quick", 
         "rain", "shade", "tree", "uncle", "van", "whip", "xylophone", "yarn", 
         "zebra", "air", "bat", "cabbage", "doll", "egg", "fly", "goose", "helmet", 
         "ice", "jackal", "kettle", "loud", "moth", "nut", "octave", "puzzle", 
         "quit", "rope", "spade", "tick", "urn", "volley", "wand", "yx", 
         "zucchini", "ace", "boat", "clover", "door", "ear", "frog", "gear", 
         "hound", "insect", "jungle", "kettle", "leaf", "man", "night", "oak", 
         "plum", "quilt", "robin", "sock", "tree", "umbrella", "violet", 
         "wave", "xenon", "yawn", "zebra", "animal", "bird", "cake", "diver", 
         "emergency", "fur", "grape", "hat", "icon", "jelly", "keychain", 
         "lemonade", "music", "noon", "oval", "pear", "quilt", "rainbow", 
         "ship", "tiger", "umrah", "vase", "whale", "xray", "yellow", "zero", 
         "and", "beach", "card", "diving", "energy", "flame", "grip", "hop", 
         "iron", "job", "knight", "lamp", "meat", "neck", "olive", "plane", 
         "question", "rest", "scooter", "turtle", "umbrella", "vacuum", "world", 
         "xenon", "yoga", "zone", "applause", "bamboo", "clamp", "doorbell", "ear", 
         "football", "guitar", "hamster", "idea", "joint", "lemon", "marble", "nuts", 
         "oven", "pumpkin", "quack", "race", "steak", "tree", "ugly", "vintage", 
         "wind", "yogurt", "zigzag", "backpack", "carpet", "duck", "eagle", "fence",
           "guitar", "hat", "idea", "jacket", "knee", "lighthouse", "mosquito", "nose", 
           "potato", "quick", "rat", "sock", "teeth", "umbrella", "vacuum", "whip", 
           "x-ray", "yarn", "zero", "album", "bacon", "candle", "dance", "effort", 
           "gland", "hand", "ironing", "jeans", "lawn", "mean", "nick", "outdoor", 
           "party", "quarter", "rose", "snow", "tile", "ufo", "vast", "windmill", 
           "yawn", "zone", "apple", "branch", "coin", "deep", "elephant", "fungus", 
           "goal", "hammer", "ink", "joint", "kick", "low", "mail", "nail", "over", 
           "pulse", "quilt", "rich", "sand", "tire", "urn", "vase", "wing", "xmas", 
           "year", "zone"]
difficulty_dict = {
    "easy": [word for word in words if len(word) <= 4],
    "medium": [word for word in words if 5 <= len(word) <= 6],
    "hard": [word for word in words if len(word) > 6]
}
score = 0
current_word = ""
scrambled_word = ""
user_input = ""
timer = 30
game_over = False
hint_displayed = False
hint_time = 0
correct_time=0
correct_displayed=False

def scramble_word(word):
    global score
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def reset_game():
    global score,current_word, scrambled_word, user_input, timer, game_over, hint_displayed, hint_time
    if(score<=6):
        current_word = random.choice(difficulty_dict["easy"])
        scrambled_word = scramble_word(current_word)
        while scrambled_word==current_word:
            scrambled_word=scramble_word(current_word)            
    elif(score>6 and score<=12):
        current_word = random.choice(difficulty_dict["medium"])
        scrambled_word = scramble_word(current_word)
        while scrambled_word==current_word:
            scrambled_word=scramble_word(current_word)
    else:
        current_word = random.choice(difficulty_dict["hard"])
        scrambled_word = scramble_word(current_word)
        while scrambled_word==current_word:
            scrambled_word=scramble_word(current_word)
    user_input = ""
    timer = 30
    game_over = False
    hint_displayed = False
    hint_time = 0
    correct_time=0



reset_game()


running = True
while running:
    screen.blit(background,(0,0))

   
    if not game_over:
        timer -= 1 / 60  
        if timer <= 0:
            game_over = True
            timer = 0
        elif timer <= 10 and not game_over:  
            timer_warning_sound.play()

    
    scrambled_text = font.render(f"Scrambled Word: {scrambled_word}", True, PINK)
    screen.blit(scrambled_text, (400,200))

    
    input_text = font.render(f"Your Guess: {user_input}", True, YELLOW)
    screen.blit(input_text, (400,280))
    

    
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (350, 120))

    
    if(timer>10):
        timer_text = font.render(f"Time Left: {int(timer)}", True, WHITE)
    else:
        timer_text = font.render(f"Time Left: {int(timer)}", True, RED)
    screen.blit(timer_text, (700,120))

    
    if game_over:
        game_over_text = font.render("GAME OVER!", True, RED)
        screen.blit(game_over_text, (400,370))
        correct_answer=font.render(f"CORRECT ANSWER IS : {current_word}", True, ASH)
        screen.blit(correct_answer,(400,410))
        restart_text = font.render("Press R to Play Again", True, WHITE)
        screen.blit(restart_text, (400,450))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    timer_warning_sound.stop()
                    score=0
            elif event.type == pygame.QUIT:
                running = False
        
    else:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.lower() == current_word.lower():
                        if(timer>=22):
                            score += 2
                        else:
                            score += 1
                        correct_time=60
                        correct_displayed=True
                        correct_sound.play()  
                        reset_game()
                    else:
                        incorrect_sound.play()  
                        hint_displayed = True
                        hint_time = 120  
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                
                    
                else:
                    user_input += event.unicode

   
    if hint_displayed:
        hint_text = font.render(f"INCORRECT - Hint: First letter is '{current_word[0]}'", True, RED)
        screen.blit(hint_text, (350,400))
        hint_time -= 1
        if hint_time <= 0:
            hint_displayed = False
    elif correct_displayed:
        correct_text=font.render("CORRECT!!!",True,GREEN)
        screen.blit(correct_text,(500,400))
        correct_time-=1
        if(correct_time<=0):
            correct_displayed=False

    pygame.display.flip()
    pygame.time.Clock().tick(60)  

pygame.quit()