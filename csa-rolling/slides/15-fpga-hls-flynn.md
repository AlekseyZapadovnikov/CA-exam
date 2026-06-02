# Архитектура компьютера

## Лекция 15

## Не фон Неймановские процессоры. <br/> ПЛИС. HLS. Классификация Флинна

Пенской А.В., 2026

---

## Немного повторов

----

### Источники роста производительности?

1. Частота.
1. Специализация системы команд, аппаратуры.
1. Параллелизм уровня бит, инструкций, задач.
1. Адаптация структуры вычислителя под задачу и параллелизм.
1. Динамическая адаптация.

--------------------------

#### И препятствия на его пути

<div class="row"><div class="col">

1. Закон Мура
1. Закон Амдала
1. Закон Деннарда
1. Power Wall
1. Memory Wall

</div><div class="col">

![](/fig/proc-performance-grow.jpg) <!-- .element: height="250px" -->

</div></div>

---

## Виды процессоров (повтор)

### Гибкость и эффективности

![](/fig/architecture-comparison-flexibility-performance-energy.png) <!-- .element: height="300px" -->

<div class="row"><div class="col">

(1) Application-Specific Integrated Circuit
(2) **Coarse-Grained Reconfigurable Arrays**
(3) **Field-Programmable Gate Array**

</div><div class="col">

(4) **Digital Signal Processor** <br/>
(5) **Graphics Processing Unit** <br/>
(6) Central Processing Unit

</div></div>

---

### Spatial vs. Temporal Computation

<div class="row"><div class="col">

![](/fig/cgra-alg.png) <!-- .element height="150px" -->

#### Temporal Computation

![](/fig/cgra-temporal-computation.png) <!-- .element height="150px" -->

"Схема" последовательно выполняет требуемые задачи.

</div><div class="col">

#### Spatial Computation

![](/fig/cgra-asic-structured.png) <!-- .element height="150px" -->

Схема повторяет граф вычислений. Параллелизм (конвейер, потоки).

![](/fig/cgra-fpga-in-a-box.png) <!-- .element height="120px" -->

"Переплетается"

</div></div>

---

### Программируемые логические интегральные схемы

<div class="row"><div class="col">

ПЛИС
: интегральная микросхема, используемая для создания конфигурируемых цифровых электронных схем.

- Логика работы задаётся данными, а не конструкцией.
- Для формирования конфигурации используется специальное ПО и Hardware Description Languages (HDL): Verilog, VHDL...
- "[Ре]конфигурируется", а не "программируется".

</div><div class="col">

![](/fig/fpga-design-flow.jpg) <!-- .element: height="550px" -->

</div></div>

----

#### Hardware Description Language <br/> Register Transfer Level (RTL)

![](/fig/verilog-and-rtl.png)

----

<div class="row"><div class="col">

#### ПЛИС/СБИС (FPGA/ASIC)

![](/fig/fpga-vs-asic-cost.png)

