# Баг-репорты для формы регистрации

## Баг 1: Кнопка "Регистрация" активна при пустом поле "Электронная почта"

**Описание:** Кнопка "Регистрация" активируется, даже если поле "Электронная почта" пустое.

**Шаги воспроизведения:**
1. Ввести "Иван" в поле "Имя".
2. Оставить поле "Электронная почта" пустым.
3. Ввести "password123" в поле "Пароль".
4. Ввести "password123" в поле "Подтверждение пароля".

**Ожидаемый результат:** Кнопка "Регистрация" должна оставаться неактивной.
**Фактический результат:** Кнопка "Регистрация" активна.

**Приоритет:** Высокий