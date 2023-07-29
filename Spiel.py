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

        self.total_time = 10

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
            if x > 400 and x < 700 and y > 290 and y < 380:
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
            if self.punkte != 3:
                self.total_time = self.total_time - delta_time


    # Spiel beenden mit der Taste 'Q' und Restarten mit der Taste 'R'
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
            arcade.draw_rectangle_outline(400, 290, 300, 90, arcade.color.WHITE, 5)
                              
        elif self.stufe == 1:
            self.gegenstand_liste.draw()
            self.hindernis_liste.draw()

            arcade.draw_text(self.punkte, 15, 15, arcade.color.WHITE, 30, font_name="Kenney Blocks")
            arcade.draw_text(round(self.total_time, 1), 785, 15, arcade.color.WHITE, 30, font_name="Kenny Blocks", anchor_x="right")

            



            # Spiel beenden 
            if self.punkte == 3:
                arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.GREEN)
                arcade.draw_text("GEWONNEN!", 400, 300, arcade.color.WHITE, 60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
                arcade.draw_text("Drücke die Taste 'R' um das Spiel zu wiederholen", 400, 100, arcade.color.WHITE, 15, font_name="Kenney Future", anchor_x="center", anchor_y="center")
                arcade.draw_text("Drücke die Taste 'Q' um das Spiel zu beenden", 400, 50, arcade.color.WHITE, 15, font_name="Kenney Future", anchor_x="center", anchor_y="center")
                arcade.draw_text("Deine Zeit:" + str(round(self.total_time, 1)), 400, 450, arcade.color.WHITE, 15, font_name="Kenney Future", anchor_x="center", anchor_y="center")

            elif self.total_time <= 0.0:
                arcade.draw_lrtb_rectangle_filled(0, 800, 600, 0, arcade.color.AMERICAN_ROSE)
                arcade.draw_text("Verloren!", 400, 300, arcade.color.WHITE, 60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
                arcade.draw_text("Drücke die Taste 'R' um das Spiel zu wiederholen", 400, 100, arcade.color.WHITE, 15, font_name="Kenney Future", anchor_x="center", anchor_y="center")
                arcade.draw_text("Drücke die Taste 'Q' um das Spiel zu beenden", 400, 50, arcade.color.WHITE, 15, font_name="Kenney Future", anchor_x="center", anchor_y="center")


        

intro = Spiel(800, 600, "Intro")
arcade.run()

