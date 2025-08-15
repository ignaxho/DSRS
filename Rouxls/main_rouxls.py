import os
import pygame
import time

class RouxlsAnimation:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Base path para rutas relativas
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        # Configuración inicial
        self.stop = False
        self.game_state = "dialogue"
        self.bg_color_rlx_app = (204, 203, 233)
        self.bg_color_text = (210, 129, 252)
        self.indice = 0
        self.frame_counter = 0
        self.start_ticks = pygame.time.get_ticks()
        self.flag1 = False
        self.flag2 = False
        self.show_textbox = False
        self.text_display_complete = False
        self.current_text = ""
        self.char_index = 0
        self.text_delay = 5
        self.text_timer = 0
        self.current_line = 0
        self.dialogue_lines = []
        self.final_dialogue = ["*MALDITA", "*SEA!"]
        self.final_dialogue_index = 0
        self.final_text_display_complete = False
        self.final_current_text = ""
        self.final_char_index = 0
        self.bs_animation_index = 0
        self.bs_frame_counter = 0
        self.wait_start_time = 0
        self.sad_animation_start_time = 0
        self.ticks_after_first_sound = 0
        self.start_text_time = 0

        # Cargar sonidos con rutas absolutas
        self.teleport_sound = pygame.mixer.Sound(os.path.join(self.base_path, "Sounds", "Rouxls Appear.mp3"))
        pygame.mixer.music.load(os.path.join(self.base_path, "Sounds", "Rouxls Music.mp3"))

        # Configuración de pantalla
        self.alto = pygame.display.Info().current_h
        self.ancho = pygame.display.Info().current_w
        self.screen = pygame.display.set_mode((self.ancho, self.alto), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        # Cargar sprites y fuentes
        self.load_sprites()

        # Cargar diálogo
        self.dialogue_lines = self.load_dialogue("Dialogue.txt")
        self.message = self.dialogue_lines[self.current_line] if self.dialogue_lines else "*THOUS FOOLS!"

    # Función para cargar diálogo con ruta absoluta
    def load_dialogue(self, filename):
        path = os.path.join(self.base_path, filename)
        with open(path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines

    # Función para cargar sprites y fuentes con ruta absoluta
    def load_sprites(self):
        # Animación de aparición
        self.rouxls_appear = []
        for i in range(10):
            s = pygame.image.load(os.path.join(self.base_path, "Sprites", "Rouxls", "Appear", f"Appear{i:03}.png")).convert()
            s.set_colorkey(self.bg_color_rlx_app)
            s = pygame.transform.scale(s, (s.get_width() * 4, s.get_height() * 4))
            self.rouxls_appear.append(s)

        # TextBox
        self.Text_box = pygame.image.load(os.path.join(self.base_path, "Sprites", "GUI", "textbox.png")).convert()
        self.Text_box.set_colorkey(self.bg_color_text)
        self.Text_box = pygame.transform.scale(self.Text_box, (self.Text_box.get_width() * 2, self.Text_box.get_height() * 2))

        # Imagen normal para diálogo inicial
        self.rouxls_talk = pygame.image.load(os.path.join(self.base_path, "Sprites", "Rouxls", "Talk", "Talk001.png")).convert()
        self.rouxls_talk.set_colorkey(self.bg_color_rlx_app)
        self.rouxls_talk = pygame.transform.scale(self.rouxls_talk, (64 * 3, 64 * 3))

        # Imagen enfadada para diálogo final
        self.rouxls_angry = pygame.image.load(os.path.join(self.base_path, "Sprites", "Rouxls", "Talk", "Talk005.png")).convert()
        self.rouxls_angry.set_colorkey(self.bg_color_rlx_app)
        self.rouxls_angry = pygame.transform.scale(self.rouxls_angry, (64 * 3, 64 * 3))

        # Animación blue screen
        self.rouxls_bs_animation = []
        for i in range(1, 3):
            s = pygame.image.load(os.path.join(self.base_path, "Sprites", "Rouxls", "Sad", f"tile00{i}.png")).convert()
            s.set_colorkey(self.bg_color_rlx_app)
            s = pygame.transform.scale(s, (s.get_width() * 4, s.get_height() * 4))
            self.rouxls_bs_animation.append(s)

        # Pantallazo azul
        self.blue_screen = pygame.image.load(os.path.join(self.base_path, "Sprites", "blue_screen.png")).convert()
        self.new_width = int(self.ancho * 1.2)
        self.blue_screen = pygame.transform.scale(self.blue_screen, (self.new_width, self.alto))

        # Fuente
        self.font = pygame.font.Font(os.path.join(self.base_path, "Sprites", "Font", "Font.ttf"), 20)
    
    # Método principal
    def run(self):
        while not self.stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.handle_key_z()

            # Limpiar pantalla
            self.screen.fill((0,0,0))

            # Dibujar blue screen
            self.draw_blue_screen()

            # Dibujar personaje
            self.draw_character()

            # Dibujar textbox y texto
            self.draw_textbox()

            # Animación del personaje
            if self.game_state == "dialogue":
                self.animate_character()

            # Transiciones de estado
            self.handle_state_transitions()

            # Lógica de sonido
            self.handle_sound()

            pygame.display.update()
            self.clock.tick(45)

    # Funciones auxiliares
    def handle_key_z(self):
        if self.game_state == "dialogue":
            if self.text_display_complete:
                self.current_line += 1
                if self.current_line < len(self.dialogue_lines):
                    if self.dialogue_lines[self.current_line].startswith('-'):
                        self.message = self.dialogue_lines[self.current_line][1:]
                    else:
                        self.message = self.dialogue_lines[self.current_line]
                    self.current_text = ""
                    self.char_index = 0
                    self.text_display_complete = False
                else:
                    self.game_state = "pre_blue_wait"
                    self.wait_start_time = pygame.time.get_ticks()
                    pygame.mixer.music.fadeout(500)
            else:
                self.current_text = self.message
                self.char_index = len(self.message)
                self.text_display_complete = True
        elif self.game_state == "final_dialogue":
            if self.final_text_display_complete:
                self.final_dialogue_index += 1
                if self.final_dialogue_index < len(self.final_dialogue):
                    self.message = self.final_dialogue[self.final_dialogue_index]
                    self.final_current_text = ""
                    self.final_char_index = 0
                    self.final_text_display_complete = False
                else:
                    self.stop = True
            else:
                self.final_current_text = self.message
                self.final_char_index = len(self.message)
                self.final_text_display_complete = True

    def draw_blue_screen(self):
        if self.game_state in ["blue_screen", "pre_final_wait", "final_dialogue"]:
            x_offset = (self.ancho - self.new_width) // 2
            self.screen.blit(self.blue_screen, (x_offset, 0))

    def draw_character(self):
        if self.game_state != "pre_blue_wait":
            if self.game_state == "dialogue":
                x = (self.ancho - self.rouxls_appear[self.indice].get_width()) // 2
                y = (self.alto - self.rouxls_appear[self.indice].get_height()) // 3
                self.screen.blit(self.rouxls_appear[self.indice], (x, y))
            elif self.game_state in ["blue_screen", "pre_final_wait", "final_dialogue"]:
                self.bs_frame_counter += 1
                if self.bs_frame_counter >= 5:
                    self.bs_animation_index = (self.bs_animation_index + 1) % len(self.rouxls_bs_animation)
                    self.bs_frame_counter = 0
                x = (self.ancho - self.rouxls_bs_animation[self.bs_animation_index].get_width()) // 2
                y = (self.alto - self.rouxls_bs_animation[self.bs_animation_index].get_height()) // 3
                self.screen.blit(self.rouxls_bs_animation[self.bs_animation_index], (x, y))

    def draw_textbox(self):
        if self.game_state in ["dialogue", "final_dialogue"] and self.show_textbox:
            textbox_x = (self.ancho - self.Text_box.get_width()) // 2
            textbox_y = self.alto - self.Text_box.get_height() - 50
            self.screen.blit(self.Text_box, (textbox_x, textbox_y))

            portrait_x = textbox_x + 40
            portrait_y = textbox_y + (self.Text_box.get_height() - self.rouxls_talk.get_height()) // 2

            if self.game_state == "final_dialogue":
                self.screen.blit(self.rouxls_angry, (portrait_x, portrait_y))
            else:
                self.screen.blit(self.rouxls_talk, (portrait_x, portrait_y))

            # Lógica de texto
            if self.game_state == "dialogue":
                if not self.text_display_complete:
                    self.text_timer += 1
                    if self.text_timer >= self.text_delay and self.char_index < len(self.message):
                        self.current_text += self.message[self.char_index]
                        self.char_index += 1
                        self.text_timer = 0
                    if self.char_index >= len(self.message):
                        self.text_display_complete = True
                text_surface = self.font.render(self.current_text, True, (255, 255, 255))
                text_x = portrait_x + self.rouxls_talk.get_width() + 20
                text_y = textbox_y + (self.Text_box.get_height() - text_surface.get_height()) // 3
                self.screen.blit(text_surface, (text_x, text_y))

            elif self.game_state == "final_dialogue":
                if not self.final_text_display_complete:
                    self.text_timer += 1
                    if self.text_timer >= self.text_delay and self.final_char_index < len(self.message):
                        self.final_current_text += self.message[self.final_char_index]
                        self.final_char_index += 1
                        self.text_timer = 0
                    if self.final_char_index >= len(self.message):
                        self.final_text_display_complete = True
                text_surface = self.font.render(self.final_current_text, True, (255, 255, 255))
                text_x = portrait_x + self.rouxls_angry.get_width() + 20
                text_y = textbox_y + (self.Text_box.get_height() - text_surface.get_height()) // 3
                self.screen.blit(text_surface, (text_x, text_y))

    def animate_character(self):
        self.frame_counter += 1
        if self.frame_counter >= 5:
            if self.indice < len(self.rouxls_appear) - 1:
                self.indice += 1
                self.frame_counter = 0
            elif not self.show_textbox:
                self.show_textbox = True
                self.start_text_time = pygame.time.get_ticks()

    def handle_state_transitions(self):
        if self.game_state == "pre_blue_wait":
            if pygame.time.get_ticks() - self.wait_start_time >= 2000:
                self.game_state = "blue_screen"
                self.bs_animation_index = 0
                self.bs_frame_counter = 0
                self.wait_start_time = pygame.time.get_ticks()

        if self.game_state == "blue_screen":
            if pygame.time.get_ticks() - self.wait_start_time >= 2000:
                self.game_state = "pre_final_wait"
                self.sad_animation_start_time = pygame.time.get_ticks()

        if self.game_state == "pre_final_wait":
            if pygame.time.get_ticks() - self.sad_animation_start_time >= 2000:
                self.game_state = "final_dialogue"
                self.final_dialogue_index = 0
                self.message = self.final_dialogue[self.final_dialogue_index]
                self.final_current_text = ""
                self.final_char_index = 0
                self.final_text_display_complete = False

    def handle_sound(self):
        if self.game_state == "dialogue":
            if not self.flag1:
                self.teleport_sound.play()
                self.flag1 = True
                self.ticks_after_first_sound = pygame.time.get_ticks()

            if self.flag1 and not self.flag2:
                if pygame.time.get_ticks() - self.ticks_after_first_sound >= 2300:
                    pygame.mixer.music.play(-1)
                    self.flag2 = True
def run_animation():
    try:
        pygame.init()
        animation = RouxlsAnimation()
        animation.run()
    except Exception as e:
        print(f"Error en la animación: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    run_animation()