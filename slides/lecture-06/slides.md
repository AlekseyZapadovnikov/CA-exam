<!-- imported-from: csa-rolling -->
<!-- lecture-id: lecture-06 -->

# lecture-06 — Проблемы аппаратуры. 2 этапа производства. Hardware/Software. Программа. MoC

> Слайды импортированы из `csa-rolling`. Это исходный материал курса, не экзаменационный билет.

<!-- source-slide-deck: slides/06-hw-sw-program-moc.md -->

# Архитектура компьютера

## Лекция 6

## Hardware/Software. <br/> Модель вычислений

Пенской А.В., 2026

---

## Программная система

software system
: A system made up of software, hardware, and data that provides its primary value by the execution of the software.
: --- OMG Essence

*Вывод*: в любой программной системе (software intensive system) есть:

- software ~ программное обеспечение
- hardware ~ аппаратное обеспечение
- data ~ какие-то необходимые для работы данные, являющиеся частью системы

---

## Аппаратное обеспечение

Аппаратное обеспечение
: электронные и механические части вычислительного устройства, входящие в состав системы или сети, исключая программное обеспечение и данные (информацию, которую вычислительная система хранит и обрабатывает). Аппаратное обеспечение включает: компьютеры и логические устройства, внешние устройства и диагностическую аппаратуру, энергетическое оборудование, батареи и аккумуляторы.

----

### Программное обеспечение

Программное обеспечение (ПО)
: совокупность программ, системы обработки информации и программных документов, необходимых для эксплуатации. Позволяет аппаратному обеспечению вычислительной системы выполнять вычисления или функции управления

Computer program
: is a sequence or set of instructions in a programming language for a computer to execute. Computer programs are one component of software, which also includes documentation and other intangible components.
: --- Wikipedia

Программа — это данные (отчуждаема и передаваема)

----

## Что такое Software (и Hardware)?

```text
Настал новый год, так что давайте начнем его с чего-то фундаментального,
разберемся с тем, что беспокоило меня в течение многих лет.

На днях я обедал с подругой, которая не разбирается в компьютерах.
Она спросила меня: "Что такое Software?"

Казалось бы, это простой вопрос для тех людей, кто зарабатывает на жизнь
созданием и разработкой программного обеспечения, но мне пришлось
хорошенько подумать, чтобы дать объяснение, которое она смогла бы понять:

Software -- это та часть компьютерной системы, которая приспосабливает
технику к различным видам использования. Например, на одном и том же
компьютере, но с разным программным обеспечением, вы можете играть в игру,
рассчитывать налоги, писать письмо или книгу, или получать ответы на
вопросы о свиданиях.

Затем я объяснил ей, что, к сожалению, в начале истории развития
компьютеров этой функции дали название "программное обеспечение (software)",
в отличие от "аппаратного обеспечения (hardware)". Ее следовало бы назвать
"гибкое программное обеспечение (flexibleware)".

К сожалению, термин "soft" многие интерпретировали как "легкий (easy)",
что совершенно неверно. Не заблуждайтесь.
То, что мы называем "hardware", должно было называться "easyware", а то,
что мы называем "software", можно было бы назвать "difficultware".
```

