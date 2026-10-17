export type Order = { quantity: number };

export function subtotal(quantity: number): number {
  return quantity * 125;
}

export function priceOrder(order: Order): number {
  return subtotal(order.quantity);
}
