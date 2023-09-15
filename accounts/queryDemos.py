#***(1) returns all customers from customer table
customers = Customer.objects.all()

# (2) reutrns first customer in the table 
firstCustomer = Customer.objects.first()
# (3) reutrns last customer in the table 
lastCustomer = Customer.objects.last()
# (4) reutrns single customer by name 
customerByName = Customer.objects.get(name='peter piper')
# (5) returns sinle customer by name
customerById = Customer.objects.get(id=4)
# (6) returns all orders related to customer 
firstCustomer.order_set.all()
# (7) returns orders customer name : (query parent model values)
order = Order.object.first()
parentName = order.customer.name
# (8) reutrns products from products table with value of "out door" in category attribute
products = Product.objects.filter(category="Out Door")
# (9) order/sort objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeasy = product.objects.all().order_by('-id')

# (10) reutrns all products with tag of "Sports" : (query many to any fields)
productsFiltered = Product.objects.filter(tags_name="Sports")

''' 
(11)
Q: if the costumer has more than 1 ball , how would you reflect it in database ? 
A: Because there are many different products and this value changes constantly you would most
likely not want to store the value in the database but rather just make this a function
we can run each time we load the customers profile
'''
# returns total count for number of time a "ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product_name="Ball").count()
# returns total count for each product ordered
allOrdered = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.pruduct.name] = 1
# returns : allOrders : {'Ball': 2 , 'BBQ Grill' : 1}


# Related set example 
class ParentModel(models.Model):
    name = models.Charfield(max_lenght=200,null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200,null=True)

parent = ParentModel.objects.first()
#return all child models related to parent 
parent.childmodel_set.all()