[Gerald M. Weinberg, What is Software?](http://secretsofconsulting.blogspot.com/2017/12/what-is-software.html?m=1)

----

### Аппаратура и ПО $\neq$ Hardware и Software

1. Программная/аппаратная составляющая слабо связаны с SW/HW
    - Minix -- одна из самых популярных ОС (встроена в Intel ME/CSME).
2. Часто наименование программной или аппаратной составляющей **зависит от языка**:
    - Virtual-Computer, -Network, -Volume, etc.
    - ПЛИС — это аппаратура, так как работает как схема.
3. Разделение на SW/HW зависит в большей степени от **способа использования** элементной базы.
    - Hardware -- то, что тяжело/долго/дорого поменять;
    - Software -- то, что легко/быстро/дешево поменять.
4. **HW совпадает с аппаратной составляющей**, если нет альтернатив: питание, антенны, аналоговые сигналы и т.п.

----

### Свойства программного обеспечения

<div class="row"><div class="col">

1. Быстрый цикл разработки.
1. Легко заменяется прямо у пользователя.
1. Пользователь как Beta-тестер.
1. Возможно удалённое обновление, в том числе без информированного согласия.
1. Сервис -- вершина владения компьютерной системой.
1. Процесс создания и внедрения ПО автоматизируется (CI/CD).
1. Высокая сложность программ.

*Примечание*: применение "патча", а не разработка.

</div><div class="col">

![](../../assets/course-fig/monkeyuser-final-patch.png) <!-- .element: height="250px" -->
![](../../assets/course-fig/gitflow.png) <!-- .element: height="250px" -->

</div></div>

---

## Типовое HW/SW проектирование

<div class="row"><div class="col">

Проектируем аппаратуру:

- система команд и вычислительные механизмы
- интерфейсы упр. аппаратурой
- цифровая схемотехника, система команд

</div><div class="col">

Пишем программу:

- прикладная задача
- язык и библиотеки
- система команд и вычислительные механизмы (вирт. память, прерывания)
- интерфейсы упр. аппаратурой

</div></div>

<div class="row"><div class="col">

![](../../assets/course-fig/hs-sw-traditional-design.jpg) <!-- .element: height="250px" -->

</div><div class="col">

Проблемы:

<div>

1. излишне шаблонное проектирование
1. высокие интеграционные риски
1. последовательная разработка (сроки)

</div> <!-- .element: class="fragment" -->

</div></div>

----

### Hardware/Software CoDesign

<div class="row"><div class="col">

Мы проектируем систему:

1. Разработка интерфейса HW/SW (системы команд)
1. Разработка моделей HW/SW, для получения обратной связи
1. Разработка HW/SW, верификация моделей.
1. Замена моделей на HW/SW

</div><div class="col">

![](../../assets/course-fig/hs-sw-co-design.jpg)

</div></div>

![](../../assets/course-fig/ES-HW-SW-lifecycle.png) <!-- .element: height="200px" -->

----

### Hardware/Software CoDesign. <br/> Скорость разработки

![](../../assets/course-fig/hw-sw-codesign-time-save.png)

---

## Как выбирать инструменты для разработки Software?

<div>

1. от доступного Hardware и инструментальных средств
1. от доступной команды разработки
1. от прикладной задачи:
    - от области (библиотеки)
    - от модели вычислений (принципов организации вычислительного процесса: параллелизм, конвейеризация, оптимизации, и т.п.)

</div> <!-- .element: class="fragment" -->

----

## Уровень организации вычислительной платформы

<div class="row"><div class="col">

Вычислительная платформа:

![](../../assets/course-fig/platform-general-view.png)

</div><div class="col">

Platform-Based Design:

![](../../assets/course-fig/platform-based-design-only-watch.png) <!-- .element: height="250px" -->

</div></div>

На стадии утилизации:

![](../../assets/course-fig/model-process-computer-one-level.png) <!-- .element: height="150px" -->

---

## Модель вычислений

<div class="row"><div class="col">

1. MoC предоставляет язык для описания моделей процессов/программ/структур.
1. MoC определяет возможности вычислительной машины.
1. MoC характеризует, как исполняется модель (программа): возможные состояния вычислителя, их последовательность, правила переходов (детерминированные или нет).
1. MoC, обычно, минималистичны относительно реальных вычислителей.

</div><div class="col">

Model of Computation -- MoC

![](../../assets/course-fig/moc.png)

[Источник](https://www.researchgate.net/publication/337394921_Pathways_to_cellular_supremacy_in_biocomputing)

</div></div>

---

### MoC. Последовательные модели <br/> Sequential models

<div class="row"><div class="col">

Allows describing a sequential process that can be represented as a sequence of state transitions:

1. Finite state machines
1. Pushdown automata
1. Turing machines
1. Random Access Machines / von Neumann Machine

</div><div class="col">

![](../../assets/course-fig/moc-sequential.png)

Относительно просто реализуются в виде аппаратных схем.

</div></div>

----

<div class="row"><div class="col">

#### Конечные автоматы

![](../../assets/course-fig/fsm.png)

![](../../assets/course-fig/fsm-example.webp)

</div><div class="col">

#### Автомат с магазинной памятью

![](../../assets/course-fig/pushdown-overview.png)

----------

Достоинства:

- Таблица состояний.
- Верифицируемость переходов.
- Простая реализация в схемотехнике и ПО.

</div></div>

----

#### Машина Тьюринга /1

<div class="row"><div class="col">

Машина Тьюринга включает:

- неограниченную двустороннюю ленту, разделенную на ячейки
- устройство управления (головка записи-чтения), которое может находиться в конечном числе состояний.

Управляющее устройство может:

- перемещаться по ленте влево и вправо,
- читать и записывать в ячейки символы конечного алфавита.

</div><div class="col">

![](../../assets/course-fig/turing_machine_fun.jpg)

</div></div>

----

#### Машина Тьюринга /2

1. не может быть реализована на практике
1. обладает полнотой по Тьюрингу <br/> (позволяет реализовать любой **известный** алгоритм)
1. проблема остановки
1. данные и управление отделены
1. ориентирована на реализацию (как ни парадоксально)

----

#### Random Access Machine

![](../../assets/course-fig/ram-machine.jpg)

(современный процессор, с оговорками)

---

### MoC. Функциональные модели <br/> Functional models

<div class="row"><div class="col">

представление вычислительного процесса как совокупности символов и правил их преобразований:

1. Арифметика
1. Лямбда исчисление <br/> (полнота по Тьюрингу)
1. Combinatory logic
1. General recursive functions
1. Abstract rewriting systems.
    - См. [Рефал](https://fprog.ru/2011/issue7/)

</div><div class="col">

![](../../assets/course-fig/math-example.png)<!-- .element: height="550px" -->

- Программа/данные -- математический объект
- Возможна Тьюринг неполнота

</div></div>

----

#### Лямбда исчисление

<div class="row"><div class="col">

4 вида выражений:

1. переменная: $x$, $y$, and $z$
1. константа: $a$, $b$, $c$
1. комбинация (вызов): $s\\;t$
1. абстракция: $\lambda x.s$

3 вида редукций/подстановки:

1. переименование переменных: $\lambda u.u\\;v  \xrightarrow{\alpha} \lambda w.w\\;v$
1. применение функции (подстановка аргумента): $(\lambda x.s)\\;t \xrightarrow{\beta} s[t/x]$
1. сокращение аргумента: $\lambda u.v\\;u  \xrightarrow{\eta} v$.

</div><div class="col">

![](../../assets/course-fig/lambda-calculus-process.png) <!-- .element: height="550px" -->

[Пример дизайна ЯП семейства ML](https://www.cl.cam.ac.uk/teaching/Lectures/funprog-jrh-1996/all.pdf) и факториал на чистом лямбда исчислении.

</div></div>

---

### MoC. Параллельные модели <br/> Concurrent models

<div class="row"><div class="col">

системы, включающие несколько взаимодействующих процессов:

- Kahn process networks -- однонаправленные каналы с неограниченными буферами.
- Actor model -- отправка сообщений в "почтовые ящики".
- Discrete Event -- события в заданные моменты времени.
- Multi-Thread Model -- общая память.
- Synchronous Data Flow -- синхронизированные потоки данных.

</div><div class="col">

![](../../assets/course-fig/moc-kahn-process-network-model.jpg) <!-- .element: height="230px" -->

![](../../assets/course-fig/moc-sdf.jpg) <!-- .element: height="260px" -->

</div></div>

----

### MoC. Примеры распределённых моделей

![](../../assets/course-fig/moc-distrib-openmp.gif) <!-- .element: height="200px" -->
![](../../assets/course-fig/moc-distrib-iec-61499.png) <!-- .element: height="200px" -->

(1) Open Multi-Processing (OpenMP)
(2) IEC 61499

![](../../assets/course-fig/moc-distrib-labview.png) <!-- .element: height="200px" -->
![](../../assets/course-fig/moc-distrib-lingua-franca.png) <!-- .element: height="200px" -->

(3) LabVIEW
(4) LinguaFranca

---

### MoC. Близкие понятия

Парадигмы программирования
: это способ классификации языков программирования на основе их функций. Языки могут относиться к нескольким парадигмам.

Стиль программирования
: это набор правил или рекомендаций, используемых при написании исходного кода компьютерной программы.

**Programming languages**, **Architectural style**, **Computational platform**

----

### MoC. Применение на практике

<div class="row"><div class="col">

1. Computer Science. Формальные модели.
1. Дизайн языков программирования.
1. Ограничение творческого порыва. Контроль сложности.
1. Модель-ориентированная инженерия (xtUML, Capella, Switch-технология и т.п.):
    - для ответственных применений;
    - для переносимости;
    - для экспертизы.

</div><div class="col">

![](../../assets/course-fig/mdd.png)

![](../../assets/course-fig/xuml-diagram.png)

</div></div>

---

### Model-Driven Engineering

<div class="row"><div class="col">

1. Разработка через моделирование предметной области
1. Автоматическая генерация кода из моделей
1. Повышение уровня абстракции при разработке
1. Сокращение разрыва между требованиями и реализацией
1. Улучшение коммуникации между заинтересованными сторонами
1. Снижение сложности разработки масштабных систем

</div><div class="col">

![](../../assets/course-fig/mda-process.png)

</div></div>

----

### Executable UML (xtUML). Process

![](../../assets/course-fig/sw-xtuml-dev-process.png) <!-- .element: height="300px" -->
![](../../assets/course-fig/sw-xtuml-translation.png) <!-- .element: height="300px" -->

----

### xtUML. Models

![](../../assets/course-fig/sw-xtuml-general-models.png)
![](../../assets/course-fig/sw-xtuml-model.png)

----

### Behavior Driven Development (BDD)

<div class="row"><div class="col">

![](../../assets/course-fig/bdd-method.jpg)

</div><div class="col">

![](../../assets/course-fig/bdd-example.png)

</div></div>

---

### Предметно-ориентированные языки (Domain Specific Language)

![](../../assets/course-fig/sw-dsl-idea.png)

---

### Другие примеры MDE

1. **Lingua Franca** -- язык координации для распределённых параллельных приложений реального времени.
1. **CASE-технология** — набор инструментов и методов программной инженерии для проектирования ПО с целью обеспечения качества, надёжности и поддерживаемости продуктов
1. **JetBrains MPS** — платформа для создания предметно-ориентированных языков с проекционным редактированием
1. **LabVIEW** — графическая среда разработки, ускоряющая создание тестовых систем через интуитивное программирование и поддержку любого измерительного оборудования
1. **IEC 61131** — международный стандарт для языков программирования промышленных логических контроллеров (ПЛК)
