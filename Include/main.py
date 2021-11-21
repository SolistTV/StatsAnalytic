import tkinter
from tkinter import *
import math

window = Tk()

# icon = PhotoImage(file='Src/Neverwinter.png')
bg_color = '#5aab98'
submit_bg_color = '#53d900'
field_bg_color = '#b9b7b7'
submit_font_color = '#000000'
parameters_font_style = 'Arial 10 bold'
parameters_width = 35
cells_width = 16

window.title("Stats analytic")
window.geometry("970x735+200+200")
window.resizable(False, False)
# window.minsize(1000, 750)
# window.iconphoto(False, icon)
window.config(bg=bg_color)

parameters = {
    'oup': {
        'name': 'Общий уровень предметов',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 30000,
        'default_value_2': 50000,
    },
    'power': {
        'name': 'Могущество',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 50,
        'default_value_2': 70,
    },
    'accuracy': {
        'name': 'Точность',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 50,
        'default_value_2': 70,
    },
    'bp': {
        'name': 'Боевое преимущество',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 50,
        'default_value_2': 70,
    },
    'crit_chance': {
        'name': 'Шанс крит. удара',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 50,
        'default_value_2': 70,
    },
    'crit': {
        'name': 'Крит. урон',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 50,
        'default_value_2': 70,
    },
    'percent_bonus': {
        'name': 'Бонус к урону',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 60,
        'default_value_2': 90,
    },
    'damage_boost': {
        'name': 'Бонус к маг/физ урону',
        'value': '',
        'label': Label(),
        'input_1': Entry(),
        'input_2': Entry(),
        'damage_part_1': Label(),
        'damage_part_2': Label(),
        'default_value_1': 5,
        'default_value_2': 8,
    },
}

row_index = 0
col_index = 0

Label(
    window,
    text='Параметры',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=parameters_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, rowspan=2, sticky='sn', column=0, padx=10, pady=10)

Label(
    window,
    text='Билд 1',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=parameters_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, column=1, columnspan=2, sticky='ew', padx=10, pady=10)

Label(
    window,
    text='Билд 2',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=parameters_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, column=3, columnspan=2, sticky='ew', padx=10, pady=10)

row_index += 1

Label(
    window,
    text='Процент стат',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=cells_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, column=1, sticky='ew', padx=10, pady=10)

Label(
    window,
    text='Множитель урона',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=cells_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, column=2, sticky='ew', padx=10, pady=10)

Label(
    window,
    text='Процент стат',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=cells_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, column=3, sticky='ew', padx=10, pady=10)

Label(
    window,
    text='Множитель урона',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=cells_width,
    anchor='center',
    justify=CENTER,
).grid(row=row_index, column=4, columnspan=2, sticky='ew', padx=10, pady=10)
row_index += 1


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def validate(input_value):
    if input_value is '':
        return True

    if is_float(input_value):
        return True
    else:
        return False


validate_field = window.register(validate)
for key, Parameter in parameters.items():
    Parameter['label'] = Label(
        window,
        text=Parameter['name'] + ':',
        font=parameters_font_style,
        padx=5,
        pady=5,
        width=parameters_width,
        anchor='e',
        justify=RIGHT,
    ).grid(row=row_index, column=0, padx=10, pady=10)

    Parameter['input_1'] = Entry(
        window,
        justify=CENTER,
        font=parameters_font_style,
        bg=field_bg_color
    )

    Parameter['input_1'].insert(0, Parameter['default_value_1'])
    Parameter['input_1'].grid(row=row_index, column=1)
    Parameter['input_1'].config(validate="key", validatecommand=(validate_field, '%P'))
    Parameter['input_2'] = Entry(
        window,
        justify=CENTER,
        font=parameters_font_style,
        bg=field_bg_color
    )

    Parameter['input_2'].insert(0, Parameter['default_value_2'])
    Parameter['input_2'].grid(row=row_index, column=3)
    if key == 'crit_chance':
        Parameter['damage_part_1'] = Label(
            window,
            text='0',
            font=parameters_font_style,
            width=cells_width,
            justify=CENTER,
        )

        Parameter['damage_part_1'].grid(row=row_index, column=2, rowspan=2, sticky='ns', padx=10)
        Parameter['damage_part_2'] = Label(
            window,
            text='0',
            font=parameters_font_style,
            width=cells_width,
            justify=CENTER,
        )

        Parameter['damage_part_2'].grid(row=row_index, column=4, rowspan=2, sticky='ns', padx=10)
    elif key != 'crit':
        Parameter['damage_part_1'] = Label(
            window,
            text='0',
            font=parameters_font_style,
            width=cells_width,
            justify=CENTER,
        )

        Parameter['damage_part_1'].grid(row=row_index, column=2, padx=10)
        Parameter['damage_part_2'] = Label(
            window,
            text='0',
            font=parameters_font_style,
            width=cells_width,
            justify=CENTER,
        )

        Parameter['damage_part_2'].grid(row=row_index, column=4, padx=10)

    row_index += 1

Label(
    window,
    text='Нанесенный урон магнитудой 100 ед:',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=parameters_width,
    anchor='e',
    justify=RIGHT,
).grid(row=row_index, column=0, padx=10, pady=10)

