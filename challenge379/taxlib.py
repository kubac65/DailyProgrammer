bands = [
    (10_000, 0),
    (30_000, 0.1),
    (100_000, 0.25),
    (None, 0.4)
]

def tax(salary):
    total_tax = 0
    previous_cap = 0

    for cap, rate in bands:
        if cap == salary:
            break

        if cap == None or salary < cap:
            band_tax = int((salary - previous_cap) * rate)
            total_tax = total_tax + band_tax
            previous_cap = cap
            break

        if salary > cap:
            band_tax = int((cap - previous_cap) * rate)
            total_tax = total_tax + band_tax
            previous_cap = cap
            continue

    return total_tax

tax(10000)