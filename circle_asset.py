from flet import *

BG = '#041955'
FWG = '#97B4FF'
FG = '#3450A1'
PINK = '#EB06FF'

circle = Stack(
    controls=[
        Container(
            width=100,
            height=100,
            border_radius=50,
            bgcolor='white12'
        ),
        Container(
            gradient=SweepGradient(
                center=alignment.center,
                start_angle=0.0,
                end_angle=3,
                stops=[0.5,0.5],
                colors=['#00000000', PINK],
            ),
            width=100,
            height=100,
            border_radius=50,
            content=Row(
                alignment='center',
                controls=[
                    Container(
                        padding=padding.all(5),
                        bgcolor=BG,
                        width=90,height=90,
                        border_radius=50,
                        content=Container(
                            bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                            content=CircleAvatar(
                                opacity=0.8,
                                foreground_image_url="https://avatars.githubusercontent.com/u/142684931?v=4"
                            )
                        )
                    )
                ],
            ),
        ),
    ]
)