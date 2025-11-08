# Создание Preview изображения для Discord/Twitter

## Инструкция

1. Откройте файл `preview-generator.html` в браузере
2. Нажмите F12 (DevTools)
3. Нажмите Ctrl+Shift+P (Command Palette)
4. Введите "Capture full size screenshot" или "Capture screenshot"
5. Сохраните как `preview.png` в папку `media/`

## Альтернативный способ

Используйте любой онлайн генератор Open Graph изображений:
- https://www.opengraph.xyz/
- https://www.bannerbear.com/tools/open-graph-preview/
- https://ogimage.gallery/

## Требования к изображению

- **Размер:** 1200x630 пикселей
- **Формат:** PNG или JPG
- **Название:** `preview.png`
- **Расположение:** `media/preview.png`

## Проверка превью

После загрузки изображения проверьте превью:
- **Discord:** Отправьте ссылку в любой чат
- **Twitter:** https://cards-dev.twitter.com/validator
- **Facebook:** https://developers.facebook.com/tools/debug/
- **LinkedIn:** https://www.linkedin.com/post-inspector/

## Текущие метатеги

```html
<meta property="og:image" content="https://davawasab.github.io/dava-wasab/media/preview.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

## Важно!

После создания `preview.png`:
1. Поместите файл в папку `media/`
2. Закоммитьте и запушьте на GitHub
3. Подождите 5-10 минут для обновления кэша
4. Проверьте превью в Discord/Twitter
