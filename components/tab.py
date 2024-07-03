import flet as ft

def main(page: ft.Page):

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        indicator_color=ft.colors.RED_400,
        label_color=ft.colors.RED_400,
        unselected_label_color=ft.colors.WHITE,
        tabs=[
            ft.Tab(
                text="XBOS",
                content=ft.Container(
                    content=ft.Text("O controle de video game é um dispositivo essencial para a experiência de jogo. Equipado com botões, alavancas e gatilhos, ele permite um controle preciso dos personagens e ações. Seu design ergonômico oferece conforto durante longas sessões, enquanto a conectividade sem fio proporciona liberdade de movimento.O controle de video game é um dispositivo essencial para a experiência de jogo. Equipado com botões, alavancas e gatilhos, ele permite um controle preciso dos personagens e ações. Seu design ergonômico oferece conforto durante longas sessões, enquanto a conectividade sem fio proporciona liberdade de movimento."), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="XBOX",
                content=ft.Container(
                    content=ft.Text("O controle de video game é um dispositivo essencial para a experiência de jogo. Equipado com botões, alavancas e gatilhos, ele permite um controle preciso dos personagens e ações. Seu design ergonômico oferece conforto durante longas sessões, enquanto a conectividade sem fio proporciona liberdade de movimento.O controle de video game é um dispositivo essencial para a experiência de jogo. Equipado com botões, alavancas e gatilhos, ele permite um controle preciso dos personagens e ações. Seu design ergonômico oferece conforto durante longas sessões, enquanto a conectividade sem fio proporciona liberdade de movimento."), alignment=ft.alignment.center
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)

ft.app(target=main)