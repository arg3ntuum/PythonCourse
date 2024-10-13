# PyGame Breakout

Посилання на оригинальні статті:
- [Building Games With Python 3 and Pygame: Part 1](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-1--cms-30081)
- [Building Games With Python 3 and Pygame: Part 2](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-2--cms-30082)
- [Building Games With Python 3 and Pygame: Part 3](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-3--cms-30083)
- [Building Games With Python 3 and Pygame: Part 4](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-4--cms-30084)
- [Building Games With Python 3 and Pygame: Part 5](https://code.tutsplus.com/tutorials/building-games-with-python-3-and-pygame-part-5--cms-30085)


# Особливості
- Простий GameObject та TextObject
- Простий загальний об'єкт гри
- Простий загальний кнопковий об'єкт
- Конфігураційний файл
- Обробка подій клавіатури та миші
- Блоки, ракетка та м'яч
- Управління рухом ракетки
- Обробка зіткнень м'яча з усім
- Фонове зображення
- Звукові ефекти
- Розширювана система спеціальних ефектів

# Інсталяція і запуск

Сайти, що вам можуть знадобитись(особисто я запускав з iнтерпретатором v.3.12)
- [Python 3.8](https://docs.python.org/3.8/) 
- [Pipenv](https://pipenv.readthedocs.io/en/latest/) 

Напишіть в своєму терміналі дану команду, і вона підгрузить потрібну бібліотеку

```
pip install pipenv
```

Після інсталяції ви побачите десь такий вивід

```
$Collecting pipenv
  Obtaining dependency information for pipenv from https://files.pythonhosted.org/packages/fd/45/9441892f5e7380ec5db371bfbd1f2f1659fed9bf2ea122f1fc20798afda7/pipenv-2024.1.0-py3-none-any.whl.metadata
  Downloading pipenv-2024.1.0-py3-none-any.whl.metadata (19 kB)
Requirement already satisfied: certifi in c:\users\user\pycharmprojects\python_beginners_course-main\course\.venv\lib\site-packages (from pipenv) (2024.7.4)
Collecting packaging>=22 (from pipenv)
  Obtaining dependency information for packaging>=22 from https://files.pythonhosted.org/packages/08/aa/cc0199a5f0ad350994d660967a8efb233fe0416e4639146c089643407ce6/packaging-24.1-py3-none-any.whl.metadata
  Downloading packaging-24.1-py3-none-any.whl.metadata (3.2 kB)
Collecting setuptools>=67 (from pipenv)
  Obtaining dependency information for setuptools>=67 from https://files.pythonhosted.org/packages/ff/ae/f19306b5a221f6a436d8f2238d5b80925004093fa3edea59835b514d9057/setuptools-75.1.0-py3-none-any.whl.metadata
  Downloading setuptools-75.1.0-py3-none-any.whl.metadata (6.9 kB)
Collecting virtualenv>=20.24.2 (from pipenv)
  Obtaining dependency information for virtualenv>=20.24.2 from https://files.pythonhosted.org/packages/59/90/57b8ac0c8a231545adc7698c64c5a36fa7cd8e376c691b9bde877269f2eb/virtualenv-20.26.6-py3-none-any.whl.metadata
  Downloading virtualenv-20.26.6-py3-none-any.whl.metadata (4.5 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv>=20.24.2->pipenv)
  Obtaining dependency information for distlib<1,>=0.3.7 from https://files.pythonhosted.org/packages/8e/41/9307e4f5f9976bc8b7fea0b66367734e8faf3ec84bc0d412d8cfabbb66cd/distlib-0.3.8-py2.py3-none-any.whl.metadata
  Downloading distlib-0.3.8-py2.py3-none-any.whl.metadata (5.1 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv>=20.24.2->pipenv)
  Obtaining dependency information for filelock<4,>=3.12.2 from https://files.pythonhosted.org/packages/b9/f8/feced7779d755758a52d1f6635d990b8d98dc0a29fa568bbe0625f18fdf3/filelock-3.16.1-py3-none-any.whl.metadata
  Downloading filelock-3.16.1-py3-none-any.whl.metadata (2.9 kB)
Collecting platformdirs<5,>=3.9.1 (from virtualenv>=20.24.2->pipenv)
  Obtaining dependency information for platformdirs<5,>=3.9.1 from https://files.pythonhosted.org/packages/3c/a6/bc1012356d8ece4d66dd75c4b9fc6c1f6650ddd5991e421177d9f8f671be/platformdirs-4.3.6-py3-none-any.whl.metadata
  Downloading platformdirs-4.3.6-py3-none-any.whl.metadata (11 kB)
Downloading pipenv-2024.1.0-py3-none-any.whl (3.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 5.7 MB/s eta 0:00:00
Downloading packaging-24.1-py3-none-any.whl (53 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.0/54.0 kB ? eta 0:00:00
Downloading setuptools-75.1.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 6.6 MB/s eta 0:00:00
Downloading virtualenv-20.26.6-py3-none-any.whl (6.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.0/6.0 MB 7.4 MB/s eta 0:00:00
Downloading distlib-0.3.8-py2.py3-none-any.whl (468 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.9/468.9 kB 7.4 MB/s eta 0:00:00
Downloading filelock-3.16.1-py3-none-any.whl (16 kB)
Downloading platformdirs-4.3.6-py3-none-any.whl (18 kB)
Installing collected packages: distlib, setuptools, platformdirs, packaging, filelock, virtualenv, pipenv
Successfully installed distlib-0.3.8 filelock-3.16.1 packaging-24.1 pipenv-2024.1.0 platformdirs-4.3.6 setuptools-75.1.0 virtualenv-20.26.6

[notice] A new release of pip is available: 23.2.1 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip

```

Для того, щоб запустити проєкт треба зайти в файл 

```
 breakout.py
```
і з нього запустити проєкт
# Credits

Використанні кольори і стаття про них: 
https://www.webucator.com/blog/2015/03/python-color-constants-module/

Посилання на оригінальний проєкт: 
https://gitlab.com/the-gigi/pygame-breakout