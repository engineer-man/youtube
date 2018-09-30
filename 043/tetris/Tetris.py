import pygame
from pygame.locals import *
from random import choice
from copy import deepcopy

NAME_OF_THE_GAME = "Tetris"
BLOCK_SIZE = 30

def coord_in_px(coord):
    return (coord[0] * BLOCK_SIZE,
            coord[1] * BLOCK_SIZE)

DRAW_SPOTLIGHT = True # the spotlight is a guide the width of the player that extends to where it would fall.
STAGE_WIDTH = 9 # stage is where the game takes place.
STAGE_HEIGHT = 17
STAGE_MARGIN = (1,1)
BOARD_WIDTH= 5 # the board shows the next piece, the score and lines
BOARD_MARGIN = (STAGE_WIDTH+3, STAGE_MARGIN[1])
BOARD_CENTER_X = BOARD_MARGIN[0] + BOARD_WIDTH/2

PIECE_STAGE_STARTING_POSITION = (4,0)
NEXT_PIECE_POSITION = (BOARD_CENTER_X - 2, 13)
SCREEN_SIZE = (BOARD_MARGIN[0] + BOARD_WIDTH + 1   , STAGE_HEIGHT + 3)
STAGE_TOP_LEFT = STAGE_MARGIN
STAGE_BOTTOM_RIGHT = (STAGE_MARGIN[0] + STAGE_WIDTH, STAGE_MARGIN[1] + STAGE_HEIGHT)

BORDER_COLOR = (160,160,160)
BORDER_WIDTH = 1 #the borders surrounding areas

SPOTLIGHT_COLOR = (15,15,15)
TITLE_COLOR = (0, 64, 128)
TEXT_COLOR = (255,255,255)
GAME_OVER_TEXT_COLOR = (255,0,0)
PAUSE_TEXT_COLOR = (255,255,255)

FPS = 60
LOWER_PIECE_EVENT_ID = USEREVENT+1


class Piece:
    """It's a piece of the game.
    contains a representation of it's shape and rotation.
    contains coordinates of it's components in the stage.
    contains capacity to move and rotate."""
    pieces = {
        "L":{"color" : (128, 94, 0),
             "offset": -1, # used to center the piece when it appears on screen
             "shape" : [[0,1,0],
                        [0,1,0],
                        [0,1,1]]},

        "J":{"color":  (0, 0, 128),
             "shape": [[0,1,0],
                       [0,1,0],
                       [1,1,0]]},
        
        "I":{"color" : (0, 128, 128),
             "offset": -1,
             "shape" : [[0,0,1,0,0],
                        [0,0,1,0,0],
                        [0,0,1,0,0],
                        [0,0,1,0,0]]},

        "S":{"color": (0, 128, 0),
             "shape": [[1,0,0],
                       [1,1,0],
                       [0,1,0]]},

        "Z":{"color": (128, 0, 0),
             "shape": [[0,1,0],
                       [1,1,0],
                       [1,0,0]]},

        "T": {"color": (128, 0, 128),
              "shape": [[0,0,0],
                        [1,1,1],
                        [0,1,0]]},

        "B": {"color": (128, 128, 0),
              "shape": [[1,1],
                        [1,1]]}}

    def __init__(self, piece_name = None, position = None):
        self.position = position or list(NEXT_PIECE_POSITION)
        self.name = piece_name or choice( list(self.pieces.keys()) )
        self.shape = deepcopy(self.pieces[self.name]["shape"])
        self.color = self.pieces[self.name]["color"]
        self.blocks = None
        self.update_blocks()
        self.offset_piece()

    def set_position(self, position):
        self.position = position
        self.update_blocks()
        self.offset_piece()

    def offset_piece(self):
        if "offset" in self.pieces[self.name].keys():
            self.move([self.pieces[self.name]["offset"], 0])

    def update_blocks(self):
        r = []
        for row_i, row in enumerate(self.shape):
            for col_i, block in enumerate(row):
                if block:
                    x = col_i + self.position[0] + STAGE_MARGIN[0]
                    y = row_i + self.position[1] + STAGE_MARGIN[1]
                    r.append([x, y])
        self.blocks = r
        if DRAW_SPOTLIGHT:
            self.blocks.sort()

    def rotate_ccw(self, update_blocks = True):
        r = []
        while self.shape:
            if self.shape[0]:
                r.append([])
                for row_i in range(len(self.shape)):
                    r[-1].append(self.shape[row_i][-1])
                    del self.shape[row_i][-1]
            else: self.shape = []
        self.shape = r
        if update_blocks:
            self.update_blocks()

    def rotate_cw(self):
        self.rotate_ccw(False)
        self.rotate_ccw(False)
        self.rotate_ccw()

    def move(self, coord):
        self.position[0] += coord[0]
        self.position[1] += coord[1]
        for block in self.blocks:
            block[0] += coord[0]
            block[1] += coord[1]

    def __iter__(self):
        for block in self.blocks:
            yield block

    def __getitem__(self, key):
        return self.blocks[key]

    def __delitem__(self, item):
        del self.blocks[item]

    def __len__(self):
        return len(self.blocks)



