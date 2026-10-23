import { total, type Order } from './domain/order';

export function runBatch(orders: Order[]): number[] {
  return orders.map(order => {
    if (!order || !Number.isInteger(order.quantity) || order.quantity <= 0
      || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {
      throw new Error('invalid order');
    }
    return total(order);
  });
}
