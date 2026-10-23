export type Order = { quantity: number; unitPrice: number };

export function total(order: Order): number {
  return order.quantity * order.unitPrice;
}
