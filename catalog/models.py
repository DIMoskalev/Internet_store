from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="products/image",
        verbose_name="Изображение(превью)",
        help_text="Загрузите изображение(превью) продукта",
        **NULLABLE,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="products",
        **NULLABLE,
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name="Дата последнего изменения",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
            "description",
        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="versions",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии", **NULLABLE
    )
    name = models.CharField(max_length=150, verbose_name="Название версии", **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="Активная версия")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = [
            "product",
            "version_number",
            "name",
        ]


#
# class Contact(models.Model):
#     name = models.CharField(
#         max_length=100,
#         verbose_name="Имя",
#     )
#     phone = models.CharField(
#         max_length=50,
#         verbose_name="Телефон",
#         **NULLABLE,
#     )
#     message = models.TextField(
#         verbose_name="Сообщение",
#         **NULLABLE,
#     )
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Контакт"
#         verbose_name_plural = "Контакты"
