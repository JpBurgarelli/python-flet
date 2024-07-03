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
            ft.Text(col={'xs': 12, 'sm':6 }, value="R$299,00", color=ft.colors.WHITE, size=30),
            ft.Row(
              col={'xs': 12, 'sm':6 },
              controls=[
                ft.Icon(name=ft.icons.DISCOUNT, color=ft.colors.GREEN_500),
                ft.Text(value="30% OFF", color=ft.colors.WHITE, size=30),
              ]
            )
          ]
        ),
        ft.Tabs(
          selected_index=0, #Por Tab padrao selecionado
          indicator_color=ft.colors.RED_400,
          label_color=ft.colors.RED_400,
          unselected_label_color=ft.colors.WHITE,
          tabs=[
            ft.Tab(
              text="XBOX",
            ),
            ft.Tab(
              text="PS5",
           
            ),
            
          ]
        ),

        ft.ResponsiveRow(
          controls=[
            ft.Dropdown(
              col=6,
              label="tipo de controle",
              label_style=ft.TextStyle(color="#ffffff", size=16),
              border_color=ft.colors.RED_400,
              border_width=0.5,
              options=[
                ft.dropdown.Option("Gamer"),
                ft.dropdown.Option("Casual"),
                ft.dropdown.Option("Colecionador"),
              ]
            ),
            
            ft.Dropdown(
              col=6,
              label="Quantidade",
              label_style=ft.TextStyle(color="#ffffff", size=16),
              border_color=ft.colors.RED_400,
              border_width=0.5,
              options=[
                #ft.dropdown.Option(text=f"{num} uni.") for num in range(1, 6),
                ft.dropdown.Option("1 controle"),
                ft.dropdown.Option("2 controle"),
                ft.dropdown.Option("3 controle"),

              ]
            )
          ]
        ),

        ft.Container(
          height=300,
          image_src="https://images.unsplash.com/photo-1578898395216-78dae5d29344?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          image_fit="cover",
          border_radius=12
        ),

        ft.ElevatedButton(
          width=150,
          text="Comprar",
          style=ft.ButtonStyle(
            padding=ft.padding.all(5),
            #bgcolor=ft.colors.RED_400,
            color=ft.colors.WHITE,
            side={
              ft.MaterialState.DEFAULT: ft.BorderSide(width=0.5, color="#ffffff"),
            },
            bgcolor={
              ft.MaterialState.DEFAULT: ft.colors.RED_400,
              ft.MaterialState.HOVERED: ft.colors.GREY_400,
            }
          )
        )
        

      
      

      ]
    ),
    padding=ft.padding.all(30),
    border_radius=12,
  )

  layout = ft.Container(
    width=900,
    height=900,
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