import matplotlib.pyplot as plt
import numpy as np



def GR(d): #функция для построения графиков
  #  Задаем смещение равное половине ширины прямоугольника:
  x1 = np.arange(1, 5) - 0.1
  x2 = np.arange(1, 5) + 0.3
  x3 = np.arange(1, 5) + 0.1
  x4 = np.arange(1, 5) - 0.3
  #----------------------------------
  y1=[d['vgood_buy']['vhigh'],d['good_buy']['vhigh'],d['acc_buy']['vhigh'],d['unacc_buy']['vhigh']]

  y2 = [d['vgood_buy']['high'],d['good_buy']['high'],d['acc_buy']['high'],d['unacc_buy']['high']]
  y3 = [d['vgood_buy']['med'],d['good_buy']['med'],d['acc_buy']['med'],d['unacc_buy']['med']]
  y4 = [d['vgood_buy']['low'],d['good_buy']['low'],d['acc_buy']['low'],d['unacc_buy']['low']]
  fig, ax = plt.subplots()

  ax.bar(x1, y1, width = 0.2, label='vhigh')
  ax.bar(x2, y2, width = 0.2, label='high')
  ax.bar(x3, y3, width = 0.2, label='med')
  ax.bar(x4, y4, width = 0.2, label='low')

  ax.set_facecolor('seashell')
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.set_facecolor('seashell')
  month = ['car("vgood")','car("good")',  'car("acc")', 'car("unacc")']
  ax.set_xticks([1,2,3,4])
  ax.set_xticklabels(month)
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')

  ax.legend(title='buying')
  fig.savefig('Графики/buying')
  plt.show()

  #  Задаем смещение равное половине ширины прямоугольника:
  x1 = np.arange(1, 5) - 0.1
  x2 = np.arange(1, 5) + 0.3
  x3 = np.arange(1, 5) + 0.1
  x4 = np.arange(1, 5) - 0.3
  #----------------------------------
  y1=[d['vgood_mint']['vhigh'],d['good_mint']['vhigh'],d['acc_mint']['vhigh'],d['unacc_mint']['vhigh']]

  y2 = [d['vgood_mint']['high'],d['good_mint']['high'],d['acc_mint']['high'],d['unacc_mint']['high']]
  y3 = [d['vgood_mint']['med'],d['good_mint']['med'],d['acc_mint']['med'],d['unacc_mint']['med']]
  y4 = [d['vgood_mint']['low'],d['good_mint']['low'],d['acc_mint']['low'],d['unacc_mint']['low']]
  fig, ax = plt.subplots()

  ax.bar(x1, y1, width = 0.2, label='vhigh')
  ax.bar(x2, y2, width = 0.2, label='high')
  ax.bar(x3, y3, width = 0.2, label='med')
  ax.bar(x4, y4, width = 0.2, label='low')

  ax.set_facecolor('seashell')
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.set_facecolor('seashell')
  month = ['car("vgood")','car("good")',  'car("acc")', 'car("unacc")']
  ax.set_xticks([1,2,3,4])
  ax.set_xticklabels(month)
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.legend(title='Maint')
  fig.savefig('Графики/Maint')
  plt.show()

  #  Задаем смещение равное половине ширины прямоугольника:
  x1 = np.arange(1, 5) - 0.1
  x3 = np.arange(1, 5) + 0.1
  x4 = np.arange(1, 5) - 0.3
  #----------------------------------
  y1=[d['vgood_doors']['5more'],d['good_doors']['5more'],d['acc_doors']['5more'],d['unacc_doors']['5more']]


  y3 = [d['vgood_doors']['three'],d['good_doors']['three'],d['acc_doors']['three'],d['unacc_doors']['three']]
  y4 = [d['vgood_doors']['two'],d['good_doors']['two'],d['acc_doors']['two'],d['unacc_doors']['two']]
  fig, ax = plt.subplots()

  ax.bar(x1, y1, width = 0.2, label='5more')

  ax.bar(x3, y3, width = 0.2, label='three')
  ax.bar(x4, y4, width = 0.2, label='two')

  ax.set_facecolor('seashell')
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.set_facecolor('seashell')
  month = ['car("vgood")','car("good")',  'car("acc")', 'car("unacc")']
  ax.set_xticks([1,2,3,4])
  ax.set_xticklabels(month)
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')

  ax.legend(title='Doors')
  fig.savefig('Графики/doors')
  plt.show()

  #  Задаем смещение равное половине ширины прямоугольника:
  x1 = np.arange(1, 5) - 0.1
  x3 = np.arange(1, 5) + 0.1
  x4 = np.arange(1, 5) - 0.3
  #----------------------------------
  y1=[d['vgood_persons']['more'],d['good_persons']['more'],d['acc_persons']['more'],d['unacc_persons']['more']]


  y3 = [d['vgood_persons']['four'],d['good_persons']['four'],d['acc_persons']['four'],d['unacc_persons']['four']]
  y4 = [d['vgood_persons']['two'],d['good_persons']['two'],d['acc_persons']['two'],d['unacc_persons']['two']]
  fig, ax = plt.subplots()

  ax.bar(x1, y1, width = 0.2, label='5more')

  ax.bar(x3, y3, width = 0.2, label='four')
  ax.bar(x4, y4, width = 0.2, label='two')

  ax.set_facecolor('seashell')
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.set_facecolor('seashell')
  month = ['car("vgood")','car("good")',  'car("acc")', 'car("unacc")']
  ax.set_xticks([1,2,3,4])
  ax.set_xticklabels(month)
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')

  ax.legend(title='persons')
  fig.savefig('Графики/persons')
  plt.show()

  #  Задаем смещение равное половине ширины прямоугольника:
  x1 = np.arange(1, 5) - 0.1
  x3 = np.arange(1, 5) + 0.1
  x4 = np.arange(1, 5) - 0.3
  #----------------------------------
  y1=[d['vgood_lug_boot']['big'],d['good_lug_boot']['big'],d['acc_lug_boot']['big'],d['unacc_lug_boot']['big']]


  y3 = [d['vgood_lug_boot']['med'],d['good_lug_boot']['med'],d['acc_lug_boot']['med'],d['unacc_lug_boot']['med']]
  y4 = [d['vgood_lug_boot']['small'],d['good_lug_boot']['small'],d['acc_lug_boot']['small'],d['unacc_lug_boot']['small']]
  fig, ax = plt.subplots()

  ax.bar(x1, y1, width = 0.2, label='big')

  ax.bar(x3, y3, width = 0.2, label='med')
  ax.bar(x4, y4, width = 0.2, label='small')

  ax.set_facecolor('seashell')
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.set_facecolor('seashell')
  month = ['car("vgood")','car("good")',  'car("acc")', 'car("unacc")']
  ax.set_xticks([1,2,3,4])
  ax.set_xticklabels(month)
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')

  ax.legend(title='lug_boot')
  fig.savefig('Графики/lug_boot')
  plt.show()

  #  Задаем смещение равное половине ширины прямоугольника:
  x1 = np.arange(1, 5) - 0.1
  x3 = np.arange(1, 5) + 0.1
  x4 = np.arange(1, 5) - 0.3
  #----------------------------------
  y1=[d['vgood_safety']['high'],d['good_safety']['high'],d['acc_safety']['high'],d['unacc_safety']['high']]


  y3 = [d['vgood_safety']['med'],d['good_safety']['med'],d['acc_safety']['med'],d['unacc_safety']['med']]
  y4 = [d['vgood_safety']['low'],d['good_safety']['low'],d['acc_safety']['low'],d['unacc_safety']['low']]
  fig, ax = plt.subplots()

  ax.bar(x1, y1, width = 0.2, label='high')

  ax.bar(x3, y3, width = 0.2, label='med')
  ax.bar(x4, y4, width = 0.2, label='low')

  ax.set_facecolor('seashell')
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')
  ax.set_facecolor('seashell')
  month = ['car("vgood")','car("good")',  'car("acc")', 'car("unacc")']
  ax.set_xticks([1,2,3,4])
  ax.set_xticklabels(month)
  fig.set_figwidth(12)    #  ширина Figure
  fig.set_figheight(6)    #  высота Figure
  fig.set_facecolor('floralwhite')

  ax.legend(title='safety')
  fig.savefig('Графики/safety')
  plt.show()
