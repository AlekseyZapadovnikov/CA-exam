# Архитектура компьютера

## Лекция 16

### Распределённые системы. Подходы

Пенской А.В., 2024

----

### План лекции

- Прикладной уровень системы
- Распределённые системы
- Erlang/OTP

*Disclaimer*: поверхностный обзор.

---

## Прикладной уровень системы /1

<div class="row"><div class="col">

1. В OSI модели -- уровни связаны условно и взаимозаменяемы. Больше "расстояние" -- меньше взаимосвязь.
1. В компьютерных системах -- аналогично, переходы обеспечиваются:
    - трансляцией;
    - виртуализацией.
1. Что такое *прикладной уровень*?

</div><div class="col">

![](/fig/vertical-horizontal-arch.png) <!-- .element: height="600px" -->

</div></div>

----

### Прикладной уровень системы /2

<div class="row"><div class="col">

1. Это уровень на котором решается "бизнес задача".
1. Выделение уровня условно при использовании языков общего назначения.
1. На каком уровне организации выч. системы бывает?
    - Цифровая схема.
    - Низкоуровневый код.
    - Высокоуровневый код.
    - Процессы. Pipeline.
    - Сервисы.
    - Контейнеры.
    - Виртуальные машины.
    - Группы компьютеров.

</div><div class="col">

![](/fig/vertical-horizontal-arch.png) <!-- .element: height="600px" -->

</div></div>

---

## Распределённые системы

<div class="row"><div class="col">

1. Прикладная задача требует использования множества компьютеров для решения одной задачи / предоставления единого сервиса.
1. Отличительные особенности:
    - сетевая составляющей;
    - отказ узлов;
    - отказ сети.
1. Условная граница между:
    - группа связанных систем;
    - распределённая система.

</div><div class="col">

![](/fig/distributed-system.png)

</div></div>

----

### Построение распределённых систем

<div class="row"><div class="col">

Варианты построения распределённых систем:

1. Горизонтальная взаимодействие в рамках одного уровня:
    - сетевое взаимодействие,
    - клиент-сервер,
    - peer-2-peer,
    - микросервисы/очереди.
1. Формирование новых уровней/инструментов для описания распределённых систем <br/> $\longrightarrow$

</div><div class="col">

![](/fig/client-server.png)
![](/fig/p2p.png)

</div></div>

---

### Различные подходы к построению распределённых систем

1. Distributed Computing Environment/Remote Procedure Calls
    - **DCOM** -- MS Distributed Component Object Model
    - **CORBA** -- OMG Common Object Request Broker Architecture
1. Actor Model-of-Computation
    - **Erlang/OTP** -- Open Telecom Platform
    - **Scala/Akka**
1. Event-Driven. Работа в реальном времени.
    - **IEC 61499** -- function blocks for industrial and control systems.
    - **Ligua Franca** -- coordination language for concurrent and time-sensitive applications.
1. **Serverless compute** service: Amazon Lambda.
1. **Blockchain & Smart Contracts** -- небезопасная среда исполнения.

---

### Erlang/OTP Actors

<div class="row"><div class="col">

![](/fig/erlang-actors.png)

</div><div class="col">

![](/fig/erlang-map-to-hw.jpg)

</div></div>

----

#### Erlang/OTP Supervisors

![](/fig/erlang-sup.png)
![](/fig/erlang-sup-types.png)

<!-- 1. **OpenMP** (Open Multi-Processing) is an API that supports multi-platform shared-memory multiprocessing -->
