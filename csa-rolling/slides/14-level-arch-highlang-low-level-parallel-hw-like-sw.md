# Архитектура компьютера

## Лекция 14

## Уровневая организация. <br/> Низкоуровневый параллелизм. <br/> Языки высокого уровня

Пенской А.В., 2026

---

## Уровневая организация

это естественный способ организации вычислительных систем

<div class="row"><div class="col">

Примеры:

1. Lava Flow или уровневая организация курильщика $\longrightarrow$
1. Уровневый архитектурный стиль (Layered Style)
1. OSI Model
1. Уровни организации вычислительного процесса

Количество уровней -- десятки.

</div><div class="col">

![](/fig/lava-antipattern.jpeg) <!-- .element: height="500px" -->

</div></div>

----

### Open Systems Interconnection (OSI) Model

<div class="row"><div class="col">

Зачем уровни? Обеспечить **модульность** и **вариативность**.

1. Application Layer
1. Presentation Layer
1. Session Layer
1. Transport Layer
1. Network Layer
1. Data Link Layer
1. Physical Layer

Что неверно в визуализации?

</div><div class="col">

![](/fig/osi-meme.png)

</div></div>

----

### Уровни организации выч. процесса

<div class="row"><div class="col">

![](/fig/platform-general-view.png)

1. Layered project organization.
1. Frameworks, библиотеки, API.
1. Языки программирования.
1. Операционные системы.
1. Системы команд (ISA), ПЛИС.
1. Виртуализированные ресурсы.

</div><div class="col">

![](/fig/vertical-horizontal-arch.png) <!-- .element: height="600px" -->

</div></div>

----

### Разделение на уровни (Disaggregation)

![](/fig/platform-disaggregation.png)

<div class="row"><div class="col">

- Интегрированные решения <br/> (in-house). Уровни переплетены и адаптированы.

</div><div class="col">

