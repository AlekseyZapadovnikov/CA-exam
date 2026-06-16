# lecture-02 log

[лог будет заполнен автоматическими скриптами]

## 2026-06-05T13:10:06+00:00 — ERROR

Библиотека youtube-transcript-api не установлена. Установи ее командой: python -m pip install youtube-transcript-api

## 2026-06-05T13:12:50+00:00 — ERROR

Не удалось получить транскрипт через youtube-transcript-api. fetch: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=q0BOtARY40E! This is most likely caused by:

YouTube is blocking requests from your IP. This usually is due to one of the following reasons:
- You have done too many requests and your IP has been blocked by YouTube
- You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.). Unfortunately, most IPs from cloud providers are blocked by YouTube.

There are two things you can do to work around this:
1. Use proxies to hide your IP address, as explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).
2. (NOT RECOMMENDED) If you authenticate your requests using cookies, you will be able to continue doing requests for a while. However, YouTube will eventually permanently ban the account that you have used to authenticate with! So only do this if you don't mind your account being banned!

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!

## 2026-06-05T14:08:40+00:00 — ERROR

Не удалось получить транскрипт через youtube-transcript-api. fetch: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=q0BOtARY40E! This is most likely caused by:

Request to YouTube failed: 503 Server Error: Service Unavailable for url: https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievable, please create an issue at https://github.com/jdepoix/youtube-transcript-api/issues. Please add which version of youtube_transcript_api you are using and provide the information needed to replicate the error. Also make sure that there are no open issues which already describe your problem!

## 2026-06-14T19:19:20+00:00 — SKIP

`transcript.raw.md` уже содержит ручной или непустой текст. Файл не перезаписан. Используй --overwrite, если это нужно.
