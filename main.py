import flet as ft
import asyncio
import aiohttp

pokemon_actual=-1

async def main (page: ft.Page):
    page.window_width=720
    page.window_height=1200
    page.window_resizable=False
    page.padding=0
    page.scroll="HIDDEN"
    page.fonts={
        "zpix":"https://github.com/SolidZORO/zpix-pixel-font/releases/download/v1.2.1/zpix-v1.2.1-legacy.ttf"
    }
    page.theme=ft.Theme(font_family="zpix")
    
    async def peticion_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def evento_get_pokemon(e: ft.ContainerTapEvent):
        global pokemon_actual
        if e.control == flecha_superior:
            pokemon_actual+=1
        else:
            pokemon_actual-=1
        numero = (pokemon_actual%150)+1
        resultado= await peticion_url(f"https://pokeapi.co/api/v2/pokemon/{numero}")
        datos = f"Name: {resultado['name']}\n \nAbilities: "
        for elemento in resultado['abilities']:
            habilidad = elemento['ability']['name']
            datos +=f"\n{habilidad}" 
        datos +=f"\nHeight:{resultado['height']}"    
        texto.value= datos
        sprite_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{numero}.png"
        imagen.src=sprite_url
        await page.update_async()
    
    async def blink():
        while True:
            await asyncio.sleep(1)
            luz_azul.bgcolor=ft.colors.BLUE_100
            await page.update_async()
            await asyncio.sleep(0.1)
            luz_azul.bgcolor=ft.colors.BLUE
            await page.update_async()
            

    luz_azul=ft.Container(width=70,height=70,left=5,top=5,bgcolor=ft.colors.BLUE,border_radius=50)
    boton_azul=ft.Stack([
        ft.Container(width=80,height=80,bgcolor=ft.colors.WHITE,border_radius=50),
        luz_azul
    ])
    items_superior=[
        ft.Container(boton_azul,width=80,height=80),
        ft.Container(width=40,height=40,bgcolor=ft.colors.RED_200,border_radius=50),
        ft.Container(width=40,height=40,bgcolor=ft.colors.YELLOW,border_radius=50),
        ft.Container(width=40,height=40,bgcolor=ft.colors.GREEN,border_radius=50)
    ]
    sprite_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
    imagen=ft.Image(
        scale=5,
        width=50,
        height=50,
        top=350/2,
        right=450/2,
        src=sprite_url
    )
    stack_central=ft.Stack([
        ft.Container(width=500,height=400,bgcolor=ft.colors.WHITE,border_radius=20),
        ft.Container(width=450,height=350,bgcolor=ft.colors.BLACK,left=25,top=25),
        imagen
    ])

    icono_flecha=ft.Image(src="arrow.png")
    flecha_superior=ft.Container(content=icono_flecha,rotate=3.14159,width=80,height=50,on_click=evento_get_pokemon)
    flechas=ft.Column([
        flecha_superior,
        ft.Container(content=icono_flecha,width=80,height=50,on_click=evento_get_pokemon),
    ])
    texto=ft.Text(value="...",
                  color=ft.colors.BLACK,
                  size=22
                  )
    items_inferior=[
        ft.Container(width=50),#Margen Izquierdo
        ft.Container(content=texto,padding=10,width=400,height=300,bgcolor=ft.colors.GREEN,border_radius=20), #Pantalla de descipcion
        ft.Container(content=flechas,width=80,height=120), #Selectores
        ft.Container(width=50)#Margen Derecho
    ]
    superior=ft.Container(content=ft.Row(items_superior),width=600,height=80,margin=ft.margin.only(top=20))
    centro=ft.Container(content=stack_central,width=600,height=400,margin=ft.margin.only(top=40),
                        alignment=ft.alignment.center)
    inferior=ft.Container(content=ft.Row(items_inferior),width=600,height=400,margin=ft.margin.only(top=40))

    col=ft.Column(spacing=0,controls=[
        superior,
        centro,
        inferior
    ]
    )
    
    Contenedor=ft.Container(col,width=720,height=1200,bgcolor=ft.colors.RED,alignment=ft.alignment.top_center)
    
    await page.add_async(Contenedor)
    await blink()

ft.app(target = main)
ass=1