from pcconfig import config
import pynecone as pc

globalStyle = {
    ":root": {
        "--topbar-colour": "#2b2b2b",
        "--background-colour": "#1c1d20",
        "--button-colour": "#e2b5b5",
    },
    "background-color": "#1c1d20",
    "color": "white",
    "overflow": "hidden",

}

class State(pc.State):
    #App State
    pass

# _________________________________________________________________________________________________________________________________________________________________ #

def index():
    return pc.vstack(
        pc.box(
            pc.link("Token", _hover={"text_decoration": "none", "color": "purple"}),
            width="100%",
            background_color="#2b2b2b",
            font_size="1.5em",
            font_weight="bold",
            padding_left="2em",
        ),
        pc.hstack(
            pc.box(
                "Welcome To ",
                pc.span("Token", color="#e2b5b5"),
                pc.text("""Token """, pc.span("is a small chat app build with ", color="white"), pc.span("Pynecone.", color="#e2b5b5"), color="#e2b5b5"),
                pc.text("""All code is on """, pc.link("Github.", color="#e2b5b5", href="https://github.com/tomosus/Token", is_external=True, _hover={"text_decoration": "none", "color": "purple"})),
            pc.link(
                "Join Token",
                background_color="#1c1d20",
                border="1px solid white",
                _hover={"background_color": "purple"},
                font_weight="bold",
                color="white",
                href="/login",
                font_size=".7em",
                padding="1%",
                border_radius="25px",
            ),
            font_size="2em",
            font_weight="bold",
            width="40%",
            margin_top="10%",
            margin_left="5%",
        ),
        pc.image(
            src="https://bitcoinik.com/wp-content/uploads/2021/11/shiba-gaming-scaled.jpg",
            height="auto",
            width="40%",
            padding_top="10%",
            padding_left="5%",
        ),
        )
    )

# _________________________________________________________________________________________________________________________________________________________________ #

def login():
    return pc.vstack(
        pc.box(
            pc.link("Token", _hover={"text_decoration": "none", "color": "purple"}, href="/"),
            width="100%",
            background_color="#2b2b2b",
            font_size="1.5em",
            font_weight="bold",
            padding_left="2em",
        ),

        pc.box(
            pc.form_control(
                pc.form_label("EMAIL", html_for="email", font_weight="bold"),
                pc.input(type_="email", placeholder="Enter your email.."),

                pc.form_label("PASSWORD", html_for="password", margin_top="1em", font_weight="bold"),
                pc.input(type_="password", placeholder="Enter your password.."),

                pc.button("Login", margin_top="1em", font_weight="bold", background_color="#e2b5b5", _hover={"background_color": "purple"}),
                pc.text("Don\'t have an account? ", pc.span(pc.link("Sign up here!", href="/register"), color="#e2b5b5"), margin_top="10px"),

                is_required=True,
                margin_top="70%",
                background_color="#2b2b2b",
                padding="3em",
                border_radius="25px",
            ),
        ),
    )

# _________________________________________________________________________________________________________________________________________________________________ #

def register():
    return pc.vstack(
        pc.box(
            pc.link("Token", _hover={"text_decoration": "none", "color": "purple"}, href="/"),
            width="100%",
            background_color="#2b2b2b",
            font_size="1.5em",
            font_weight="bold",
            padding_left="2em",
        ),

        pc.box(
            pc.form_control(
                pc.form_label("USERNAME", html_for="username", font_weight="bold"),
                pc.input(type_="username", placeholder="Enter your username.."),

                pc.form_label("EMAIL", html_for="email", font_weight="bold"),
                pc.input(type_="email", placeholder="Enter your email.."),

                pc.form_label("PASSWORD", html_for="password", margin_top="1em", font_weight="bold"),
                pc.input(type_="password", placeholder="Enter your password.."),

                pc.form_label("CONFIRM PASSWORD", html_for="password", margin_top="1em", font_weight="bold"),
                pc.input(type_="password", placeholder="Enter your password again.."),

                pc.button("Sign up", margin_top="1em", font_weight="bold", background_color="#e2b5b5", _hover={"background_color": "purple"}),
                pc.text("Already have an account? ", pc.link("Back to Login", href="/login", color="#e2b5b5"), margin_top="10px"),

                is_required=True,
                margin_top="50%",
                background_color="#2b2b2b",
                padding="3em",
                border_radius="25px",
            ),
        ),
    )

# _________________________________________________________________________________________________________________________________________________________________ #

app = pc.App(state=State, style=globalStyle)
app.add_page(index, title="Token")
app.add_page(login, title="Token - Login")
app.add_page(register, title="Token - Register")
app.compile()