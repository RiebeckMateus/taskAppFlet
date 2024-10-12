import flet as ft
from custom_checkbox import CustomCheckBox
from circle_asset import circle

class FletClass():
    def __init__(self):
        pass
    
    def main(self, page: ft.Page):
        
        BG = '#041955'
        FWG = '#97B4FF'
        FG = '#3450A1'
        PINK = '#EB06FF'
        
        def shrink(e):
            page_2.controls[0].width = 120
            page_2.controls[0].scale = ft.transform.Scale(
                0.8, alignment=ft.alignment.center_right
            )
            page_2.controls[0].border_radius=ft.border_radius.only(
                top_left=35,
                top_right=0,
                bottom_left=35,
                bottom_right=0
            )
            page_2.update()
        
        def restore(e):
            page_2.controls[0].width = 400
            page_2.controls[0].scale = ft.transform.Scale(
                1, alignment=ft.alignment.center_right
            )
            page_2.update()
        
        create_task_view = ft.Container(
            content=ft.Container(
                bgcolor=PINK,
                on_click=lambda _: page.go('/'),
                height=40,
                width=40,
                content=ft.Icon(ft.icons.CLOSE)
            )
        )
        
        tasks = ft.Column(
            height=400,
            scroll='auto',
            # controls=[
            #     ft.Container(height=50, width=300, bgcolor='red')
            # ]
        )
        
        for i in range(10):
            tasks.controls.append(
                ft.Container(
                    height=70,
                    width=400,
                    bgcolor=BG,
                    border_radius=25,
                    padding=ft.padding.only(
                        left=20,
                        top=22
                    ),
                    content=CustomCheckBox(
                        color=PINK,
                        label='Create interesting content!')
                )
            )
        
        categories_card = ft.Row(
            scroll='auto'
        )
        categories = ['Trabalho', 'Familia', 'Amigos']
        for i, category in enumerate(categories):
            categories_card.controls.append(
                ft.Container(
                    bgcolor=BG,
                    height=110,
                    width=170,
                    padding=15,
                    border_radius=20,
                    content=ft.Column(
                        controls=[
                            ft.Text('40 Tasks'),
                            ft.Text(category),
                            ft.Container(
                                width=160,
                                height=5,
                                bgcolor='white12',
                                border_radius=20,
                                padding=ft.padding.only(right=i*30),
                                content=ft.Container(
                                    bgcolor=PINK
                                )
                            )
                        ]
                    )
                )
            )
        
        first_page_contents = ft.Container(
            # bgcolor='#A456A7',
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment='spaceBetween',
                        controls=[
                            ft.Container(
                                content=ft.Icon(ft.icons.MENU),
                                on_click=lambda e: shrink(e)
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.icons.SEARCH),
                                    ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED),
                                ]
                            ),
                        ]
                    ),
                    ft.Container(
                        # espaçamento
                        height=20
                        ),
                    ft.Text(
                        value='Diz aí, Mateus!!',
                        size=20,
                        font_family='poppins'
                    ),
                    ft.Text(
                        value='Categorias'
                    ),
                    ft.Container(
                        padding=ft.padding.only(
                            top=10,
                            bottom=20
                        ),
                        content=categories_card
                    ),
                    ft.Text(
                        value='Tarefas de hoje'
                    ),
                    ft.Stack(
                        controls=[
                            tasks,
                            ft.FloatingActionButton(
                                icon=ft.icons.ADD,
                                on_click=lambda _: page.go('/create_task'),
                                bottom=2,
                                right=20
                            )
                        ]
                    )
                    
                ]
            )
        )
        
        page_1 = ft.Container(
            width=400,
            height=850,
            bgcolor=BG,
            border_radius=35,
            padding=ft.padding.only(left=50, top=60, right=200),
            
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment='end',
                        controls=[
                            ft.Container(
                                height=35,
                                width=35,
                                border=ft.border.all(color='white', width=1),
                                content=ft.Icon(ft.icons.ARROW_BACK_IOS_NEW_OUTLINED),
                                on_click=lambda e: restore(e)
                            )
                        ]
                    ),
                    ft.Container(
                        height=20
                        ),
                    circle,
                    ft.Text('Mateus\nRiebeck', size=32, weight='bold'),
                    ft.Container(
                        height=20
                        ),
                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.icons.FAVORITE_BORDER_SHARP,
                                color='white60'
                                ),
                            ft.Text(
                                'Templates',
                                size=15,
                                weight=ft.FontWeight.W_300,
                                color='white',
                                font_family='poppins'
                                )
                        ]
                    ),
                    ft.Container(
                        height=5
                        ),
                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.icons.CARD_TRAVEL,
                                color='white60'
                                ),
                            ft.Text(
                                'Categories',
                                size=15,
                                weight=ft.FontWeight.W_300,
                                color='white',
                                font_family='poppins'
                                )
                        ]
                    ),
                    ft.Container(
                        height=5
                        ),
                    ft.Row(
                        controls=[
                            ft.Icon(
                                ft.icons.CALCULATE_OUTLINED,
                                color='white60'
                                ),
                            ft.Text(
                                'Analytics',
                                size=15,
                                weight=ft.FontWeight.W_300,
                                color='white',
                                font_family='poppins'
                                )
                        ]
                    )
                ]
            )
        )
        page_2 = ft.Row(
            alignment='end',
            # Row se caracteriza como uma div horizontal
            controls=[
                # controls são os elementos dentro dessa "div"
                ft.Container(
                    width=400,
                    height=850,
                    bgcolor=FG,
                    border_radius=35,
                    animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                    animate_scale=ft.animation.Animation(400, curve='decelerate'),
                    padding=ft.padding.only(
                        top=50,
                        left=20,
                        right=20,
                        bottom=5
                    ),
                    content=ft.Column(
                        # column se caracteriza como uma div vertical
                        controls=[
                            first_page_contents
                        ]
                    )
                )
            ]
        )
        
        container = ft.Container(
            width=400,
            height=850,
            bgcolor=BG,
            border_radius=35,
            # content são os widgets inclusos nesse container
            content=ft.Stack(
                # o stack serve pra colocar um elemente sobrepondo o outro em ordem
                controls=[
                    page_1,
                    page_2
                ]
            )
        )
        
        pages = {
            '/':ft.View(
                "/",
                [
                    container
                ],
            ),
            '/create_task':ft.View(
                "/create_task",
                [
                    create_task_view
                ],
            )
        }
        
        def route_change(event):
            page.views.clear()
            page.views.append(
                pages[page.route]
            )
            page.update()
        
        # page.add(container)
        
        page.on_route_change = route_change
        page.go(page.route)
        
# Instancia a classe e chama o método main
app_instance = FletClass()
ft.app(target=app_instance.main)