class GameCore:
    """Manages the interaction between the player and movement, margins, lower pieces, states, score, next piece and level."""
    def __init__(self, piece_name = None):
        self.playing = True
        self.paused = False
        self.game_over = False
        self.player = Piece(piece_name, list(PIECE_STAGE_STARTING_POSITION))
        self.player.offset_piece()
        self.next_piece = Piece()
        self.score = Score()
        self.bottom_pieces = BottomPieces(self)

    def set_paused(self, pause = None):
        self.paused = pause if pause != None else not self.paused
        self.playing = not self.paused and not self.game_over

    def player_oversteps_bottom_pieces(self):
        for coord in self.player.blocks:
            if coord in self.bottom_pieces:
                return True
        return False

    def player_oversteps_border(self):
        for coord in self.player.blocks:
            if not (STAGE_MARGIN[0] <= coord[0] <= STAGE_WIDTH+STAGE_MARGIN[0]) or \
               not (coord[1] <= STAGE_HEIGHT+STAGE_MARGIN[1]):
                return True
        return False

    def player_oversteps(self):
        return self.player_oversteps_border() or self.player_oversteps_bottom_pieces()

    def move_player(self, coord):
        self.player.move(coord)
        if self.player_oversteps():
            self.player.move([coord[0]*-1, coord[1]*-1])
            if coord[1]:
                self.change_player()

    def rotate_player(self):
        self.player.rotate_cw()
        if self.player_oversteps():
            self.player.rotate_ccw()

    def change_player(self):
        self.bottom_pieces.append(self.player)
        self.player = self.next_piece
        self.player.set_position(list(PIECE_STAGE_STARTING_POSITION))
        self.next_piece = Piece()
        self.bottom_pieces.check_rows()
        if self.player_oversteps_bottom_pieces():
            self.playing = False
            self.game_over = True

    def bottom_pieces_call(self, number):
        """BottomPieces uses this method when it clears lines"""
        self.score.add_lines(number)

    def move_piece_to_limit(self, coord):
        """It lowers the piece to the bottom in one movement,
        or it moves it to the right or left until a limit is met"""
        def has_advanced(previous_pos, current_pos):
            if   coord[0] > 0:
                return previous_pos[0] < current_pos[0]
            elif coord[0] < 0:
                return previous_pos[0] > current_pos[0]
            elif coord[1] > 0:
                return previous_pos[1] < current_pos[1]
            elif coord[1] < 0:
                return previous_pos[1] > current_pos[1]
            elif previous_pos == current_pos:
                return False

        keep_moving = True
        while keep_moving:
            old_position = self.player.position[:]
            self.move_player(coord)
            if not has_advanced(old_position, self.player.position):
                keep_moving = False



