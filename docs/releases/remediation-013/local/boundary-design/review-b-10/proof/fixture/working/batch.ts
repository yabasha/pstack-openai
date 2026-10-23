import { isOrder, total, type Order } from "./domain/order";

export function runBatch(orders: Order[]): Array<number | null> {
  return orders.map(order => {
    if (!isOrder(order)) throw new Error("invalid order");
    const result = total(order);
    return Number.isFinite(result) ? result : null;
  });
}
