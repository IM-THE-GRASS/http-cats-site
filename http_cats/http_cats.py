"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random
from rxconfig import config
from reflex_motion import motion

class State(rx.State):
    codes = [100,101,102,103,200,201,202,203,204,205,206,207,208,301,301,303,304,305,306,307,308,401,402,403,404,405,406,407,408,409,410,411,413,415,416,417,418,419,420,421,422,423,424,425,426,428,429,431,451,500,501,502,503,504,505,506,507,508,509,510,511]
    cat_img:str = "https://http.cat/404.jpg"
    def random_cat(self):
        cat_num = self.codes[random.randrange(0, len(self.codes))]
        self.cat_img = f"https://http.cat/{cat_num}.jpg"
        
    def set_text(self, text):
        try:
            self.cat_img = f"https://http.cat/{int(text)}.jpg"
        except:
            self.cat_img = "https://http.cat/404.jpg"
        
    


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading(
                    "HTTP error cats", 
                    font_size = "50px", 
                    margin_top="1%", 
                    color_scheme="green"
                ),
                rx.hstack(
                    rx.text("error code:", margin_top="0.5%"),
                    motion(
                        rx.input(
                            placeolder="haii",
                            on_change= State.set_text,
                            width = "22vw"
                        ),
                        initial={"scale": 1},
                        while_hover={"scale": 1.05},
                        while_tap={"scale": 0.9},
                        transition={"type": "spring", "stiffness": 260, "damping": 20},
                    
                    ),
                    motion(
                        rx.button(
                            "random cat",
                            variant= "surface",
                            width = "auto",
                            on_click=State.random_cat
                        ),
                        initial={"scale": 1},
                        while_hover={"scale": 1.1},
                        while_tap={"scale": 0.9, "rotate": 5},
                        transition={"type": "spring", "stiffness": 260, "damping": 20},
                    ),
                    width= "40vw"
                    
                ),
                rx.image(
                    src=State.cat_img,
                    width="40vw",
                    height="auto",
                    
                ),
                spacing="4",
            ),
            margin_top = "5vh"
        ),
        
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="green",
    )
)
app.add_page(index)
