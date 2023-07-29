import arcade, random


# Play window and sound
class Spiel(arcade.Window):


    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.WHITE)


        #self.hit_sound = arcade.load_sound("")
        self.stufe = 0

    def setup(self):
        arcade.set_background_color(arcade.color.YELLOW)
        self.stufe = 1
        self.gegenstand_liste = arcade.SpriteList()
        
        apple = arcade.Sprite("apple.png")
        apple.center_x = random.randrange(800)
        apple.center_y = random.randrange(600)
        self.gegenstand_liste.append(apple)
        
        bannane = arcade.Sprite("bannane.png")
        bannane.center_x = random.randrange(800)
        bannane.center_y = random.randrange(600)
        self.gegenstand_liste.append(bannane)
        
        carott = arcade.Sprite("carott.png")
        carott.center_x = random.randrange(800)
        carott.center_y = random.randrange(600)
        self.gegenstand_liste.append(carott)


        self.hindernis_liste = arcade.SpriteList()

        self.total_time = 20

        i = 1
        while i <= 10:
            fastfood = arcade.Sprite(random.choice(["pizza.png", "Burger.png", "cola.png", "Pommes.png"]))
            fastfood.center_x = random.randrange(800)
            fastfood.center_y = random.randrange(600)
            self.hindernis_liste.append(fastfood)
            i = i + 1

        self.punkte = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.stufe == 0:
            self.setup()
        elif self.stufe == 1:
            pseudosprite = arcade.Sprite()
            pseudosprite.center_x = x
            pseudosprite.center_y = y
            pseudosprite.set_hit_box([(1, 1), (-1, -1), (-1, 1), (1, -1)])


            gegenstand_hitliste = arcade.check_for_collision_with_list(pseudosprite, self.gegenstand_liste)

            index = 0
            while index < len(gegenstand_hitliste):
                gegenstand_hitliste[index].kill()
                self.punkte = self.punkte + 1
                index = index + 1


    # Timer
    def on_update(self, delta_time):
        if self.stufe == 1:
            self.total_time = self.total_time - delta_time
        
       
    # Spiel beenden mit der Taste 'Q'
    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()
        elif key == arcade.key.R:
            self.setup()




            


    def on_draw(self):
        self.clear()

        if self.stufe == 0:
            arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.YELLOW)
            arcade.draw_text("PLAY!", 400, 300, arcade.color.WHITE, 60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
            arcade.draw_text("Play", 800 / 2, 600 / 2, arcade.color.WHITE, font_size = 50, anchor_x = "center")
        elif self.stufe == 1:
            self.gegenstand_liste.draw()
            self.hindernis_liste.draw()

            arcade.draw_text(self.punkte, 15, 15, arcade.color.WHITE, 30, font_name="Kenney Blocks")
            arcade.draw_text(round(self.total_time, 1), 785, 15, arcade.color.WHITE, 30, font_name="Kenny Blocks", anchor_x="right")



            # Timer 
            minutes = int(self.total_time) // 60
            seconds = int(self.total_time) % 60
            output = f"Time: {minutes:02d}:{seconds:02d}s"

            arcade.draw_text(output, 10, 10, arcade.color.WHITE, 14)
            

            self.gegenstand_liste.draw()
            self.hindernis_liste.draw()

            arcade.draw_text(self.punkte, 20, 20, arcade.color.WHITE, 30, font_name="Kenney Blocks")

        

            # Spiel beenden 
            if self.punkte == 3:
                arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.GREEN)
                arcade.draw_text("GEWONNEN!", 400, 300, arcade.color.WHITE, 60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
                arcade.draw_text("Drück die Taste 'R' um das Spiel zu wiederholen", 400, 100, arcade.color.WHITE, 15, font_name="Kenney Future", anchor_x="center", anchor_y="center")

            if self.total_time <= 0.0:
                arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.BLACK_BEAN)
                arcade.draw_text("Game over!", 400, 300, arcade.color.WHITE, 60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")

        

intro = Spiel(800, 600, "Intro")
arcade.run()

...