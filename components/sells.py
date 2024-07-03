import flet as ft

def main(page: ft.Page):
  page.bgcolor = ft.colors.BLACK

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
        content=ft.Row([
            ft.Text("Estados: SP"),
            ft.Text("Pais: Brasil")
        ]),
        bgcolor="#6e28d9",
        padding=12,
        border_radius=10
    )

  layout = ft.Container(
    width=900,
    margin=ft.margin.all(30),  
    shadow=ft.BoxShadow(blur_radius=250, color=ft.colors.RED_100),
    content=ft.Row(
      spacing=28,
      run_spacing=12,
      controls=[
        div1,
        div2
      ]
    )
  )

  page.add(layout)

ft.app(target=main)