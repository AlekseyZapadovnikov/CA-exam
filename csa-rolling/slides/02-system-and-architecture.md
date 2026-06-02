# Архитектура компьютера

## Лекция 2

## Информационные и управляющие системы. <br/> Понятия системы и архитектуры

Пенской А.В., 2026

---

## Компьютерные системы

Для курса -- любые системы, оснащённые внутренними алгоритмами.

Примеры:

- светодиодная лампа;
- кабели зарядки мобильных телефонов;
- часы и, конечно, умные часы;
- интерактивные детские игрушки;
- автомобиль и беспилотный автомобиль;
- станок;
- дверной замок;
- и т.п.

---

### Системы с преобладающей программной составляющей

<div class="row"><div class="col">

**Software-intensive systems**: are systems in which software development and/or integration are dominant considerations (i.e., most complex systems these days). This includes computer-based systems ranging from individual software applications, information systems, embedded systems, software product lines and product families and systems-of-systems.

--- ISO/IEC/IEEE 42010

</div><div class="col">

![](/fig/HW-SW-support-cost.png)

**Offtopic**: Что такое Minix?

</div></div>

---

### Классификация компьютерных систем

1. Информационные системы
1. Управляющие системы

----

#### Информационные системы

: получить данные, преобразовать/накопить, и выдать в измененном/обработанном виде.

Особенности:

1. Главный приоритет: производительность.
1. Спекулятивные вычисления.
1. Параллелизм.
1. Кластерные и облачные вычисления.

----

![](/fig/information-systems-evolution-eras.png) <!-- .element height="80%" width="80%" -->

<!-- https://www.researchgate.net/publication/270586955_TOWARDS_PERVASIVE_HYBRID_INTERFACES_Integration_of_ubiquitous_computing_technology_in_the_design_process -->

---

#### Управляющие системы

взаимодействие с реальным физическим миром с целью контроля или управления посредством *получения данных, преобразования/накопления, и выдачи в измененном/обработанном виде*.

Особенности:

1. встроенное исполнение:
    - интеграция в реальный мир,
    - ограниченные ресурсы (энергия),
    - специализация функций, специализация платформы, аппаратуры;
1. автономная эксплуатация;
1. ограниченные вычислительные ресурсы;
1. работа в режиме реального времени (см. след. слайд).

----

#### Реальное время

<div class="row"><div class="col">

![](/fig/realtime.jpg)

</div><div class="col">

Реальное время

- $\neq$ быстро
- $\neq$ абсолютно точно
- $\neq$ без отказов
- $=$ предсказуемо и в срок ($\pm$)

Примеры:

- ГЭС, водосброс.
- Пример где один код это ИС или УС в зависимости от задачи:
    - Видеокодек. <!-- .element: class="fragment" -->

</div></div>

----

#### Эволюция управляющих систем

![](/fig/CPS-elements-evolution.png)

Примеры КФС: гироскутер; безопасные, энергоэффективные вращающиеся двери; провис проводов и передаваемая мощность.