- Уровни разделены по индустриям/специальностям.
- Эффект масштаба.
- Независимое существование. Закон Мура. [Proebsting's Law](https://proebsting.cs.arizona.edu/law.html)

</div></div>

----

### Смешение уровней. Интеграция

![](/fig/platform-levels-mix-for-realtime.jpg)

1. Зачем: для обеспечения системных характеристик: энергопотребление, реальное время, производительность.
1. Смешение уровней $\longrightarrow$ рост связанности и сложности системы.
1. Смешение уровней при разработке.
1. Сквозные инструментальные решения.

Пример: hard real-time на современном процессоре. Спекулятивное исполнение, OoO, кеш, виртуальная память делают время выполнения недетерминированным $\longrightarrow$ требуется отключение/обход этих механизмов на нижних уровнях.

---

<div class="row"><div class="col">

## Вокруг процессора фон Неймана

1. Параллелизм уровня инструкций, <br/> (Low-Level Parallelism):
    - Суперскалярность
    - VLIW
1. Языки программирования высокого уровня. Структурное программирование.

</div><div class="col">

![](/fig/vertical-horizontal-arch-high-lang-instr-parallelism.png) <!-- .element: height="600px" -->

</div></div>

---

## Низкоуровневый параллелизм <br/> (Low-Level Parallelism)

("не влияет" на прикладное программирование)

1. **Конвейеризация**. Разбиение выполнения инструкции на последовательность этапов.
1. **Множественные функциональные узлы в ЦПУ**. Независимые функциональные блоки для арифметических и булевых операций, выполняемых одновременно.
    - Суперскалярный процессор
    - Very Long Instruction Word

---

### Суперскалярный процессор

<div class="row"><div class="col">

Проблемы:

- разные операции выполняются в разное время (сумма, деление);
- простаивание конвейера во время длинных операций.

Решение:

- анализ потока инструкций на лету и автоматическая параллелизация инструкций, прозрачная для программиста.

</div><div class="col">

![Concept of a superscalar processor](/fig/superscalar-processor-two-unit.png)

Скалярная величина
: величина, которая может быть представлена числом (целочисленным или с плавающей точкой).

</div></div>

----

#### Суперскалярный процессор. Структура

<div class="row"><div class="col">

1. Инструкции читаются в очередь команд по порядку.
1. Декодируются и перемещаются на станции резервирования.
1. Станции резервирования выполняют переупорядочивание:
    - по мере доступности данных;
    - по мере доступности вычислительных ресурсов.

</div><div class="col">

![](/fig/proc-superscalar-processor-organisation.png)

</div></div>

Notes: 18-600 Foundations of Computer Systems, Carnegie Mellon University, J.P. Shen

----

#### Суперскалярный процессор. Достоинства

1. Рост производительности. Сглаживание длительности выполнения инструкций.
1. Повышение уровня загрузки ресурсов.
1. Совместимость с существующим машинным кодом.
1. Компилятор может устранить значительное количество конфликтов за счёт сортировки инструкций.

#### Суперскалярный процессор. Недостатки

1. Конфликты по данным оказывают значительное влияние на производительность и сложность процессора.
1. Высокое энергопотребление.
1. Проблемы детерминированности работы многоядерных процессоров.

----

#### Барьеры памяти (Fence)

<div class="row"><div class="col">

Барьер памяти
: вид барьерной инструкции, которая приказывает компилятору (при генерации инструкций) и процессору (при исполнении инструкций) устанавливать строгую последовательность между обращениями к памяти до и после барьера.

Все обращения к памяти перед барьером будут гарантированно выполнены до первого обращения к памяти после барьера.

Зачем: суперскаляр, OoO и **store buffer** переупорядочивают записи в память ради производительности (**memory reordering**). На одном ядре это незаметно, на нескольких -- последовательность записей "снаружи" отличается от программной.

</div><div class="col">

```c
// Processor 1:
while (f == 0);
// Memory fence required here
print(x);

// Processor 2:
x = 42;
// Memory fence required here
f = 1;
```

![](/fig/barrier-effect-example.png)

</div></div>

---

### Very Long Instruction Word (VLIW)

<div class="row"><div class="col">

**RISC**: упростим процессор за счёт языков высокого уровня!

**VLIW**: упростим процессор за счёт переноса параллелизма инструкций в compile-time!

1. Много АЛУ.
1. Объединим несколько инструкций в одну.
1. Уберём механизмы суперскаляра.
1. Компилятор знает всё $\longrightarrow$ максимальная оптимизация и параллелизм.

</div><div class="col">

![](/fig/superscalar-and-vliw-scheme.png)

</div></div>

----

#### VLIW. Система команд и устройство

![](/fig/vliw-isa.png)

----

<div class="row"><div class="col">

#### VLIW. Достоинства

1. Упрощение процессора, снижение энергопотребления.
1. Упрощение декодера. Рост частоты.
1. Компилятор имеет больше информации о коде, он лучше знает, что параллельно!

</div><div class="col">

#### VLIW. Недостатки

1. Сложность компилятора.
1. Высокая нагрузка на каналы данных и регистровые файлы.
1. Конфликты конвейера приводят к простою всех узлов.
1. Проблемы условных переходов.
1. Низкая плотность кода.
1. Ширина команды -- ограничение микроархитектуры.

</div></div>

![](/fig/cisc-risc-vliw-isa.png)    <!-- .element: height="250px" -->

Notes: <https://www.isi.edu/~youngcho/cse560m/vliw.pdf>

---

### VLIW vs. Superscalar

(структурированный поток vs. просто поток инструкций)

- **Суперскаляр** -- general-purpose CPU (x86, ARM): неоднородные нагрузки, важна совместимость с уже скомпилированным кодом.
- **VLIW** -- DSP, GPU shader cores, специализированные ускорители (TI C6000, Эльбрус, Intel Itanium): регулярные нагрузки, компилятор знает структуру кода.

![](/fig/proc-superscalar-vs-vliw.jpg)<!-- .element height="600" -->

----

### Уровневая организация. <br/> Суперскаляр $\longleftrightarrow$ VLIW

![](/fig/proc-superscalar-epic-vliw.png)

----

**EPIC** (Explicitly Parallel Instruction Computing, Intel Itanium) -- промежуточный вариант: компилятор как в VLIW размечает параллелизм (bundle + stop-биты), но процессор сохраняет рантайм-механики (предикация, спекулятивные загрузки, rotating registers).

Understanding EPIC Architectures and Implementations, Mark Smotherman, <https://people.computing.clemson.edu/~mark/464/acmse_epic.pdf>

**Dynamic VLIW** -- сборка VLIW-бандла переносится из compile-time в run-time, статический ISA (например, x86 или ARM) транслируется в широкое VLIW-слово на лету:

- бинарный транслятор (программный или аппаратный) формирует и кеширует бандлы прямо по ходу исполнения;
- решения о параллелизации учитывают реальные кеш-промахи и поведение ветвлений, чего статическому компилятору не видно;
- сохраняется совместимость со стандартным ISA, под капотом -- VLIW-ядро.
- Примеры: **Transmeta Crusoe/Efficeon** (x86 $\rightarrow$ VLIW через Code Morphing Software), **NVIDIA Denver/Carmel** (ARM $\rightarrow$ внутренний широкий формат с кешированием трансляций).

---

## Языки высокого уровня

Инструкции и Go To $\rightarrow$ Структурные блоки и их последовательность

<div class="row"><div class="col">

1. Естественные элементы для архитектуры фон Неймана:
    - последовательный код$^*$,
    - условный оператор$^*$,
    - циклы, подпрограммы.
1. Распределение регистров. Математические выражения.
1. Функции, области видимости и автоматическая память.
1. Исключения, состояния и перезапуски.$^{**}$
1. Полиморфизм. Замыкания.$^{**}$

- $^*$ -- переосмыслены.
- $^{**}$ -- опустим.

</div><div class="col">

![](/fig/structural-programming.png)
![](/fig/structural-programming-proc.png) <!-- .element height="200" -->
Подробности: [Курс ФП. История](https://gitlab.se.ifmo.ru/functional-programming/main)

</div></div>

----

### Распределение регистров. Выражения

![](/fig/proc-prog-instruction-selection.png) <!-- .element height="370" -->
![](/fig/proc-prog-reg-allocations.png)       <!-- .element height="370" -->

1. Проблемы:
    - кол-во регистров конечно (ARM 15/31, x86 8/16, MIPS 32/32),
    - не все регистры одинаковы (особенно в CISC).
1. Проблема компилятора или низкоуровневого программирования.
1. Код не ограничивается выражениями.
1. Согласование использования регистров между вызовами процедур.

----

#### Раскраска регистров

![](/fig/register-allocation.png) <!-- .element height="450" -->

<div class="row"><div class="col">

$R_1, R_2$ -- регистры аргументов.

$R_{LK}$ -- возврат, $R_1$ -- результат.

</div><div class="col">

Источник: [Register allocation](https://cs420.epfl.ch/archive/20/c/08_reg-alloc.html)

В статье пример с Lisp.

</div></div>

---

### Подпрограммы. Процедуры

<div class="row"><div class="col">

1. Зачем:
    - переиспользование машинного кода,
    - оптимизация работы кеша инструкций.
1. Инструкции:
    - Через `inline`.
    - Через `goto`.
    - Через `call`, `return`.
1. Данные: рабочая память выделена статически.
1. Нет реентерабельности (при статическом выделении).
1. Проблемы: кеширование, сброс регистров, переходы и конвейер.

</div><div class="col">

```c
int *x, *y;
void *SWAP_RET;
int tmp;

swap:
    tmp = *x;
    *x = *y;
    *y = tmp;
    goto *SWAP_RET;
```

```c
int tmp;

void swap(int *x, int *y) {
    tmp = *x;
    *x = *y; // прерывание: isr()
    *y = tmp;
}

int a, b;

void isr() {
    a = 1;
    b = 2;
    swap(&a, &b);
}
```

</div></div>

----

#### Реентерабельность. Рекурсивный вызов

<div class="row"><div class="col">

1. Реализация через `call`, `return`.
    - Статическое выделение памяти для каждого входа.
    - Автоматическая память, стек: `push`, `pop` (рекурсия).
1. Зачем:
    - параллелизм уровня задач,
    - рекурсивные алгоритмы.
1. Проблемы: автоматическая память, утечки данных, перезапись адреса возврата.

```c
int fact(int n) {
    if (n == 0) return 1;
    return n * fact(n - 1);
}
```

</div><div class="col">

```c
struct swap {int* x; int* y; int tmp;};

void swap(struct swap* base) {
    base->tmp = *(base->x);
    *(base->x) = *(base->y);
    *(base->y) = base->tmp;
}

struct swap enter1, enter2;
swap(&enter1);
swap(&enter2);

// или через автоматическую память (стек):
void swap(int* x, int* y) {
    int tmp; // reserve mem
    tmp = *x;
    *x = *y;
    *y = tmp;
}
```

![](/fig/prog-recursive-procedure.png)

</div></div>

---

### Переосмысление условного оператора

- (1) Традиционный подход: встроенная конструкция языка, реализуемая инструментарием (компилятор, интерпретатор).
- (2) Полиморфизм + замыкания (анонимные функции). Smalltalk.

<div class="row"><div class="col">

```smalltalk
Object subclass: #Bool !

Bool subclass: #True
  ifTrue: aBlock ifFalse: bBlock
    ^ aBlock value ! !

Bool subclass: #False
  ifTrue: aBlock ifFalse: bBlock
    ^ bBlock value ! !
```

</div><div class="col">

```smalltalk
(17 * 13 > 220).
>>>true

(17 * 13 > 220)
       ifTrue: [ 'bigger' ]
       ifFalse: [ 'smaller' ].
>>>'bigger'

n := 1.
[ n < 1000 ] whileTrue: [ n := n*2 ].
n
>>> 1024
```

</div></div>

----

- (3) Нормальный порядок вычислений. Ленивые вычисления.

    Охватывающее выражение полностью редуцируется, применяя функции до вычисления аргументов (с кешированием).

<div class="row"><div class="col">

```python
def my_if(cond, if_true, if_false):
    if cond:
        if_true
    else:
        if_false

my_if(True,
      print("foo"),
      print("bar"))
```

```python
if True:
    print("foo")
else:
    print("bar")
```

```python
print("foo")
```

</div><div class="col">

Нормальный порядок (~макросы)

``` c
#define square(X) ((X) * (X))

x = square(1 + 2);
-> x = ((1 + 2) * (1 + 2));
```

Ленивые вычисления:

```haskell
let square x = x * x
 in square (1 + 2)
--
let square x = x * x
    tmp = 1 + 2
 in square tmp
--
let square x = x * x
    tmp = 1 + 2
 in tmp * tmp
```

</div></div>

---

### Переосмысление последовательного кода

- (1) Optional Chaining (Swift).

    Глубокий JSON с опциональными полями.

```swift
let string: String? = "hello" // or nil
let count = string?.count
if count != nil {
    print(count!)
}
```

----

- (2) `async/await`

    То, что выглядит последовательным кодом, им не является (кооперативная многозадачность).

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1) # будет возвращено замыкание, с оставшимся
                           # кодом, которое будет выполнено после
                           # завершения sleep.
    print('world')

asyncio.run(main()) # asyncio.run обеспечивает ожидание асинхронных
                    # функций и запуск соответствующих замыканий.
                    # (кооперативная многозадачность)
```

----

- (3) Монады. Явно определяем операцию связывания (`bind`, `>>=`):
    - результата прошлого шага
    - и действия следующего шага.

(без погружения в детали, очень синтетический пример, без синтаксического сахара и реального применения)

```haskell
class Monad m where
    return :: a -> m a
    (>>=)  :: m a -> (a -> m b) -> m b

instance Monad Maybe where
    return :: a -> Maybe a
    return x = Just x

    (>>=) :: Maybe a -> (a -> Maybe b) -> Maybe b
    Nothing >>= _ = Nothing
    Just x  >>= f = f x

string = Just "hello"
count = string >>= (\s -> return (length s))
```

Async/Await -- см. библиотеку lwt для OCaml.

Детали: см. курс [Функционального программирования](https://gitlab.se.ifmo.ru/functional-programming/main).
