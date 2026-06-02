<!-- imported-from: csa-rolling -->
<!-- lecture-id: lecture-01 -->

# lecture-01 — Введение. Вычислительные платформы. Структура курса. Оценивание

> Слайды импортированы из `csa-rolling`. Это исходный материал курса, не экзаменационный билет.

<!-- source-slide-deck: slides/01-introduction.md -->

# Архитектура компьютера

## Лекция 1

## Введение. Вычислительные платформы. Структура курса. Оценивание

Пенской А.В., 2026

---

## Ссылки

- Чат: [csa_ак_2026](https://t.me/+KAsszJMPkCZhZTA0)

- Telegram Bot: [@csa_2026_bot](https://t.me/csa_2026_bot)

- Ведомость: [csa-ак-2026](https://docs.google.com/spreadsheets/d/1iebVw-6m9Bmzq_LzqEdVZd0w5ha6oIZpPp4pfbWUXsM/edit?usp=sharing)

- Очереди (SOON): [slap.csa.edu.swampbuds.me](https://slap.csa.edu.swampbuds.me)

------

Материалы: [Gitlab SE ITMO](https://gitlab.se.ifmo.ru/computer-systems/csa-rolling)

---

## Позиционирование курса

Хороший разработчик -- тот, кто умеет делать правильные предположения:

- как устроены системы, с которыми он работает;
- как должны быть устроены системы, которые он делает;
- к каким последствиям могут приводить принятые им решения;
- какие «странности» можно ожидать и почему.

**Цель курса:**

- сформировать базу для предположений (одинаковые механизмы воспроизводятся в разных частях компьютерных систем);
- устранить элементы "магического мышления" и "карго культа".

----

### Отличительные особенности курса

- широта вместо глубины рассмотрения (отсутствие фокуса на конкретной архитектуре);
- акцент на компромиссах, экзотики;
- логика развития компьютерных систем (пантеизм vs. эволюция).

### Курс не готовит

- программистов на низком уровне;
- разработчиков процессоров;
- программистов высокопроизводительных систем;
- разработчиков встроенных систем;
- архитекторов компьютерных систем.

---

### Центральное понятие: <br/> "Вычислительная платформа"

![](../../assets/course-fig/platform-general-view.png)

(для пользователя/программиста/разработчика)

----

### Иерархия уровней платформ/абстракций

<div class="row"><div class="col">

![](../../assets/course-fig/level-of-abstraction-for-computing-system-vert.png) <!-- .element height="600px" -->

</div><div class="col">

![](../../assets/course-fig/vertical-horizontal-arch.png) <!-- .element: height="600px" -->

</div></div>

----

### Platform-based Design. <br/> Разработка системной платформы

![Design Process in Platform-based Methodology](../../assets/course-fig/platform-based-design.png)

*Zeng Haibo, Vishal Shah, Douglas Densmore, and Abhijit Davare. Simple Case Study in Metropolis. Vol. 4. Technical Memorandum UCB/ERL.*

----

### Уровни платформ и продуктов. Специальности

!["OSI Layers" for Coding Careers](../../assets/course-fig/osi-carrers.jpg) <!-- .element height="550px" -->

- OSI Layers for Coding Careers, [link](https://swyx.io/osi-layers-coding-careers)
- Inspired by [OSI Model](https://en.wikipedia.org/wiki/OSI_model)

----

### Тенденции вычислительных платформ

Внутри компьютера:

- смена основной процессорной архитектуры;
- разнообразие (гетерогенность) вычислительных платформ;
    - число использования спец. вычислителей (GPU, TPU);
- реконфигурируемые вычислители.

За пределами компьютера:

- облачные вычисления, server-less;
- распределённые системы, системы систем, IoT;
- вычисление вне доверенного окружения, Blockchain, Smart Contract.

---

## Содержание курса

[README.md](https://gitlab.se.ifmo.ru/computer-systems/csa-rolling/-/blob/master/README.md)

1. Лабораторные работы.
1. Экзамен.
1. Оценивание и баллы.
1. Консультации.
1. Инструментарий курса: [wrench](https://github.com/ryukzak/wrench), [bot](https://github.com/ryukzak/course-bot), [slap](https://github.com/ryukzak/slap).
1. Побочные квесты.
1. Ведомость -- пока сырая, но варианты можно подсмотреть.
