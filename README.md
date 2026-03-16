🩺 MED-REPORT-NORMALIZER

Medical Report Normalization Service
Превращает врачебный текст в структурированные медицинские данные

📌 Зачем этот сервис

В медицине огромное количество данных существует в виде неструктурированного текста:

выписки

протоколы осмотров 

заключения

назначения

эпикризы
 
Этот текст:

трудно анализировать

невозможно валидировать

нельзя безопасно использовать в AI без подготовки

MED-REPORT-NORMALIZER решает эту проблему.

🧠 Врач пишет как человек
📄 Документ хранится как текст
🤖 AI требует структуру

Нормализация — мост между врачом, данными и AI

🎯 Что делает MED-REPORT-NORMALIZER

принимает медицинский текст

извлекает клинический смысл

приводит данные к стандартизированной структуре

подготавливает результат для:

хранения

анализа

валидации

AI / LLM

downstream-сервисов

🧱 Архитектурная идея

Сервис — логика

API — контракт

Боты / UI — только интерфейсы

Медицина = сервисы
Боты = интерфейсы

Этот репозиторий — чистый сервис, без UI и лишней логики.

⚙️ Технологии

Python 3.11+

FastAPI

Pydantic

OpenAPI 3.1

Готов к:

Docker

Kubernetes

Service Mesh

API Gateway

🚀 API
POST /normalize

Нормализация медицинского текста.

Request

{
  "text": "Пациент поступил с жалобами на..."
}


Response

{
  "structured_data": {
    "complaints": [],
    "diagnoses": [],
    "procedures": [],
    "medications": [],
    "notes": ""
  },
  "meta": {
    "version": "0.1.0",
    "normalized_at": "2026-01-XX"
  }
}

📖 OpenAPI

После запуска сервис автоматически предоставляет документацию:

Swagger UI:
http://localhost:8000/docs

OpenAPI JSON:
http://localhost:8000/openapi.json

🧪 Статус проекта

MVP / Core Service Skeleton

✔ API контракт
✔ Валидация
✔ Расширяемая архитектура
✔ Готов к интеграции с AI и другими сервисами

🔮 Планируемые расширения

режимы нормализации (light / clinical / ai-ready)

медицинские словари и справочники

интеграция с:

MED-ORDER-CHECK

RAG-пайплайнами

clinical decision support systems

аудит и трассируемость изменений

👨‍⚕️ Автор

Vladimir Kopylov
Medical Full-Stack Developer · AI/ML Engineer
Emergency Medicine Engineering

GitHub: https://github.com/rolloerro

Telegram: @MSL72Rph

📜 Лицензия

Open-source.
Используйте, расширяйте, интегрируйте — ответственно.
