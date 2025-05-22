def apply_discount(sales, discount=0.1):
    return [round(sale * (1 - discount), 2) for sale in sales]


def calculate_daily_sales(sales):
    """
    Calculates the total sales for the day.
    :param sales: list of numerical sales values
    :return: total sales sum
    """
    return sum(sales)


if __name__ == "__main__":
    sample_sales = [100, 200, 300]
    discounted_sales = apply_discount(sample_sales, discount=0.2)
    print("Discounted Sales:", discounted_sales)
    print("Total Discounted Sales:", calculate_daily_sales(discounted_sales))

