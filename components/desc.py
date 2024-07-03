import flet as ft

def main(page: ft.Page):
  page.bgcolor = ft.colors.BLACK

  details = ft.Container(
    content=ft.Column(
      controls=[
        ft.Text(
          value="Controles de video game",
          color=ft.colors.GREEN_400,
          weight=ft.FontWeight.BOLD
        ),
        ft.Text(
          value="Controle Tecnologico",
          color=ft.colors.WHITE,
          weight=ft.FontWeight.BOLD,
          size=30,
        ),
        ft.Text(
          value="Controle",
          color=ft.colors.GREY_300,
          italic=True
        ),
        ft.ResponsiveRow(
          controls=[
            ft.Text(col=6, value="R$299,00", color=ft.colors.WHITE, size=30),
            ft.Row(
              col=6,
              controls=[
                ft.Icon(name=ft.icons.DISCOUNT, color=ft.colors.GREEN_500),
                ft.Text(value="30% OFF", color=ft.colors.WHITE, size=30),
              ]
            )
          ]
        )
      ]
    ),
    padding=ft.padding.all(30),
    bgcolor=ft.colors.AMBER_100,
    border_radius=12,
  )

  layout = ft.Container(
    width=900,
    margin=ft.margin.all(30),
    shadow=ft.BoxShadow(blur_radius=250, color=ft.colors.RED_100),
    content=ft.Column(
      spacing=28,
      run_spacing=12,
      controls=[
        details
      ]
    )
  )

  page.add(layout)

ft.app(target=main)