builds = {
    'damage_1' : Label(
        window,
        text='0',
        font=parameters_font_style,
        padx=5,
        pady=5,
        width=parameters_width,
        anchor='center',
        justify=CENTER,
    ),
    'damage_2' : Label(
        window,
        text='0',
        font=parameters_font_style,
        padx=5,
        pady=5,
        width=parameters_width,
        anchor='center',
        justify=CENTER,
    ),
    'damage_diff' : Label(
        window,
        text='0%',
        font=parameters_font_style,
        padx=5,
        pady=5,
        width=parameters_width,
        anchor='center',
        justify=CENTER,
    ),
    'total_stats_1' : Label(
        window,
        text='0%',
        font=parameters_font_style,
        padx=5,
        pady=5,
        width=parameters_width,
        anchor='center',
        justify=CENTER,
    ),
    'total_stats_2' : Label(
        window,
        text='0%',
        font=parameters_font_style,
        padx=5,
        pady=5,
        width=parameters_width,
        anchor='center',
        justify=CENTER,
    ),
}

builds['damage_1'].grid(row=row_index, column=1, columnspan=2, padx=10, pady=10)
builds['damage_2'].grid(row=row_index, column=3, columnspan=2, padx=10, pady=10)
row_index += 1
Label(
    window,
    text='Разница в уроне:',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=parameters_width,
    anchor='e',
    justify=RIGHT,
).grid(row=row_index, column=0, padx=10, pady=10)
builds['damage_diff'].grid(row=row_index, column=1, columnspan=4, sticky='ew', padx=10, pady=10)
row_index += 1
Label(
    window,
    text='Общее процентное усиление статами:',
    font=parameters_font_style,
    padx=5,
    pady=5,
    width=parameters_width,
    anchor='e',
    justify=RIGHT,
).grid(row=row_index, column=0, padx=10, pady=10)
builds['total_stats_1'].grid(row=row_index, column=1, columnspan=2, padx=10, pady=10)
builds['total_stats_2'].grid(row=row_index, column=3, columnspan=2, padx=10, pady=10)
row_index += 1


def calc():
    base_resists = 50
    role_bonus = 1.2
    for input_index in [1, 2]:
        input_name = f"input_{input_index}"
        damage_parts = {
            'oup': eval(f"{parameters['oup'][input_name].get()} / 10"),
            'power': eval(f"(1 + {parameters['power'][input_name].get()} / 100)"),
            'crit_chance': eval(f"{parameters['crit_chance'][input_name].get()} / 100"),
            'crit': eval(f"({parameters['crit'][input_name].get()} - {base_resists}) / 100"),
            'bp': eval(f"(1 + ({parameters['bp'][input_name].get()} - 50) / 100)"),
            'accuracy': eval(f"(1 + 50 * (1/(50 - {parameters['accuracy'][input_name].get()} + 100) - 1/100))"),
            'percent_bonus': eval(f"(1 + {parameters['percent_bonus'][input_name].get()} / 100)"),
            'damage_boost': eval(f"(1 + {parameters['damage_boost'][input_name].get()} / 100)")
        }

        stats_coefficient = eval(f"{damage_parts['power']}"
                                 + f" * (1 + {damage_parts['crit_chance']} * {damage_parts['crit']})"
                                 + f" * {damage_parts['bp']} * {damage_parts['accuracy']}"
                                 + f" * {damage_parts['percent_bonus']} * {damage_parts['damage_boost']}"
                                 )

        secuence = str(f"{damage_parts['oup']} * {role_bonus} * {stats_coefficient}")
        total_damage = eval(secuence)

        for name, parameter in parameters.items():
            damage_part_name = f"damage_part_{input_index}"
            if name == 'oup':
                parameters[name][damage_part_name].config(text=damage_parts[name])
            elif name == 'crit' or name == 'crit_chance':
                if float(damage_parts['crit']) == 0.0:
                    damage_part_value = '0.0%'
                    parameters[name][damage_part_name].config(text=damage_part_value)
                else:
                    damage_part_value = str(round(eval(
                        f"1 + {damage_parts['crit_chance']} * {damage_parts['crit']}"
                    ), 3))

                    parameters[name][damage_part_name].config(text=damage_part_value)
            else:
                damage_part_value = str(round(damage_parts[name], 3))
                parameters[name][damage_part_name].config(text=damage_part_value)

        stats_coefficient = str(round(eval(f"{stats_coefficient} * 100"))) + '%'
        builds[f"total_stats_{input_index}"].config(text=stats_coefficient)
        total_damage = round(total_damage, 2)
        builds[f"damage_{input_index}"].config(text=total_damage)

    if builds['damage_1']['text'] > builds['damage_2']['text']:
        builds['damage_1'].config(bg=submit_bg_color)
        builds['damage_2'].config(bg='#b9b7b7')
    else:
        builds['damage_1'].config(bg='#b9b7b7')
        builds['damage_2'].config(bg=submit_bg_color)

    damage_diff = eval(
        f"(({builds['damage_2']['text']} - {builds['damage_1']['text']})"
        + f" / ({builds['damage_1']['text']} + {builds['damage_2']['text']}))"
        + f" / 2* 100"
    )
    damage_diff = str(round(damage_diff, 2)) + '%'
    builds['damage_diff'].config(text=damage_diff)


submit_button = Button(
    window,
    text='Рассчитать',
    command=lambda : calc(),
    font='Arial 14 bold',
    bg=submit_bg_color,
    fg=submit_font_color,
    relief=RAISED,
    bd=5,
)

submit_button.grid(row=row_index, column=0, padx=10, pady=10, stick='w')
window.mainloop()




