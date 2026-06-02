# Архитектура компьютера

## Лекция *

### NITTA (CGRA)

Пенской А.В., 2024

----

### План лекции

- Архитектура NITTA

---

## NITTA

Гибридная параллельная CGRA архитектура реального времени:

1. **TTA**. Статическое планирование по потоку данных.
1. **NISC**. Программа составляется на уровне управляющих сигналов.
1. **VLIW**. Инструкция управляет группой вычислительных узлов.
1. **MIMD** с распределённой памятью и разнотипными узлами.

![](/fig/nitta-arch.png)

----

### NITTA -- Process Units

<div class="row"><div class="col">

![](/fig/nitta-sum-simple.png) <!-- .element height="150px" -->
![](/fig/nitta-sum-fun-simple.png) <!-- .element height="150px" -->

</div><div class="col">

![](/fig/nitta-accum.png) <!-- .element height="150px" -->
![](/fig/nitta-sum-fun-simple.png) <!-- .element height="150px" -->
![](/fig/nitta-sum-complex.png) <!-- .element height="150px" -->

(и любые другие варианты)

</div></div>

----

### NITTA -- Коммуникация

<div class="row"><div class="col">

SISD

![](/fig/nitta-mem.png) <!-- .element height="150px" -->

MIMD

![](/fig/nitta-mem-2.png) <!-- .element height="150px" -->

</div><div class="col">

TTA / NITTA

![](/fig/nitta-mem-3.png) <!-- .element height="150px" -->

TTA / NITTA future

![](/fig/nitta-mem-4.png) <!-- .element height="150px" -->

</div></div>

---

<div class="row"><div class="col">

### NITTA -- Управление

NITTA предназначенна для циклического исполнения алгоритмов управления и обработки сигналов/данных.

Области применения:

1. разработки встроенных и киберфизических систем;
1. программно-аппаратного тестирования и быстрого прототипирования (HIL и PIL);
1. разработки программируемых ускорителей и сопроцессоров.

</div><div class="col">

![](/fig/nitta-system-target.png) <!-- .element height="650px" -->

</div></div>

----

<div class="row"><div class="col">

### NITTA -- Процесс планирования

Этапы (последовательность условна):

1. Формирование Data Flow Graph.
1. Формирование микроархитектуры для его вычисления.
1. Привязка (Bind) функций на вычислительные блоки.
1. Планирование процесса отталкиваясь от пересылки данных.

</div><div class="col">

![](/fig/nitta-scheduling-process.png) <!-- .element height="650px" -->

</div></div>

----

<div class="row"><div class="col">

### NITTA -- Design Flow

1. Синий -- прикладное программирование.
1.o Зелёный -- аппаратура.
1. Жёлтый -- синтез, планирование, генерация управляющей программы.
1. Монитор -- пользовательский инстрфейс САПР.
1. Чек-лист -- тестирование за счёт совместного моделирования.

</div><div class="col">

![](/fig/nitta-design-flow.png) <!-- .element height="650px" -->

</div></div>

----

### NITTA -- Модель процессора и процесса синтеза

`Lua | Xmile` $\longrightarrow$ `{ Microarch, Model }` $\longrightarrow$ `{ Verilog, Code }`
![](/fig/nitta-target-system-model.png)
![](/fig/nitta-synthesis-model.png)

---

Key technologies: Haskell, Verilog, TypeScript, React, GitHub.

Приходите в проект: [NITTA](https://ryukzak.github.io/projects/nitta/).
