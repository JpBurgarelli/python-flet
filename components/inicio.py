import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    loginPage = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    height=500,
                    image_src="https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    image_fit="cover",
                    border_radius=12
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(value="RecipeIn", color=ft.colors.RED_300, size=60),
                            ft.ElevatedButton(
                                height=50,
                                width=200,
                                text="Login",
                                style=ft.ButtonStyle(
                                    padding=ft.padding.all(10),
                                    color=ft.colors.BLACK,
                                    side={
                                        ft.MaterialState.DEFAULT: ft.BorderSide(width=0.5, color="#ffffff"),
                                    },
                                    bgcolor={
                                        ft.MaterialState.DEFAULT: "#FF4F4F",
                                        ft.MaterialState.HOVERED: "#FFFF99",
                                    }
                                ),
                                content=ft.Row(
                                    [
                                        ft.Text(value="Login", color=ft.colors.BLACK, size=25, weight=ft.FontWeight.BOLD)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ),
                            ft.ElevatedButton(
                                height=50,
                                width=200,
                                text="Login",
                                style=ft.ButtonStyle(
                                    padding=ft.padding.all(10),
                                    color=ft.colors.BLACK,
                                    side={
                                        ft.MaterialState.DEFAULT: ft.BorderSide(width=0.5, color="#ffffff"),
                                    },
                                    bgcolor={
                                        ft.MaterialState.DEFAULT: "#FFFF99",
                                        ft.MaterialState.HOVERED: "#FF4F4F",
                                    }
                                ),
                                content=ft.Row(
                                    [
                                        ft.Text(value="Sing up", color=ft.colors.BLACK, size=25, weight=ft.FontWeight.BOLD)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ),
                        ]
                    ),
                    alignment=ft.alignment.center
                )
            ]
        ),
    )


    layout = ft.Container(
        width=390,
        height=844,
        margin=ft.margin.all(30),
        border_radius=ft.border_radius.all(10),
        border=ft.border.all(2, "#C0C2C9"),
        content=ft.Column(
            spacing=28,
            run_spacing=12,
            controls=[
                loginPage
            ]
        )
    )

    page.add(layout)

ft.app(target=main)
