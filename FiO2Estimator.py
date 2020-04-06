'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Ankit Parekh & David M. Rapoport
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

This is a simple interface for estimating FiO2 %

Input -
    Circuit 1:
        CPAP Pressure
        Inflow of O2

    Circuit 2:
        Mean Pressures
        Inflow of O2

Output -
    Total Flow (L/min)
    FiO2 Estimate

* Note use enter key for quick calculation

Developed by Ankit Parekh & David M. Rapoport
Last Edit: April 5, 2020

'''

import PySimpleGUI as sg

def main():
    sg.theme('Dark Blue 3')
    #Circuit One
    col1 = [[sg.Text('Circuit 1: HFNC with CPAP', text_color='blue', font='Helvetica 16')],
              [sg.Text('CPAP Pressure: ', size=(15,1), text_color='blue', font='Helvetica 16'), sg.InputText(size=(4,1),font='Helvetica 16')],
              [sg.Text('Inflow of O2 : ', size=(15,1),text_color='blue',font='Helvetica 16'), sg.InputText(size=(4,1),font='Helvetica 16')],
              [sg.Text('Total Flow (L/min): ', text_color='blue',font='Helvetica 16'), sg.Text(' ', size=(8, 1),font='Helvetica 16', key='total_flow')],
              [sg.Text('-'*57, text_color='black') ],
              [sg.Text('FiO2 estimate: ', font='Helvetica 20'), sg.Text(' ', size=(3, 1), key='FiO2_1', justification='right', font='Helvetica 20'), sg.Text('%', font='Helvetica 20')],
              [sg.Text('with Pressure =', font='Helvetica 12',justification='left', size=(15,1)), sg.Text('', size=(4, 1), key='press', justification='left', font='Helvetica 12')],
               [sg.Text('O2 =', font='Helvetica 12', size=(15,1)), sg.Text('', size=(4, 1), key='o2', justification='left', font='Helvetica 12')],
               [sg.Text('Flow =', font='Helvetica 12', size=(15,1)), sg.Text('', size=(4, 1), key='flow1', justification='left', font='Helvetica 12')]]


    #Circuit Two
    col2 = [[sg.Text('Circuit 2: S9 Bilevel ', text_color='yellow', font='Helvetica 16')],
            [sg.Text('Mean Pressures: ', size=(15,1), text_color='yellow', font='Helvetica 16'), sg.InputText(size=(4,1),font='Helvetica 16')],
            [sg.Text('Inflow of O2 : ', size=(15,1), text_color='yellow', font='Helvetica 16'), sg.InputText(size=(4,1),font='Helvetica 16')],
            [sg.Text('Total Flow (L/min): ',text_color='yellow', font='Helvetica 16'), sg.Text(' ', size=(8, 1), font='Helvetica 16',key='total_flow2')],
            [sg.Text('-'*57, text_color='black')],
            [sg.Text('FiO2 estimate: ', font='Helvetica 20'), sg.Text(' ', size=(3, 1),key='FiO2_2', justification='right', font='Helvetica 20'), sg.Text('%', font='Helvetica 20')],
            [sg.Text('with Pressure =', font='Helvetica 12', justification='left', size=(15, 1)),
             sg.Text('', size=(4, 1), key='press2', justification='left', font='Helvetica 12')],
            [sg.Text('O2 =', font='Helvetica 12', size=(15, 1)),
             sg.Text('', size=(4, 1), key='o22', justification='left', font='Helvetica 12')],
            [sg.Text('Flow =', font='Helvetica 12', size=(15, 1)),
             sg.Text('', size=(4, 1), key='flow2', justification='left', font='Helvetica 12')]]

    layout = [[sg.Column(col1), sg.Column(col2)],
              [sg.Button('CALCULATE', font='Helvetica 16', bind_return_key=True), sg.Button('EXIT', font='Helvetica 16')]]

    window = sg.Window('FiO2 Estimator. Developed by Ankit Parekh and David M. Rapoport', layout)

    while True:
        event, values = window.read()

        if event in (None, 'EXIT'):
            break

        if event == 'CALCULATE' and (not values[0] or not values[1]):
            window.Element('FiO2_2').Update('')
            window.Element('press').Update('')
            window.Element('o2').Update('')
            window.Element('flow1').Update('')

        elif event == 'CALCULATE' and float(values[0]) > 0 and float(values[1]) > 0:
            total_flow = 3*float(values[0])+5
            window.Element('total_flow').Update(total_flow)
            fio2 = int(min(float(1), (max(float(0), total_flow - float(values[1])) * 0.21 + float(values[1]))/total_flow) * 100)
            window.Element('FiO2_1').Update(fio2)
            window.Element('press').Update((values[0]))
            window.Element('o2').Update((values[1]))
            window.Element('flow1').Update(total_flow)

        if event == 'CALCULATE' and (not values[2] or not values[3]):
            window.Element('FiO2_2').Update('')
            window.Element('press2').Update('')
            window.Element('o22').Update('')
            window.Element('flow2').Update('')

        elif event == 'CALCULATE' and float(values[2]) > 0 and float(values[3]) > 0:
            total_flow2 = float(values[2]) + 10.0
            window.Element('total_flow2').Update(total_flow2)
            fio2 = int(min(float(1), (max(float(0), total_flow2 - float(values[3])) * 0.21 + float(values[3])) / total_flow2) * 100)
            window.Element('FiO2_2').Update(fio2)
            window.Element('press2').Update((values[2]))
            window.Element('o22').Update((values[3]))
            window.Element('flow2').Update(total_flow2)

    window.close()
    del window


if __name__ == '__main__':
    main()




