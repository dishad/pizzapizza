from django.db import models
from django.contrib import admin


# Create your models here.
class MenuItem(models.Model):
	PZ = 'Pizza'
	GP = 'Gourmet Pizzas'
	TP = 'Toppings'
	AP = 'Appetizers'
	WI = 'Wings'
	SA = 'Salads'
	SU = 'Soups'
	CA = 'Calzones'
	ST = 'Strombolis'
	GR = 'Grinders'
	WR = 'Wraps'
	PA = 'Pasta Dishes'
	EN = 'Entrees'
	DE = 'Desserts'
	EX = 'Extras'
	BE = 'Beverages'

	categories = (
		(PZ, 'Pizza'),
		(GP, 'Gourmet Pizza'),
		(TP, 'Topping'),
		(AP, 'Appetizer'),
		(WI, 'Wings'),
		(SA, 'Salad'),
		(SU, 'Soup'),
		(CA, 'Calzone'),
		(ST, 'Stromboli'),
		(GR, 'Grinder'),
		(WR, 'Wrap'),
		(PA, 'Pasta'),
		(EN, 'Entree'),
		(DE, 'Dessert'),
		(EX, 'Extra'),
		(BE, 'Beverage'),
	)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=250, null=True, blank=True)
	category = models.CharField(max_length=15, choices=categories, default=PZ)
	def __str__(self):
   		return self.category + ' Item: ' + self.name

class Price(models.Model):
	menuitem = models.ForeignKey(MenuItem, related_name='prices')
	size = models.CharField(max_length=25, null=True, blank=True)
	price = models.CharField(max_length=10, null=True, blank=True)

class PriceInline(admin.StackedInline):
    model = Price

class MenuItemAdmin(admin.ModelAdmin):
    inlines = [
		PriceInline,
    ]

admin.site.register(MenuItem, MenuItemAdmin)
