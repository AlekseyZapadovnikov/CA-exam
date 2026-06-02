<!-- imported-from: csa-rolling -->
<!-- lecture-id: lecture-13 -->

# lecture-13 — Иерархия памяти. Устройство памяти. Кеширование

> Слайды импортированы из `csa-rolling`. Это исходный материал курса, не экзаменационный билет.

<!-- source-slide-deck: slides/12-memory-hierarchy-ram.md -->

# Архитектура компьютера

## Лекция 12

## Иерархия памяти. RAM

Пенской А.В., 2026

---

## Иерархия памяти

<div class="row"><div class="col">

Задачи хранения:

1. Исходные данные, необходимые для запуска системы.
1. Рабочие данные, создаваемые и изменяемые в процессе работы системы.

**Проблема**: с ростом скорости памяти растёт её стоимость (производство и размещение).

*Почему она нерешаема?*

</div><div class="col">

Выше -- быстрее и дороже.

![*Memory Hierarchy*](../../assets/course-fig/memory-hierarchy.jpg)

`+` Сетевые хранилища.

Ниже -- больше и дешевле.

</div></div>

----

### Визуализация примечательных задержек

![](../../assets/course-fig/latency-visualization.png)

----

### Иерархия памяти для разработчика

#### Явная иерархия (Expose Hierarchy)

<div class="row"><div class="col">

1. Регистры, SRAM, DRAM, диски доступны как альтернативные хранилища.
1. Посыл: используйте с умом.

</div><div class="col">

![](../../assets/course-fig/memory-cpu-and-hierarchy-expose.png)

</div></div>

Scratchpad-based Memory Scheme (by developer)

#### Скрытая иерархия (Hide Hierarchy)

<div class="row"><div class="col">

1. Модель: одна память, одно адресное пространство.
1. Зависит от использования. Определяется прозрачно.
1. Посыл: мы всё сделаем за тебя.

</div><div class="col">

![](../../assets/course-fig/memory-cpu-and-hierarchy-hide.png)

</div></div>

Cache-based Memory Scheme by Hardware (mostly)

----

### Типовая работа с памятью

![](../../assets/course-fig/memory-translations.png)

План: устройство памяти $\longrightarrow$ устройство кешей (Лекция 13)

---

## Типы доступа к памяти

1. C **произвольным доступом**, Random-Access Memory (RAM). Задержка доступа не зависит от истории запросов.

1. C **последовательным доступом** (жёсткие диски, магнитные ленты, [AWS Tape Gateway](https://aws.amazon.com/storagegateway/vtl/)).
    - Длительная задержка при смене адреса.
    - Часто, высокая скорость последовательной записи/чтения.

1. **Гибридные**: библиотека магнитных лент, векторные операции.

Наша область: от процессора до основной памяти.

---

## Память с произвольным доступом (RAM). Принцип работы

<div class="row"><div class="col">

![Memory array](../../assets/course-fig/memory-array.png)

Массив ячеек памяти $4\times3$ <br/> (4 слова по 3 бита)

</div><div class="col">

- `Address` -- адрес ячейки памяти шириной 2 бита.
- `Decoder` -- [дешифратор](https://ru.wikipedia.org/wiki/Дешифратор), активирует линию (1 из 4 шт.).
- `wordline_i` -- линия, активирующая ячейки требуемого машинного слова.
- `bitline_i` -- линия, на которую выставляется/читается значение бита определённой позиции.
- `stored_bit` -- ячейка памяти.

</div></div>

----

### Технология реализации битовых ячеек

Существует много вариантов реализации ячейки памяти. Типовые:

| Memory Type         | Transistors*Bit | Latency   | Capacity         | Cost/GB         |
|---------------------|-----------------|-----------|------------------|-----------------|
| Flip-flop (Триггер) | $\sim 20$       | 20 ps     | $\sim 1-5kB$     | a lot of $      |
| ROM                 | $\leq 1$        | -         | -                | -               |
| SRAM                | 6               | $1-10 ns$ | $\sim 10kB-10MB$ | $\sim \\$ 1000$ |
| DRAM                | $\frac{1}{2}-1$ | 80 ns     | $\sim 10GB$      | $\sim \\$ 10$   |

Notes: <https://computationstructures.org/lectures/caches/caches.html>

----

### Read Only Memory (ROM) Cell

<div class="row"><div class="col">

Память только для чтения.

Способы реализации:

- Физическое [не]размещение транзисторов (на производстве).
- Пережигание перемычек при однократном программировании (см. [PROM](https://ru.wikipedia.org/wiki/PROM)).

</div><div class="col">

![*ROM*](../../assets/course-fig/rom.png) <!-- .element height="600px" -->

</div></div>

---

### Static Random Access Memory (SRAM)

<div class="row"><div class="col">

Хранение данных при помощи **состояния группы транзисторов** (4 -- инверторы, 2 -- доступ):

1. быстрый доступ на чтение и запись;
1. значение хранится до отключения питания;
1. требует довольно большое количество транзисторов (низкая плотность ячеек).

Далее -- примеры чтения и записи.

</div><div class="col">

![](../../assets/course-fig/memory-sram-cell-1.png)
![](../../assets/course-fig/memory-sram-cell-2.png)

</div></div>

----

#### SRAM Array

![](../../assets/course-fig/memory-sram-array.png) <!-- .element height="600px" -->

----

#### SRAM Read

![](../../assets/course-fig/memory-sram-read.png)

----

#### SRAM Write

![](../../assets/course-fig/memory-sram-write.png)

----

#### SRAM Multiport

![](../../assets/course-fig/memory-sram-multi-port.png)

---

### Dynamic Random Access Memory (DRAM)

<div class="row"><div class="col">

Динамическая память, состояние хранится **в конденсаторе**.

1. состояние конденсатора можно считать лишь раз;
1. состояние конденсатора утекает;
1. требуется контроллер памяти для *регенерации*;
    - увеличивает длительность доступа;
    - блокирует доступ к памяти во время регенерации.
1. один транзистор и конденсатор на ячейку памяти.

</div><div class="col">

![](../../assets/course-fig/dram-a.png) <!-- .element height="250px" -->
![](../../assets/course-fig/dram-b.png) <!-- .element height="250px" -->

</div></div>

----

#### DRAM Read/Write

![](../../assets/course-fig/memory-dram-read-write.png)
