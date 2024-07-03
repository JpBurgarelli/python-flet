import flet as ft

class CustomButton(ft.ElevatedButton):
    def __init__(self, text="", bgcolor="#FFFFFF", color="#000000", on_click=None, **kwargs):
        super().__init__(text=text, on_click=on_click, bgcolor=bgcolor, color=color, **kwargs)

def main(page: ft.Page):

    def submit_clicked(e):
        name_display.value = f"Primeiro Nome: {nameField.value}"
        last_name_display.value = f"Último Nome: {lastNameField.value}"
        nameField.value = f"formulario enviado com sucesso!"
        lastNameField.value = f"formulario enviado com sucesso!"
        page.update()

    def reset_clicked(e):
        nameField.value = ""
        lastNameField.value = ""
        name_display.value = ""
        last_name_display.value = ""
        page.update()

    def toggle_switch(e):
        nameField.visible = not nameField.visible
        lastNameField.visible = not lastNameField.visible
        page.update()

    textoPrincipal = ft.Text("Formulario Teste", theme_style=ft.TextThemeStyle.DISPLAY_LARGE)

    nameField = ft.TextField(label="Primeiro Nome", hint_text="Digite o primeiro nome aqui")
    lastNameField = ft.TextField(label="Último Nome", hint_text="Digite o último nome aqui")

    btn_enviar = ft.ElevatedButton(text="Enviar", on_click=submit_clicked, color="#2196F3")
    btn_resetar = ft.ElevatedButton(text="Resetar", on_click=reset_clicked,  color="#F44336")

    switch = ft.Switch(label="Toggle", on_change=toggle_switch)

    name_display = ft.Text(value="", size=20, color="#000000")
    last_name_display = ft.Text(value="", size=20, color="#000000")

    row = ft.Row(
        controls=[
            btn_enviar,
            btn_resetar,
            switch
        ]
    )

    page.add(textoPrincipal, nameField, lastNameField, row, name_display, last_name_display)

ft.app(target=main)
