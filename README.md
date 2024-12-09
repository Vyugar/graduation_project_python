# Дипломный проект

## **Дипломный проект Керимова Вьюгара** в рамках курса **"Python-разработчик. Специалист"** в **GeekBrains**.

Python нашёл себе место почти во всех сферах IT. Разработка веб-сайтов, управление станками ЧПУ, desktop, мобильные приложения, а уж про искусственный интеллект, машинное обучение и анализ данных я вообще молчу.  Сейчас Python лучший друг хоть школьнику, хоть сотруднику научно-исследовательской лаборатории. А что на счёт игр? Компьютерные игры - это огромная доля IT рынка, которая уже набрала и продолжает набирать обороты. 

Благодаря своей простоте и читаемости, Python является отличным выбором для начинающих разработчиков. Но Python не такой уж редкий гость и в крупном геймдеве. Его часто используют:
* для написания игровой логики (для написания внутриигровых скриптов и подсобной работы, не касающейся рендеринга, например, организации серверных элементов управления, внутриигрового моддинга, интерфейсов и прочего);
* для тестирования игр (написания автотестов);
* для создания хобби-проектов, инди и мобильных игр.

**Подготовленный дипломный проект восвящен актуальным вопросам использования Python при разработке игр.**

### **Дипломный проект** подготовлен в формате *docx* и размещен **в корневой папке** данного репозитария.

К диплому в качестве **практического материала** прилагаются написанные на **Python** игры **"Minecraft imitation"**, **"Angry Birds imitation"** и **"Panda3D-Arena"**.

**Игры** были сделаны:
1) **"Minecraft imitation"**  - с использованием библиотек *Ursina* (популярная библиотека для создания 2D и 3D игр) и *Perlin_noise* (для генерации мира с помощью Шумов Перлина) на **Python**;
2) **"Angry Birds imitation"**  - с использованием библиотек *pygame* (одна из самых известных библиотек для разработки 2D-игр на Python), *pymunk* (для создания 2D-физики), *cffi* (для вызова кода C) и *pycparser* (для полного парсера языка C) на **Python**;
3) **"Panda3D-Arena"**  - с использованием библиотек panda3d (популярный 3D игровой движок), panda3d-complexpbr (модуль рендеринга IBL (Image-Based Lighting), который поддерживает отражения в реальном времени и эффекты постобработки в Panda3D) и typing-extensions (дополняет модуль typing дополнительными подсказками типов) на **Python**, а также чуть-чуть языка **GLSL** (языка высокого уровня для программирования шейдеров).

Руководство по запуску игр:
1) **"Minecraft imitation"**:
- перейдите в папку "minecraft" (введите в терминале команду cd minecraft);
- установите все необходимые библиотеки, используя команду pip install -r requirements.txt в терминале;
- затем запустите игру, используя в терминале команду python main.py;
2) **"Angry Birds imitation"**:
- перейдите в папку "angry-birds" (введите в терминале команду cd angry-birds);
- установите все необходимые библиотеки, используя команду pip install -r requirements.txt в терминале;
- перейдите в папку "src" (введите в терминале команду cd src);
- затем запустите игру, используя в терминале команду python main.py;
3) **"Panda3D-Arena"**:
- перейдите в папку "Panda3D-Arena" (введите в терминале команду cd Panda3D-Arena);
- установите все необходимые библиотеки, используя команду pip install -r requirements.txt в терминале;
- затем запустите игру, используя в терминале команду python main.py.