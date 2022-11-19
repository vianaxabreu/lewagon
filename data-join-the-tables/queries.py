# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """
        SELECT Orders.OrderId, Customers.ContactName,
        Employees.FirstName
        FROM Orders
        JOIN Customers ON Orders.CustomerID = Customers.CustomerID
        JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
        ORDER BY Orders.OrderID
    """
    return db.execute(query).fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """
        SELECT c.ContactName,
        SUM((od.UnitPrice*od.Quantity)) AS amount
        FROM OrderDetails od
        JOIN Orders o ON od.OrderID = o.OrderID
        JOIN Customers c ON o.CustomerID = c.CustomerID
        GROUP BY c.ContactName
        ORDER BY amount ASC
    """
    return db.execute(query).fetchall()

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query = """
        SELECT e.FirstName, e.LastName,
        SUM((od.UnitPrice*od.Quantity)) AS amount
        FROM OrderDetails od
        JOIN Orders o ON od.OrderID = o.OrderID
        JOIN Employees e ON o.EmployeeID  = e.EmployeeID
        GROUP BY (e.FirstName || ' ' || e.LastName)
        ORDER BY amount DESC
        LIMIT 1
    """
    return db.execute(query).fetchone()

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = """
        SELECT c.ContactName, count(o.OrderID) as number_orders
        FROM Customers c
        LEFT JOIN Orders o ON o.CustomerID = c.CustomerID
        GROUP BY c.ContactName
        ORDER BY number_orders ASC
    """
    return db.execute(query).fetchall()
