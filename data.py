from orders import Orders
from DE import DE
from controller import assignments




orders = []
des = []

order1 = Orders('1,1', '1', 123)
order2 = Orders('3,3', '2', 321)

de1 = DE(567, '5,5', '3')
de2 = DE(765, '7,7', '4')
de3 = DE(766, '9,9', '5')

orders.append(order1)
orders.append(order2)
des.append(de1)
des.append(de2)
des.append(de3)

assignments(orders,des)
