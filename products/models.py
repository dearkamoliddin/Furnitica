from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'


class ProductColorModel(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Color'
        verbose_name_plural = 'Product Colors'


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Size'
        verbose_name_plural = 'Product Sizes'


class ProductManufactureModel(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(null=True, blank=True, upload_to='manufacture/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Manufacture'
        verbose_name_plural = 'Product Manufactures'


class ProductModel(models.Model):
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')

    name = models.CharField(max_length=288)
    long_description = models.TextField()
    short_description = models.CharField(max_length=288)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    sku = models.CharField(max_length=10, unique=True)
    count = models.PositiveSmallIntegerField()

    manufacture = models.ForeignKey(ProductManufactureModel, on_delete=models.CASCADE, related_name='products')
    color = models.ManyToManyField(ProductColorModel, related_name='products')
    tag = models.ManyToManyField(ProductTagModel, related_name='products')
    category = models.ManyToManyField(ProductCategoryModel, related_name='products')
    size = models.ManyToManyField(ProductSizeModel, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_discount(self):
        return self.discount != 0

    def is_available(self):
        return self.count != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