class BottomPieces(list):
    def __init__(self, game_core):
        super(BottomPieces, self).__init__()
        self.game_core = game_core

    def __contains__(self, element):
        if super(BottomPieces, self).__contains__(element):
            return True
        else:
            for piece in self:
                if element in piece:
                    return True
        return False

    def check_rows(self):
        blocks_deleated = 0
        acc = {}
        for piece in self:
            for block in piece:
                if block[1] not in acc.keys():
                    acc[block[1]] = []
                acc[block[1]].append(block[0])

        for key, value in sorted(acc.items()):
            if len(value) == STAGE_WIDTH+1:
                blocks_deleated += self.delete_row(key)

        lines_cleared = blocks_deleated // (STAGE_WIDTH + 1)
        if lines_cleared:
            self.game_core.bottom_pieces_call(lines_cleared)

    def delete_row(self, row):
        blocks_deleated = 0
        for piece_index in range(len(self)-1, -1, -1):
            for box_index in range(len(self[piece_index])-1,-1, -1):
                if self[piece_index][box_index][1] == row:
                    del self[piece_index][box_index]
                    blocks_deleated += 1
                    if not len(self[piece_index]):
                        del self[piece_index]
                elif self[piece_index][box_index][1] < row:
                    self[piece_index][box_index][1] += 1
        return blocks_deleated



class Score:
    def __init__(self):
        self.lines = 0
        self.level = 0
        self.score = 0

    def add_lines(self, lines):
        self.lines += lines
        self.level  = self.lines//10
        if   lines == 1: self.score += 40   * (self.level + 1)
        elif lines == 2: self.score += 100  * (self.level + 1)
        elif lines == 3: self.score += 300  * (self.level + 1)
        elif lines == 4: self.score += 1200 * (self.level + 1)



class Clock:
    def __init__(self, score):
        self.score = score
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.lower_piece_data = {n:int(48 - 2.4 * n) for n in range(21)}
        self.time_accumulated_to_lower_piece = 0

    lower_piece_every = property(lambda self: self.lower_piece_data[self.score.level] or 2)

    def tick(self):
        elapsed_time = self.clock.tick(self.fps)
        self.process_lower_piece(elapsed_time)

    def process_lower_piece(self, elapsed_time):
        self.time_accumulated_to_lower_piece += elapsed_time
        if self.time_accumulated_to_lower_piece >= self.lower_piece_every * 1000//FPS:
            self.time_accumulated_to_lower_piece = 0
            event_lower_piece = pygame.event.Event(LOWER_PIECE_EVENT_ID)
            pygame.event.post(event_lower_piece)



