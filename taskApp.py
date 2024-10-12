import flet as ft

class FletClass():
    def __init__(self):
        pass
    
    def main(self, page: ft.Page):
        
        BG = '#041955'
        FWG = '#97B4FF'
        FG = '#3450A1'
        PINK = '#EB06FF'
        
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
                    border_radius=25
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
            bgcolor='#A456A7',
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment='spaceBetween',
                        controls=[
                            ft.Container(
                                content=ft.Icon(ft.icons.MENU)
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
                        value='Diz aí, Mateus!!'
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
        
        page_1 = ft.Container()
        page_2 = ft.Row(
            # Row se caracteriza como uma div horizontal
            controls=[
                # controls são os elementos dentro dessa "div"
                ft.Container(
                    width=400,
                    height=850,
                    bgcolor=FG,
                    border_radius=35,
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
