# Инструкция по использованию

## Запуск локального сервера

### Вариант 1: Через батник (рекомендуется)
```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio\build-tools"
deploy.bat
# Выберите опцию 4 - Start local server
```

### Вариант 2: Напрямую
```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio"
python -m http.server 8000
```

Сайт будет доступен по адресу: http://localhost:8000

## Обновление галерей

### Через батник:
```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio\build-tools"
deploy.bat
# Выберите опцию 3 - Update galleries only
```

### Напрямую:
```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio\build-tools"
python generate_galleries.py
```

## Публикация на GitHub

### Первая публикация:
```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio\build-tools"
deploy.bat
# Выберите опцию 1 - First time setup
```

### Обновление сайта:
```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio\build-tools"
deploy.bat
# Выберите опцию 2 - Update site
# ИЛИ
# Выберите опцию 6 - Quick update (галереи + коммит + пуш)
```

## Добавление изображений

1. Поместите изображения в соответствующую папку:
   - `media/Skin Gallery/` - для скинов
   - `media/Model Gallery/` - для моделей
   - `media/PixelArt Gallery/` - для пиксель-арта
   - `media/Render Gallery/` - для рендеров

2. Запустите обновление галерей (опция 3 в батнике)

3. Опубликуйте изменения (опция 2 или 6 в батнике)

## Переименование изображений по дате

```bash
cd "C:\Users\Professional\Documents\DavaWasab Portfolio\build-tools"
deploy.bat
# Выберите опцию 5 - Rename images by date
```

## Структура проекта

```
DavaWasab Portfolio/
├── index.html          # Главная страница
├── styles.css          # Стили
├── script.js           # JavaScript
├── media/              # Папка с изображениями
│   ├── Skin Gallery/
│   ├── Model Gallery/
│   ├── PixelArt Gallery/
│   └── Render Gallery/
└── build-tools/        # Инструменты сборки (в .gitignore)
    ├── deploy.bat
    ├── generate_galleries.py
    └── rename_images_by_date.py
```

## Возможные проблемы

### Сервер не запускается
- Проверьте, что Python установлен: `python --version`
- Проверьте, что порт 8000 свободен
- Попробуйте другой порт: `python -m http.server 8080`

### Галереи не обновляются
- Убедитесь, что изображения в правильных папках
- Проверьте формат изображений (png, jpg, jpeg, gif)
- Запустите скрипт напрямую для просмотра ошибок

### Git ошибки
- Убедитесь, что Git установлен: `git --version`
- Проверьте, что remote настроен: `git remote -v`
- Проверьте права доступа к репозиторию

## Счётчик посетителей

Счётчик использует localStorage браузера:
- **Today** - уникальные посетители за день (минимум 1)
- **Online** - активные пользователи последние 5 минут (минимум 1)
- Данные сбрасываются в полночь
- Каждому посетителю присваивается уникальный ID

## Особенности

- ✅ Автоматическое URL-кодирование путей к изображениям
- ✅ Защита изображений от копирования
- ✅ Плавная прокрутка при клике на навигацию
- ✅ Система редиректов для соц. сетей
- ✅ Loading screen при загрузке
- ✅ Счётчик посетителей
- ✅ Адаптивный дизайн
