# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    query = """
        SELECT OrderID, CustomerID, OrderDate,
	        RANK() OVER (PARTITION BY CustomerID  ORDER BY OrderDate) AS OrderRank
        FROM Orders
    """
    return db.execute(query).fetchall()


def order_cumulative_amount_per_customer(db):
    pass  # YOUR CODE HERE