[Источник](https://towardsdatascience.com/introduction-to-fpga-and-its-architecture-20a62c14421c)

</div><div class="col">

#### ПЛИС. Этапы синтеза

![](/fig/fpga-synthesis.jpg)

</div></div>

----

<div class="row"><div class="col">

#### ПЛИС. Устройство

![](/fig/fpga-internal.png)

</div><div class="col">

#### ПЛИС. Lookup tables (LUT)

![](/fig/fpga-lut.png)

</div></div>

----

### CPU vs. FPGA

![](/fig/cgra-cpu-vs-fpga.jpeg) <!-- .element height="600px" -->

Тут: MoC с точки зрения -- как мы используем аппаратные ресурсы.

---

### Высокоуровневый синтез /1 <br/> (High-Level Synthesis)

<div class="row"><div class="col">

Проблемы:

1. Множество вариантов отображения алгоритма в цифровую схему.
1. Выбор зависит от требований.
1. Изменение требований может вызвать перепроектирование.
1. Разработка схем трудоёмка и требует специалистов.
1. Медленные тесты.

</div><div class="col">

![](/fig/hls-tradeoff-examples.png)

**Spatial** vs. **Temporal Computation**

</div></div>

----

#### Высокоуровневый синтез /2

![](/fig/hls-design-flow.png)

----

#### Высокоуровневый синтез. Достоинства

1. Скорость проектирования. Быстрое прототипирование.
1. Переносимость между разными целевыми платформами.
1. Адаптируемость микроархитектуры под новые условия.
1. Автоматизация процесса оптимизации схемы.

#### Высокоуровневый синтез. Недостатки

1. Ограниченный контроль за результатом синтеза. "Чудеса"
1. Кривая обучения (специальность HLS Engineer)
1. Уровень зрелости технологии сильно варьируется:
    - верификация результата;
    - стабильность работы.

---

### Другие подходы описания аппаратуры

#### Chisel

Constructing Hardware in a **Scala** Embedded Language

<div class="row"><div class="col">

![](/fig/chisel-design-and-validation-flow.png)

</div><div class="col">

![](/fig/chisel-code-example.jpeg)

</div></div>

----

#### Bluespec

**High-level hardware description language**. It has a variety of advanced features including a powerful **type system** that can prevent errors prior to synthesis time, and its most distinguishing feature, **Guarded Atomic Actions**, allow you to define hardware components in a modular manner based on their invariants, and let **the compiler pick a scheduler**.

<div class="row"><div class="col">

![](/fig/bluespec-flow.jpg)

</div><div class="col">

![](/fig/bluespec-example.jpg)

</div></div>

----

- **Clash** -- Clash is a **functional** hardware description language that borrows both its syntax and semantics from the functional programming language Haskell.
- **PyHDL** -- turns Python into a hardware description and verification language, providing hardware engineers with the power of the Python ecosystem.
- ...

---

## Классификация параллельных процессоров

1. Таксономия Флинна (1979 год)
2. Классификация Дункана (1990 год)
3. CGRA Classification (2019)

    Liu, Leibo, et al. "A survey of coarse-grained reconfigurable architecture and design: Taxonomy, challenges, and applications." ACM Computing Surveys (CSUR) 52.6 (2019): 1-39.

---

### Таксономия Флинна

<div class="row"><div class="col">

Классификация параллельных процессоров на основе:

1. количества потоков инструкций.
1. количества потоков данных.

Достоинства: простая и понятная.

Недостатки:

1. Не применима к не фон Неймановским архитектурам.
1. Перегруженность класса MIMD.

</div><div class="col">

![](/fig/flynns-taxonomy.png)

</div></div>

----

#### SISD (Single Instruction, Single Data)

![](/fig/flynns-sisd.png)

1. Простой последовательный процессор.
1. Абсолютное большинство рассмотренных ранее процессоров.
1. Включая процессоры с низкоуровневым параллелизмом.

----

#### SIMD (Single Instruction, Multiple Data)

![](/fig/flynns-simd.png)     <!-- .element: height="300px" -->
![](/fig/proc-cpu-vs-gpu.png) <!-- .element: height="300px" -->

1. Одновременное выполнение несколькими процессорами одной инструкции (Lockstep execution).
1. Назначение: однообразная обработка множества наборов данных.
1. Пример: GPU, поиск блока для BitCoin, мат. моделирование.
1. Ключевое ограничение: операции ветвления.

----

#### SIMT (Single Instruction, Multiple Threads)

<div class="row"><div class="col">

![](/fig/simt.png)  <!-- .element: height="300px" -->

</div><div class="col">

![](/fig/simt-code.png) <!-- .element: height="120px" -->
![](/fig/simt-process.png) <!-- .element: height="200px" -->

</div></div>

1. Расширение SIMD, позволяющее работать с оператором ветвления.
1. Широко применяется в современных GPU и GPGPU (CUDA).
1. Включает механизмы синхронизации потоков между собой для достижения lockstep execution.

----

#### MISD (Multiple Instruction, Single Data)

![](/fig/flynns-misd.png)

1. Один поток данных обрабатывается разными наборами инструкций.
1. Обычно выделяется для полноты классификации.
1. На практике -- повышение надёжности работы систем. Защита от ошибок проектирования и алгоритмов. Параллельная разработка и эксплуатация решений задачи.

----

#### MIMD (Multiple Instruction, Multiple Data)

![](/fig/flynns-mimd.png)

1. Множество процессоров автономно выполняют различные инструкции над различными данными.
1. Самый разнообразный класс процессоров по классификации Флинна.
1. Не выделяются подвиды, поэтому будут рассмотрены в контексте классификации Дункана.

---