class Game:
    "Draws stuff and handles events"
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(coord_in_px(SCREEN_SIZE))
        pygame.display.set_caption(NAME_OF_THE_GAME)
        pygame.key.set_repeat(1,160)
        self.core = GameCore()
        self.running = True # is the application running
        self.clock = Clock(self.core.score)
        self.font = pygame.font.SysFont("Arial", 22)

    def run(self):
        while self.running:
            self.clock.tick()
            self.handle_events()
            self.draw_game()

    def tick(self):
        self.core.move_player( (0,1) )

    def draw_game(self):
        self.screen.fill((0, 0, 0))
        if self.core.game_over:
            self.draw_game_over()
        if self.core.paused:
            self.draw_pause()
        if DRAW_SPOTLIGHT:
            self.draw_spotlight()
        self.draw_pieces()
        self.draw_number_of_lines()
        self.draw_score()
        self.draw_level_number()
        self.draw_next_piece()
        self.draw_borders()
        pygame.display.flip()

    def render_text(self, text, position, color):
        txt_pos = list(coord_in_px(position))
        text = self.font.render(text, True, color)
        txt_pos[0] -= text.get_width()//2
        self.screen.blit(text, txt_pos)    

    def draw_number_of_lines(self):
        self.render_text("LINES", (BOARD_CENTER_X, 1.5), TITLE_COLOR)
        self.render_text(str(self.core.score.lines), (BOARD_CENTER_X, 2.5), TEXT_COLOR)

    def draw_level_number(self):
        self.render_text("LEVEL", (BOARD_CENTER_X, 4.5), TITLE_COLOR)
        self.render_text(str(self.core.score.level), (BOARD_CENTER_X, 5.5), TEXT_COLOR)

    def draw_score(self):
        self.render_text("SCORE", (BOARD_CENTER_X, 7.5), TITLE_COLOR)
        self.render_text(str(self.core.score.score), (BOARD_CENTER_X, 8.5), TEXT_COLOR)
 
    def draw_game_over(self):
        self.render_text("GAME OVER", (BOARD_CENTER_X, 10.5), GAME_OVER_TEXT_COLOR)

    def draw_pause(self):
        self.render_text("PAUSE", (BOARD_CENTER_X, 10.5), PAUSE_TEXT_COLOR)

    
    def draw_next_piece(self):
        self.render_text("NEXT PIECE", (BOARD_CENTER_X, 12.5), TITLE_COLOR)
        self.draw_piece(self.core.next_piece)

    def draw_piece(self, piece):
        size_rect = (BLOCK_SIZE, BLOCK_SIZE)
        for block_pos in piece:
            pixel_pos = coord_in_px(block_pos)
            pygame.draw.rect(self.screen, piece.color, Rect(pixel_pos, size_rect))

    def draw_spotlight(self):
        top_left_x = coord_in_px(self.core.player.blocks[0])[0]
        top_left_y = coord_in_px(STAGE_TOP_LEFT)[1]
        top_left = (top_left_x, top_left_y)
        x_for_bottom_x = self.core.player.blocks[-1][0] - self.core.player.blocks[0][0]
        bottom_right_x = coord_in_px((x_for_bottom_x + STAGE_MARGIN[0], 1))[0]
        bottom_right_y = coord_in_px(STAGE_BOTTOM_RIGHT)[1]
        bottom_right = (bottom_right_x, bottom_right_y)
        pygame.draw.rect(self.screen, SPOTLIGHT_COLOR, Rect(top_left, bottom_right))

    def draw_pieces(self):
        self.draw_piece(self.core.player)
        for piece in self.core.bottom_pieces:
            self.draw_piece(piece)

    def draw_borders(self):
        stage_rect = Rect(coord_in_px(STAGE_TOP_LEFT), coord_in_px(STAGE_BOTTOM_RIGHT))
        pygame.draw.rect(self.screen, BORDER_COLOR, stage_rect, BORDER_WIDTH)
        right_area_top_left = BOARD_MARGIN
        right_area_bottom_right = (BOARD_WIDTH, STAGE_HEIGHT+1)
        right_area_rect = Rect(coord_in_px(right_area_top_left), coord_in_px(right_area_bottom_right))
        pygame.draw.rect(self.screen, BORDER_COLOR, right_area_rect, BORDER_WIDTH)

    def handle_events(self):
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == KEYDOWN:
                if event.key in (K_PAUSE, K_RETURN, K_p):
                    if not self.core.game_over:
                        self.core.set_paused()
                    else:
                        self.__init__()
                
            if self.core.playing:
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.core.rotate_player()
                    elif event.key == K_DOWN:
                        self.core.move_player( (0,1) )
                    elif event.key == K_RIGHT:
                        self.core.move_player( (1,0) )
                    elif event.key == K_LEFT:
                        self.core.move_player( (-1,0) )
                    elif event.key == K_SPACE:
                        if keys_pressed[K_RIGHT]:
                            self.core.move_piece_to_limit((1,0))
                        elif keys_pressed[K_LEFT]:
                            self.core.move_piece_to_limit((-1,0))
                        else:
                            self.core.move_piece_to_limit((0,1))
                elif event.type == LOWER_PIECE_EVENT_ID:
                    self.core.move_player( (0,1) )



if __name__ == '__main__':
    Game().run()
