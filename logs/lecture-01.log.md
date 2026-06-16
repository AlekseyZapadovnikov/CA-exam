# lecture-01 log

[лог будет заполнен автоматическими скриптами]

## 2026-05-26T09:32:54+00:00 — ERROR

Не удалось получить транскрипт через youtube-transcript-api. fetch: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=p7dKTKv9OKQ! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

There are two things you can do to work around this:
1. Use proxies to hide your IP address, as explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).
2. (NOT RECOMMENDED) If you authenticate your requests using cookies, you will be able to continue doing requests for a while. However, YouTube will eventually permanently ban the account that you have used to authenticate with! So only do this if you don't mind your account being banned!

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!

## Transcript fallback

Получен русский автотранскрипт через `https://pastecontext.com/api.php` по полной YouTube-ссылке. Видео не скачивалось.

## 2026-05-26T12:44:54+03:00 — TICKET DRAFT

Созданы/обновлены рабочие материалы первой лекции:

- `sources/lecture-01/transcript.cleaned.md`
- `sources/lecture-01/source-pack.md`
- `tickets/lecture-01.md`

Билет является черновиком по автотранскрипту и слайдам; места, требующие сверки, помечены `[проверить]`.

## 2026-06-14T19:19:19+00:00 — SKIP

`transcript.raw.md` уже содержит ручной или непустой текст. Файл не перезаписан. Используй --overwrite, если это нужно.
