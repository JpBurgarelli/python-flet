import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    
    text = ft.Text(value="joao")

    div1 = ft.Container(
        content=ft.Column([
            ft.Text("nome: joao"),
            ft.Text("idade: 12")
        ]),
        bgcolor="#6e28d9",
        padding=12,
        border_radius=10
    )

    div2 = ft.Container(
        content=ft.Column([
            ft.Text("Estados: SP"),
            ft.Text("Pais: Brasil")
        ]),
        bgcolor="#6e28d9",
        padding=12,
        border_radius=10
    )

    container = ft.Container(
        content=ft.Row(
            controls=[
                div1,
                div2
            ],
            alignment="space_between",
        ),
        bgcolor="#6e28d9",
        padding=12,
        border_radius=10,
        width=600,
    )

    page.add(container)

ft.app(target=main)