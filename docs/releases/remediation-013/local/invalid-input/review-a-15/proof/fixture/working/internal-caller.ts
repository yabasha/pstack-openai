import { priceOrder, type Order } from './domain';

export function exampleTotal(): number {
  const order: Order = { quantity: 2 };
  return priceOrder(order);
}
