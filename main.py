import flet as ft

async def main (page: ft.Page):
    page.window_width=720
    page.window_height=1200
    page.window_resizable=False
    page.padding=0
    page.scroll="HIDDEN"
    
    boton_azul=ft.Stack([
        ft.Container(width=80,height=80,bgcolor=ft.colors.WHITE,border_radius=50),
        ft.Container(width=70,height=70,left=5,top=5,bgcolor=ft.colors.BLUE,border_radius=50)
    ])
    items_superior=[
        ft.Container(boton_azul,width=80,height=80),
        ft.Container(width=40,height=40,bgcolor=ft.colors.RED_200,border_radius=50),
        ft.Container(width=40,height=40,bgcolor=ft.colors.YELLOW,border_radius=50),
        ft.Container(width=40,height=40,bgcolor=ft.colors.GREEN,border_radius=50)
    ]
    stack_central=ft.Stack([
        ft.Container(width=500,height=400,bgcolor=ft.colors.WHITE),
        ft.Container(width=450,height=350,bgcolor=ft.colors.BLACK,left=25,top=25),
        ft.Image(
            scale=5,
            width=50,
            height=50,
            top=350/2,
            right=450/2,
            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"
        )
    ])

    superior=ft.Container(content=ft.Row(items_superior),width=600,height=80,margin=ft.margin.only(top=20),border=ft.border.all())
    centro=ft.Container(content=stack_central,width=600,height=400,margin=ft.margin.only(top=40),
                        alignment=ft.alignment.center)
    inferior=ft.Container(width=600,height=400,margin=ft.margin.only(top=40),border=ft.border.all())

    col=ft.Column(spacing=0,controls=[
        superior,
        centro,
        inferior,
    ]
    )
    
    Contenedor=ft.Container(col,width=720,height=1200,bgcolor=ft.colors.RED,alignment=ft.alignment.top_center)
    
    await page.add_async(Contenedor)


ft.app(target = main)