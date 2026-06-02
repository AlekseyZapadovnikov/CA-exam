# Сопровождение материалов

Этот файл хранит практические инструкции по обновлению источников и билетов.
Корневой `README.md` оставлен для читателя репозитория, а агентские правила
лежат отдельно в `AGENTS.md` и `PIPELINE.md`.

## Общий процесс

1. Обновить запись лекции в `lectures.yaml`.
2. Получить или добавить raw-транскрипт.
3. Извлечь или импортировать слайды в Markdown.
4. Очистить транскрипт.
5. Собрать `sources/lecture-XX/source-pack.md`.
6. Сгенерировать `tickets/lecture-XX.md` по вопросам из `csa-rolling/exam-questions-blitz.md`.
7. Провести ревью по источникам.
8. Исправить билет после ревью.
9. Создать или обновить `tickets/lecture-XX.cram.md`.

Для AI-агента подробный обязательный порядок описан в `PIPELINE.md`.

## `lectures.yaml`

Для каждой лекции используются поля:

- `id` — стабильный идентификатор, например `lecture-01`;
- `title` — название лекции;
- `youtube_url` — ссылка на YouTube, если она есть;
- `slides_path` — путь к слайдам;
- `course_repo_slides_path` — путь к слайдам в `csa-rolling`, если они импортированы оттуда;
- `course_note_path` — путь к конспекту курса, если он есть;
- `status` — текущий статус подготовки;
- `notes` — служебные заметки.

Пример:

```yaml
lectures:
  - id: lecture-01
    title: "Введение. Вычислительные платформы. Структура курса. Оценивание"
    youtube_url: "https://youtu.be/p7dKTKv9OKQ"
    slides_path: "slides/lecture-01/slides.md"
    course_repo_slides_path: "csa-rolling/slides/01-introduction.md"
    course_note_path: "csa-rolling/course-note/01-course-description.md"
    status: "todo"
    notes: ""
```

## Транскрипты

Получить транскрипт для одной лекции:

```bash
python3 scripts/fetch_transcript.py --lecture lecture-XX
```

Полезные флаги:

- `--lecture lecture-XX` — обработать только выбранную лекцию; можно передать несколько раз;
- `--languages ru,en,en-US,en-GB` — указать языки субтитров;
- `--overwrite` — перезаписать существующий `transcript.raw.md`.

Если транскрипт не удалось получить автоматически, добавь его вручную в
`sources/lecture-XX/transcript.raw.md` и явно пометь сомнительные места.

## Слайды

Если слайды уже есть в Markdown из `csa-rolling`, их можно импортировать в:

- `slides/lecture-XX/slides.md`
- `sources/lecture-XX/slides.md`

В таком случае PDF-извлечение не требуется.

Если есть PDF-слайды, положи их в папку лекции и запусти:

```bash
python3 scripts/extract_slides.py --lecture lecture-XX
```

Полезные флаги:

- `--lecture lecture-XX` — обработать только выбранную лекцию; можно передать несколько раз;
- `--overwrite` — перезаписать существующий `sources/lecture-XX/slides.md`.

Если извлечение получилось плохим, проверь `assets/lecture-XX/` и вручную
дополни `sources/lecture-XX/slides.md`.

## Промпты

После подготовки raw-источников агент применяет промпты из `prompts/`:

1. `prompts/clean-transcript.md` — очистка raw-транскрипта.
2. `prompts/build-source-pack.md` — сборка компактного source-pack.
3. `prompts/generate-ticket.md` — генерация билета.
4. `prompts/review-ticket.md` — ревью билета.
5. `prompts/finalize-ticket.md` — финализация и краткая версия.

При генерации билетов список вопросов берётся из
`csa-rolling/exam-questions-blitz.md`, а не из общего содержания лекции.

## Зависимости

Минимально нужен Python 3.10+.

Опциональные зависимости:

- `youtube-transcript-api` — получение YouTube-транскриптов;
- `PyYAML` — полноценное чтение `lectures.yaml`;
- `PyMuPDF` (`fitz`) — извлечение текста и изображений из PDF;
- `pypdf` — fallback для извлечения текста из PDF;
- `pdftoppm` — fallback для рендера страниц PDF в изображения.

Если в системе нет команды `python`, используй `python3`.

## Проверки перед публикацией билета

- `tickets/lecture-XX.md` создан или обновлён.
- `tickets/lecture-XX.cram.md` создан или обновлён.
- Вопросы совпадают с блоком нужной лекции в `exam-questions-blitz.md`.
- Каждый билет отвечает на свой вопрос, а не пересказывает лекцию целиком.
- Все факты подтверждены источниками лекции.
- Сомнительные места помечены `[проверить]`.
- Неподтверждённые места помечены `[нет в источниках]`.
- В конце билета есть `Статус подготовки`.

## Предупреждения

- Автоматические YouTube-субтитры могут быть неточными.
- Не переписывай `transcript.raw.md` вручную без необходимости: лучше сохранять сырой источник как есть.
- Итоговый билет нельзя считать готовым, пока он не прошёл ревью.
- Перед публикацией на GitHub проверь права на исходные материалы курса,
  транскрипты, изображения и вложенный каталог `csa-rolling/`.
