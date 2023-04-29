import flet as ft
from caculate import *


def main(page: ft.Page):
    probability_input = ft.Ref[ft.TextField]()
    result_column = ft.Ref[ft.Column]()

    def calculate_click(e):
        probability = covert_float(probability_input.current.value)
        if probability == None:
            result_column.current.controls.append(
                ft.Text(
                    f"请输入符合要求的数n，要求n在0-1之间")
            )
            page.update()
        else:
            res = calculate_information_entropy(probability)
            result_column.current.controls.append(
                ft.Text(
                    f"概率{probability_input.current.value}对应信息熵是：{res:.3f} bits/符号")
            )
            probability_input.current.value = ''
            page.update()

    page.add(
        ft.Row([
            ft.TextField(ref=probability_input,
                         hint_text='1/9或0.32', label='概率',
                         autofocus=True),
            ft.ElevatedButton(text="计算自信息",
                              on_click=calculate_click),
        ])
    )
    page.add(ft.Column(ref=result_column))
    page.update()


ft.app(target=main)