*Extra*: [Пенской А.В., Понятие киберфизической системы считать вредным](https://ryukzak.github.io/2019/11/15/cps-concept.html)

---

## Система. Системная инженерия

----

Системная инженерия (SE)
: это междисциплинарный подход и средство, позволяющее реализовать успешные системы. Он фокусируется на целостном и одновременном понимании потребностей заинтересованных сторон (стейкхолдеров); изучении возможностей; документировании требований; и синтезе, проверке, приемке и разработке решений при рассмотрении всей проблемы, от исследования концепции системы до вывода системы из эксплуатации.

 -- The Guide to the Systems Engineering Body of Knowledge (SEBoK), V.1.3. 2014.

----

### Предмет системной инженерии

<div class="row"><div class="col">

![](/fig/se-domain.jpg)

</div><div class="col">

![](/fig/system-view-of-an-aircraft.png)

</div></div>

Сверхбольшие системы. Требуют множества дисциплин и участников.

----

### Роль системного инженера

Координация и структура: команды разработки, процессов, передачи информации, и т.п.

![](/fig/se-role.jpg)

---

## Понятие системы

(3 точки зрения)

- (1) система как совокупность частей <!-- .element: class="fragment" -->

- (2) система как функциональное место <!-- .element: class="fragment" -->

- (3) система как жизненный цикл <!-- .element: class="fragment" -->

----

### Система как совокупность частей

<div class="row"><div class="col">
System is a combination of interacting elements organized to achieve one or more stated purposes

NOTE 1 A system may be considered as a product or as the services it provides.

NOTE 2 In practice, the interpretation of its meaning is frequently clarified by the use of an associative noun, e.g. aircraft system. Alternatively the word system may be substituted simply by a context dependent synonym, e.g. aircraft, though this may then obscure a system principles perspective.

</div><div class="col">

![](/fig/modeling-complex-system-composition.png)

Так ли это важно?

</div></div>

----

### Структура системы

![](/fig/system-internal-organisation.png) <!-- .element: height="500px" -->

---

### Система как функциональное место

позволяющее её идентифицировать:

- назвать,
- определить,
- выделить (select).

![](/fig/iso-15926-pipe-temporal-parts.jpg)
![](/fig/space-time-map-of-the-chairman.png)

----

#### Представление и точка зрения

<div class="row"><div class="col">

Stakeholder
: Individual or organization having a right, share, claim, or interest in a system or in its possession of characteristics that meet their needs and expectations

 -- ISO/IEC/IEEE 2015

Точка зрения (Viewpoint)
: это спецификация соглашений, правил построения и использования представления с целью решения проблем заинтересованных сторон.

</div><div class="col">

![](/fig/system-project-view.png)

Представление (View)
: Представление системы с заданной точки зрения точки зрения.

(OMG 2010)

</div></div>

----

### Операционное окружение

<div class="row"><div class="col">

- Окружение в котором развертываются системы. Проблема или возможность, в ответ на которую была разработана система, существует в этом окружении.
- Важный фактор при определении возможностей системы, желаемых результатов и выгод для заинтересованных сторон, а также ограничений.

</div><div class="col">

![](/fig/operational-environment-and-enabling-systems.png)

</div></div>

---

### Система как Жизненный цикл

Жизненный цикл системы -- эволюция интересующей системы во времени от концепции до вывода из эксплуатации.

Типовые стадии:

1. Концептуальный этап
2. Этап разработки
3. Этап производства
4. Этап утилизации (англ. utilization)
5. Этап поддержки
6. Этап вывода из эксплуатации

----

#### Обеспечивающая система

Обеспечивающая система -- система, которая дополняет интересующую систему на этапах ее жизненного цикла, но не обязательно вносит непосредственный вклад в ее функционирование во время эксплуатации.

ПРИМЕЧАНИЕ 1 Например, когда система, представляющая интерес, вступает в стадию производства, требуется вспомогательная производственная система.

ПРИМЕЧАНИЕ 2 Каждая обеспечивающая система имеет свой собственный жизненный цикл. Этот Международный стандарт применим к каждой обеспечивающей системе, когда она сама по себе рассматривается как система, представляющая интерес.

 -- ISO 15288

----

![](/fig/system-life-cycle.png)

----

### Разработка успешной системы требует

1. рассмотрения её структуры
1. рассмотрения её функционального места
1. рассмотрения её операционного окружения
1. рассмотрения её жизненного цикла
1. рассмотрения её обеспечивающих систем

Аналогичный результаты получены в:

- OMG Essence,
- СМД-методологии.

---

## Архитектура

![](/fig/geek-and-poke-architecture.jpg)<!-- .element: height="600px" -->

----

### Классическое определение: Гради Буч

Архитектура
: логическая и физическая структура компонентов системы и их взаимосвязи, сформированные всеми стратегическими и тактическими проектными решениями, применяемыми во время разработки.

Логический взгляд
: на систему учитывает концепции, созданные в концептуальной модели, и устанавливает существование и роль ключевых абстракций и механизмов, которые будут определять архитектуру и общий дизайн системы.

Физическая модель
: системы описывает конкретный программный и аппаратный состав реализации системы. Очевидно, что физическая модель зависит от конкретной технологии.

----

### Системная инженерия: ISO 42010

architecture
: [system] fundamental concepts or properties of a system in its environment embodied in its elements, relationships, and in the principles of its design and evolution

architecture description
: work product used to express an architecture

There is no single characterization of what is essential or fundamental to a system; that characterization could pertain to any or all of:

- system constituents or elements;
- how system elements are arranged or interrelated;
- principles of the system’s organization or design; and
- principles governing the evolution of the system over its life cycle.

----

### Сущностные определения

Архитектура -- все важное.

 -- Интернет

Software architecture (en) is the set of design decisions which, if made incorrectly, may cause your project to be cancelled.

 -- Eoin Woods (SEI 2010)

Архитектура программного обеспечения (ru) -- это набор проектных решений, которые, если они будут приняты неправильно, могут привести к отмене вашего проекта.

 -- Eoin Woods (SEI 2010)

---

## Почему архитектура -- это важно?

### V-диаграмма

![](/fig/v-model.png)

----

### Риск откладывания управления рисками

![](/fig/risk-of-delaying-risk-management.png)

----

### Эффект архитектурного проектирования

![](/fig/schedule-overrun-from-amount-of-design.png)

---

## Проблема коммуникации при разработке компьютерных систем

> Poor management can increase software costs more rapidly than any other factor. <br/> -- Barry W. Boehm

----

## Передача информации <br/> и поиск решений

Some critical questions for the success of the system may be missed.

<div class="row"><div class="col">

- Question is beyond the competence of the developer.
- Template design dominates.
- Artificial narrowing of design requirements.
- Substitution of one task to another.
- Inefficient arrangement of priorities at designing.

</div><div class="col">

### Постановка задачи техническим специалистом

![](/fig/communication-problem-senior-and-junior.png)

</div></div>

----

### Попытка разобраться самостоятельно

![](/fig/communication-problem-senior-and-junior-detail.png)

----

### Постановка задачи нетехническим специалистом

![](/fig/communication-problem-manager-and-dev.png)

---

<div class="row"><div class="col">

## Примеры ошибок коммуникации

Выше были теоретические рассуждения.

Теперь несколько примеров из практики.

</div><div class="col">

![](/fig/geek-and-poke-fail.png)<!-- .element: height="600px" -->

</div></div>

----

### Пример проблем с операционным окружением

![](/fig/controller-right2left.png)

----

Подсказка:

![](/fig/controller-right2left-2.png)

Notes: На столе разработчика -- силовые линии лучше увести со стола вверх. В шкафу -- вниз, т.к. техника безопасности.

----

### Пример с коммуникацией между стадиями жизненного цикла

![](/fig/angle-marks.png)

----

Подсказка:

![](/fig/angle-marks-2.png)

Notes: План: вырезать на лазере. Синие точки -- отверстия в качестве маркировки уголка. Делали руками, замучились отмерять.

----

### Пример правильной и практичной интерпретации стандарта

<div class="row"><div class="col">

```text
number
    integer fraction exponent

integer
    digit
    onenine digits
    '-' digit
    '-' onenine digits

digits
    digit
    digit digits

digit
    '0'
    onenine
```

</div><div class="col">

```text
onenine
    '1' . '9'

fraction
    ""
    '.' digits

exponent
    ""
    'E' sign digits
    'e' sign digits
```

</div></div>

Из описания формата JSON. Что такое `number`? Какие есть варианты?

----

#### Что такое number в JSON?

`number` это: short, int, long, big-int, float, double

##### Контекст

- JavaScript -- старая экосистема, разработанная для автоматизации веба на коленке.
    - Следствие: работа с `number` как с `long` в большинстве решений.
- Haskell -- язык, сделанный любителями и профессионалами от математики.
    - Следствие 1: есть `Integer` без ограничения диапазона значений.
    - Следствие 2: библиотека Aeson (стандарт для работы с JSON) интерпретирует `number` как `Integer`.
- Crypto & Blockchain mess -- активное использование ключей.
    - Следствие: числа в 256 бит не предел.

----

##### Проблема

- Передача JSON из Haskell в веб.
- Сериализация `Integer` в `number` формирует очень длинное число, которое парсится в `long`.
- Hash перестаёт совпадать.

##### Решение

- предобработка текста JSON с заменой всех больших `number` на специальную строку;
- постобработка структуры с JSON с возвращением всех `number` к истинным значениям.
